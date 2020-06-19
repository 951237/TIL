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

from tkinter import *

root = Tk()
root.title("제목없음 - windows 메모장")     # 제목
root.geometry("640x480")    # 창의 크기




def create_file():
    print("새 파일을 만듭니다.")

def open_file():
    pass

def save_file():
    pass



# 메뉴만들기
menu = Menu(root)

# 파일메뉴
menu_file = Menu(menu, tearoff=0)     #
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# 편집메뉴
menu.add_cascade(label="Edit", menu=menu_edit)

# 서식
menu.add_cascade(label="Style", menu=menu_style)

# 보기
menu.add_cascade(label="view", menu=menu_view)


# 도움말
menu.add_cascade(label="Help", menu=menu_help)

# 스크롤바 처리
scrollbar = Scrollbar(root)     # 스크롤바 오브젝트 생성
scrollbar.pack(side="right", fill="y")  # 오른쪽에 붙여서 높이는 꽉차게

# 본문영역
txt = Text(root, yscrollcommand=scrollbar.set)      # 텍스트 창에 스크롤바 설정하기
txt.pack(fill="both", expand=True)      # 텍스트창 양쪽으로 넓히고, 확장하기
scrollbar.config(command=txt.yview)     # 스크롤바와 본문을 맵핑 시킴

root.config(menu=menu)
root.mainloop()

