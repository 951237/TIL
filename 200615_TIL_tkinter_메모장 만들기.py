'''
quiz ) tkinter를 이용한 메모장 프로그램 만들기

[gui조건]
1. title : 제목없음 - windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작시 본문은 비어 있는 상태
5. 하단 status바는 필요없음.
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함.
7. 본문 우측에 상하 스크롤바 넣기
'''
import os
from tkinter import *

root = Tk()
root.title("제목없음 - windows 메모장")     # 제목
root.geometry("640x480")    # 창의 크기

filename = "mynote.txt"     # 파일 이름 지정


def create_file():      # 함수 새파일 생성.
    print("새 파일을 만듭니다.")

def open_file():        # 함수 파일 열기
    if os.paht.isfile(filename):       # 같은 파일이 있으면 True, 아니면 False
        with open(filename, "r", encoding="utf-8") as file:     # 파일 열기
            txt.delete("1.0", END)  # 텍스트 1행, 0칼럼 부터 끝까지 지우기
            txt.insert(END, file.read())    # 끝에 읽은 내용을 넣기

def save_file():    # 함수 저장하기
    with open(filename, "w", encoding="utf-8") as file:     # 파일 열기
        file.write(txt.get("1.0", END)) # 텍스트 1행 0칼럼 부터 끝까지 가져와서 쓰기



# 메뉴만들기
menu = Menu(root)

# 파일메뉴
menu_file = Menu(menu, tearoff=0)     # menu_file 오브젝트 생성
menu_file.add_command(label="Open", command=open_file)  # menu_file에 라벨 달고 명령어 연결
menu_file.add_command(label="Save", command=save_file)  # menu_file에 저장하기 라벨달고 명령어 연결
menu_file.add_separator()       # menu_file에 구분선 삽입
menu_file.add_command(label="Exit", command=root.quit)  # menu_file에 나가기 라벨 달고 명령어 연결
menu.add_cascade(label="File", menu=menu_file)  # menu_file에 파일 라벨 달기

# 편집메뉴
menu.add_cascade(label="Edit", menu=menu_edit)  # menu_edit에 편집 라벨 달기

# 서식
menu.add_cascade(label="Style", menu=menu_style)    #menu_style에 style라벨 달기

# 보기
menu.add_cascade(label="view", menu=menu_view)  # menu_view에 보기 라벨 달기


# 도움말
menu.add_cascade(label="Help", menu=menu_help)  # menu_help에 도움말 라벨 달기

# 스크롤바 처리
scrollbar = Scrollbar(root)     # root에 스크롤바 오브젝트 생성
scrollbar.pack(side="right", fill="y")  # 오른쪽에 붙여서 높이는 꽉차게

# 본문영역
txt = Text(root, yscrollcommand=scrollbar.set)      # 텍스트 창에 스크롤바 설정하기
txt.pack(fill="both", expand=True)      # 텍스트창 양쪽으로 넓히고, 확장하기
scrollbar.config(command=txt.yview)     # 스크롤바와 본문을 맵핑 시킴

root.config(menu=menu)  # menu 설정하기
root.mainloop()

