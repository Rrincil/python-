import tkinter as t
import tkinter.messagebox as tm
root = t.Tk()
root.title("学习tikinter")
root["width"] = 600
root["height"] = 400
root["bg"] = "white" #背景色

myfont = ("黑体",16)
l1 = t.Button(root,text="提交",bg="red",width=5,height=1,font= myfont)
l2 = t.Label(root,text="商城",bg="blue",width=200,height=4,font= myfont)
l3 = t.Label(root,text="",bg="green",width=60,height=4,font= myfont)
l4 = t.Button(root,text="提交",bg="red",width=5,height=1,font= myfont)
l2.place(x=0,y=0)
#l3.pack(side="top",fill="x")
l1.place(x=20,y=200)
l4.place(x=100,y=200)
#root.resizable(False,False)

def myin(event):
    tm.showinfo("提示框",event)

'''
鼠标点击事件
<Button-1>  鼠标左键
<Button-2>   鼠标中间键（滚轮）
<Button-3>  鼠标右键
<Double-Button-1>   双击鼠标左键
<Double-Button-3>   双击鼠标右键
<Triple-Button-1>   三击鼠标左键
<Triple-Button-3>   三击鼠标右键
'''
x = input("请输入：")
l1.bind("<Button-1>",myin(x))
root.mainloop()