import PyPDF2

FILE = 'cctv.pdf'
reader = PyPDF2.PdfFileReader(FILE)  # pdf파일 읽어오기
num_of_pages = reader.numPages  # pdf파일 전체 쪽수 구하기

writer = PyPDF2.PdfFileWriter()  # pdf 파일 쓰기 객체

result = 'result.pdf'  # 결과물 파일 명

for i in range(num_of_pages):
    if i % 3 == 2:  # 3, 6, 9, ... 페이지만 모으기
        want_page = reader.getPage(i)  # 원하는 페이지 쪽수 저장하기
        writer.addPage(want_page)  # 원하는 페이지 담기

with open(result, 'wb') as output:  # 모은 파일 결과파일로 만들기
    writer.write(output)
