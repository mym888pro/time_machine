import tkinter as tk
from time import strftime
from datetime import datetime

class PhoneClock:
    def __init__(self, root):
        self.root = root
        self.root.title("手机时钟")
        self.root.geometry("300x500")  # 类似手机屏幕的比例
        self.root.configure(bg='black')  # 黑色背景更接近手机风格
        
        # 使窗口无边框，更像手机应用
        self.root.overrideredirect(False)
        
        # 添加日期标签
        self.date_label = tk.Label(root, font=('Helvetica', 14), bg='black', fg='white')
        self.date_label.pack(pady=20)
        
        # 添加时间标签
        self.time_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
        self.time_label.pack(pady=30)
        
        # 添加秒和AM/PM标签
        self.seconds_label = tk.Label(root, font=('Helvetica', 16), bg='black', fg='white')
        self.seconds_label.pack()
        
        # 添加星期标签
        self.day_label = tk.Label(root, font=('Helvetica', 18), bg='black', fg='white')
        self.day_label.pack(pady=20)
        
        # 添加退出按钮
        self.exit_button = tk.Button(root, text="退出", font=('Helvetica', 12), 
                                    command=root.quit, bg='#333333', fg='white')
        self.exit_button.pack(pady=30)
        
        # 初始更新时间
        self.update_time()
    
    def update_time(self):
        # 获取当前时间
        current_time = datetime.now()
        
        # 格式化时间
        time_string = current_time.strftime("%H:%M")  # 24小时制
        # 如果要12小时制，可以使用: time_string = current_time.strftime("%I:%M")
        
        # 格式化日期
        date_string = current_time.strftime("%Y年%m月%d日")
        
        # 格式化秒和AM/PM
        seconds_string = current_time.strftime("%S")
        ampm_string = current_time.strftime("%p")  # AM或PM
        
        # 格式化星期
        day_string = current_time.strftime("%A")
        
        # 更新标签
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        self.seconds_label.config(text=f"{seconds_string} {ampm_string}")
        self.day_label.config(text=day_string)
        
        # 每200毫秒更新一次
        self.time_label.after(200, self.update_time)

# 创建主窗口
root = tk.Tk()
clock = PhoneClock(root)
root.mainloop()
