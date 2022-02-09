name, address, phone = "", "", ""
kor, eng, math, tot, avg = 0, 0, 0, 0, 0

def info_init(iname, iaddress, iphone):
    global name, address, phone
    name, address, phone = iname, iaddress, iphone

def score_init(ikor, ieng, imath):
    global kor, eng, math, tot, avg
    kor, eng, math = ikor, ieng, imath
    tot = kor + eng + math
    avg = tot / 3

def info_prt():
    str = "이름 : {}\n주소 : {}\n연락처 : {}"
    print(str.format(name, address, phone))

def socre_prt():
    global name, address, phone
    str = "국어 : {}\n영어 : {}\n수학 : {}\n합계 : {}\n평균 : {}"
    print(str.format(kor, eng, math, tot, avg))

info_init('리턴제로',"인천시 연수구","010-1234-5678")
info_prt()
score_init(75, 80, 85)
socre_prt()