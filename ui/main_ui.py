"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.tk_label_title = self.__tk_label_title(self)
        self.tk_button_ok = self.__tk_button_ok(self)
        self.tk_label_frame_lveuzlan = self.__tk_label_frame_lveuzlan(self)
        self.tk_button_lveuugo5 = self.__tk_button_lveuugo5( self.tk_label_frame_lveuzlan) 
        self.tk_button_lveuxlat = self.__tk_button_lveuxlat( self.tk_label_frame_lveuzlan) 
        self.tk_button_lveuxwh0 = self.__tk_button_lveuxwh0( self.tk_label_frame_lveuzlan) 
        self.tk_button_lveuyl7r = self.__tk_button_lveuyl7r( self.tk_label_frame_lveuzlan) 
        self.tk_button_lvf2vmnf = self.__tk_button_lvf2vmnf(self)
        
    def __win(self):
        self.title("禁止手冲小助手 by bili codeJack")
        # 设置窗口大小、居中
        width = 776
        height = 417
        # 窗口置顶
        self.attributes('-topmost', 1)
        # 不可调整窗口大小
        self.resizable(width=False, height=False)
        # 不在任务栏显示
        self.wm_attributes('-toolwindow', True)
        # 无边框
        self.overrideredirect(True)
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def new_style(self,widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789',5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl
    def __tk_label_title(self,parent):
        label = Label(parent,text="检测到违规内容",anchor="center", bootstyle="warning inverse")
        label.place(x=0, y=0, width=776, height=53)
        return label
    def __tk_button_ok(self,parent):
        btn = Button(parent, text="继续访问", takefocus=False,bootstyle="danger outline")
        btn.place(x=282, y=157, width=216, height=47)
        return btn
    def __tk_label_frame_lveuzlan(self,parent):
        frame = LabelFrame(parent,text="猜你想搜",bootstyle="default")
        frame.place(x=5, y=296, width=761, height=113)
        return frame
    def __tk_button_lveuugo5(self,parent):
        btn = Button(parent, text="手冲的危害", takefocus=False,bootstyle="secondary")
        btn.place(x=15, y=27, width=154, height=42)
        return btn
    def __tk_button_lveuxlat(self,parent):
        btn = Button(parent, text="肾虚怎么办", takefocus=False,bootstyle="secondary")
        btn.place(x=187, y=27, width=154, height=42)
        return btn
    def __tk_button_lveuxwh0(self,parent):
        btn = Button(parent, text="只看不冲有危害吗", takefocus=False,bootstyle="secondary")
        btn.place(x=357, y=27, width=179, height=42)
        return btn
    def __tk_button_lveuyl7r(self,parent):
        btn = Button(parent, text="对同性有感觉正常吗", takefocus=False,bootstyle="secondary")
        btn.place(x=553, y=26, width=187, height=42)
        return btn
    def __tk_button_lvf2vmnf(self,parent):
        btn = Button(parent, text="马上关掉", takefocus=False,bootstyle="success")
        btn.place(x=601, y=85, width=175, height=35)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_ok.bind('<Enter>',self.ctl.mouse_enter)
        self.tk_button_lveuugo5.bind('<Button-1>',self.ctl.open_url_1)
        self.tk_button_lveuxlat.bind('<Button-1>',self.ctl.open_url_2)
        self.tk_button_lveuxwh0.bind('<Button-1>',self.ctl.open_url_3)
        self.tk_button_lveuyl7r.bind('<Button-1>',self.ctl.open_url_4)
        self.tk_button_lvf2vmnf.bind('<Button-1>',self.ctl.hide_win)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_title),font=("微软雅黑",-24,"bold"))
        sty.configure(self.new_style(self.tk_button_ok),font=("微软雅黑",-20,"bold"))
        sty.configure(self.new_style(self.tk_button_lveuugo5),font=("微软雅黑",-18,"bold"))
        sty.configure(self.new_style(self.tk_button_lveuxlat),font=("微软雅黑",-18,"bold"))
        sty.configure(self.new_style(self.tk_button_lveuxwh0),font=("微软雅黑",-18,"bold"))
        sty.configure(self.new_style(self.tk_button_lveuyl7r),font=("微软雅黑",-18,"bold"))
        sty.configure(self.new_style(self.tk_button_lvf2vmnf),font=("微软雅黑",-18,"bold"))
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()