from tkinter import *

root = Tk()
root.title("951237")
root.geometry("640x480")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady = 10, text="버튼2")    # 버튼내에서 x, y 축으로 여백주기
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

photo = PhotoImage(file="img.png")      # 버튼으로 사용할 이미지 불러오기
btn4 = Button(root, image=photo)    # 버튼을 이미지로 저장하기
btn4.pack()


root.mainloop()