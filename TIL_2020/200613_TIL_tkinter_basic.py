from tkinter import *   # 라이브러리 호출

root = Tk()     # tkinter 오브젝트 셍성
root.title("951237 tkinter study")      # 윈도우창 제목 설정
root.geometry("640x480")        # 윈도우 크기 설정 / 가록 * 세로

def btncmd():       # 윈도우 버튼 명령 함수
    pass

btn = Button(root, text = "주문", command=btncmd)       # 버튼 디자인 및 명령 함수 링크
btn.pack()      # 버튼 생성

root.mainloop()     # 윈도우창 항상 켜져있도록 



