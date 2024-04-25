from PIL import ImageGrab
from nudenet import NudeDetector
import time
import os
import threading
import queue
from tendo import singleton
from ui.main_ui import Win as MainWin
from controller.control import Controller as MainUIController

BAN1 = [
    "FEMALE_GENITALIA_COVERED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
    "ANUS_EXPOSED",
    "MALE_GENITALIA_EXPOSED", 
    "ANUS_COVERED",
]


BAN2 = [
    "BELLY_COVERED",
    "FEET_COVERED",
    "ARMPITS_COVERED",
    "ARMPITS_EXPOSED",
    "BELLY_EXPOSED",
    "FEMALE_BREAST_COVERED",
    "BUTTOCKS_COVERED",
]

tag = {
    # 默认模式
    "DEFAULT": [*BAN1],
    # 严格模式
    "SEVERE": [*BAN1, *BAN2],
    # 色即是空模式 屏蔽一切和女性相关的
    "SEXLESS": [*BAN1, *BAN2, "FACE_FEMALE"],
}


class EloDetector():
    def __init__(self) -> None:
        super().__init__()
        self.mod = "DEFAULT" # 默认模式
        # 读取tmp\\mode.codeJack
        if os.path.exists('tmp\\mode.codeJack'):
            with open('tmp\\mode.codeJack', 'r') as f:
                self.mod = f.read()
        else:
            with open('tmp\\mode.codeJack', 'w') as f:
                f.write(self.mod)
        self.threshold = 3 # 阈值
        self.sleep = 10 # 扫描间隔时间
        if os.path.exists('tmp\\sleep.codeJack'):
            with open('tmp\\sleep.codeJack', 'r') as f:
                self.sleep = int(f.read())
        else:
            with open('tmp\\sleep.codeJack', 'w') as f:
                f.write(str(self.sleep))

        self.trigger_type = 0 # 触发类型 0 是默认 1 是关机
        if os.path.exists('tmp\\trigger_type.codeJack'):
            with open('tmp\\trigger_type.codeJack', 'r') as f:
                self.trigger_type = int(f.read())
        else:
            with open('tmp\\trigger_type.codeJack', 'w') as f:
                f.write(str(self.trigger_type))

        
        self.delay = 0 # 延迟触发时间
        self.split_rows = 3 # 切割行数
        self.split_cols = 3 # 切割列数
        self.results = []
        self.q = None
        self.app = None

    def show_window(self):
        # 查看窗口是否可见
        if self.app.winfo_viewable():
            return
        
        if os.path.exists('tmp\\isclose.codeJack'):
            # 删除掉关闭按钮
            self.app.tk_button_lvf2vmnf.place_forget()
        width = 776
        height = 417
        # 移动窗口到屏幕中央
        screenwidth = self.app.winfo_screenwidth()
        screenheight = self.app.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.app.geometry(geometry)
        # 设置按钮位置
        self.app.tk_button_ok.place(x=281, y=158, width=216, height=47)
        self.app.deiconify()

            
    def init_window(self):
        self.app = MainWin(MainUIController())
        self.app.withdraw()
        self.app.after(100, self.check_queue)
        self.app.mainloop()

    def split_image(self, image):
        # 获取图片尺寸
        width, height = image.size
        # 计算每块的宽度和高度
        block_width = width // self.split_rows
        block_height = height // self.split_cols
        # 列表存储每块图片
        blocks = []
        # 切割图片
        for row in range(self.split_rows):
            for col in range(self.split_cols):
                left = col * block_width
                top = row * block_height
                right = left + block_width
                bottom = top + block_height

                # 根据计算好的坐标位置切割图片
                block = image.crop((left, top, right, bottom))
                blocks.append(block)

        return blocks


    def detect(self, q):
        nude_detector = NudeDetector()
        self.results = []
        while True:
            try:
                screenshot = ImageGrab.grab()
                blocks = self.split_image(screenshot)
                new_result = []
                for index, block in enumerate(blocks):
                    filename = f'tmp/screenshot_part_{index + 1}.png'
                    block.save(filename)
                    result = nude_detector.detect(filename)
                    for item in result:
                        if item['class'] in tag[self.mod]:
                            item['box'] = [item['box'][0] + index % self.split_cols * block.width, item['box'][1] + index // self.split_cols * block.height, item['box'][2], item['box'][3]]
                            new_result.append(item)
                if self.results != new_result and len(new_result) >= self.threshold:
                    time.sleep(self.delay)
                    q.put("show")
                time.sleep(self.sleep)
            except Exception as e:
                pass

    def check_queue(self):
        try:
            # 从队列中获取结果，非阻塞模式
            result = self.q.get_nowait()
            if result == "show":
                if self.trigger_type == 1:
                    os.system("shutdown -s -t 0")
                else:
                    self.show_window()
        except queue.Empty:
            # 如果队列为空，什么都不做
            pass
        finally:
            # 每隔100ms检查一次队列
            self.app.after(100, self.check_queue)

    def start(self):
        self.q = queue.Queue()
        t = threading.Thread(target=self.detect, args=(self.q, ))
        t.setDaemon = True
        t.start()
        self.init_window()


if __name__ == '__main__':
    try:
        me = singleton.SingleInstance()
    except singleton.SingleInstanceException:
        print("Another instance of this program is already running.")
        exit(1)

    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    detector = EloDetector()
    detector.start()