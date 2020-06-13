from tkinter import *   # 라이브러리 호출

root = Tk()
root.title("951237 tkinter study")
root.geometry("640x480")

def btncmd():
    pass

btn = Button(root, text = "주문", command=btncmd)
btn.pack()

root.mainloop()



