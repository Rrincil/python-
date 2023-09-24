import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title("GUI编程示例")

# 创建标签
label = tk.Label(window, text="欢迎来到GUI编程！", font=("Arial", 16))
label.pack()

# 创建按钮
button = tk.Button(window, text="点击我！", command=lambda: print("你点击了按钮！"))
button.pack()

# 运行主循环
window.mainloop()
