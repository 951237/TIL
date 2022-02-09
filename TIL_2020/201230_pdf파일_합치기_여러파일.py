from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import glob
from tqdm import tqdm

# PDF 보관 폴더
PATH_FILE = 'C:\\Users\\User\\Desktop\\영민스캔'

# 파일의 갯수 세어서 반복 회수 카운팅
num_file = len(glob.glob(f'{PATH_FILE}\\*.*')) / 2 + 1

# 파일 만들기 반복
for i in tqdm(range(1, int(num_file)), desc='PDF 파일 합치기'):     # 파일의 전체수의 반만큼 반복(2개를 1개로 합쳐야 함)
    file_1 = f'{PATH_FILE}\\0{i}_01.pdf'
    file_2 = f'{PATH_FILE}\\0{i}_02.pdf'

    # 결과파일 패스
    result = f'C:\\Users\\User\\Desktop\\result_0{i}.pdf'

    # 파일 불러오기
    file1 = PdfFileReader(open(file_1, "rb"), strict=False)
    file2 = PdfFileReader(open(file_2, "rb"), strict=False)

    # pdf writer
    output = PdfFileWriter()

    # pdf파일의 총 페이지
    page_num = file1.getNumPages()

    # 두개의 파일 번갈아가며 합치기
    for i in range(page_num):
        output.addPage(file1.getPage(0+i))
        output.addPage(file2.getPage(((page_num-1))-i))

    outputStream = open(result, "wb")

    output.write(outputStream)
    outputStream.close()

