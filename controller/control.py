"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import os
import webbrowser
# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        self.close_count = 0
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def mouse_enter(self,evt):
        self.ui.tk_button_ok.place(x=self.ui.tk_button_ok.winfo_x(), y=self.ui.tk_button_ok.winfo_y() + 50)
    def open_url_1(self,evt):
        webbrowser.open("https://www.bilibili.com/video/BV1yf421o73d")
        self.ui.withdraw()
    def open_url_2(self,evt):
        webbrowser.open("https://www.bilibili.com/video/BV1vP4y147tC")
        self.ui.withdraw()
    def open_url_3(self,evt):
        webbrowser.open("https://www.bilibili.com/video/BV17J4m147DJ")
        self.ui.withdraw()
    def open_url_4(self,evt):
        webbrowser.open("https://www.bilibili.com/video/BV1ef4y1n7vG")
        self.ui.withdraw()

    def hide_win(self,evt):
        self.close_count += 1
        if self.close_count >= 3:
            # 查看tmp/config.ini文件是否存在
            if not os.path.exists('tmp\\isclose.codeJack'):
                # 不存在则创建
                with open('tmp\\isclose.codeJack', 'w') as f:
                    f.write('by bilibili codeJack')
        # 隐藏窗口
        self.ui.withdraw()