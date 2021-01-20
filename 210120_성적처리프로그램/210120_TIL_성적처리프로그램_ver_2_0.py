import csv
from prettytable import PrettyTable

PATH_FILE = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_TIL/210120_성적처리프로그램/sample_data.csv"

# 반별 평균 구하기 
def get_class_sum(lst_class):
    total = 0
    count = 0
    for line in lst_class:
        k = (int(line[3]) + int(line[4]) + int(line[5])) / 3
        total += k
        count += 1
    _sum = total / count
    return round(_sum, 2)

# 과목별 평균 구하기
def get_subject_sum(lst_subject):
    total = 0
    for i in lst_subject:
        total += int(i)
    _sum = total / len(lst_subject)
    return round(_sum, 2)

def main():
    date = open(PATH_FILE)      # csv파일 열기
    reader = csv.reader(date)   # cdv 파일 읽어 객체로 저장

    # 각반별 및 과목별 리스트 선언
    result = {
        '1반' : {
            '국어' : [],
            '영어' : [],
            '수학' : [],
            '전체' : []
        },
        '2반' : {
            '국어' : [],
            '영어' : [],
            '수학' : [],
            '전체' : []
        },
        '3반' : {
            '국어' : [],
            '영어' : [],
            '수학' : [],
            '전체' : []
        },
        '국어' : [],
        '영어' : [],
        '수학' : []
    }

    # csv 객체 읽기
    for i, line in enumerate(reader):
        if i != 0:
            if line[2] == "1반":
                result['1반']['전체'].append(line)    # 1반 데이터 모으기
                result['1반']['국어'].append(line[3])    # 1반 데이터 모으기
                result['1반']['영어'].append(line[4])    # 1반 데이터 모으기
                result['1반']['수학'].append(line[5])    # 1반 데이터 모으기
            elif line[2] == "2반":
                result['2반']['전체'].append(line)    # 2반 데이터 모으기
                result['2반']['국어'].append(line[3])    # 2반 데이터 모으기
                result['2반']['영어'].append(line[4])    # 2반 데이터 모으기
                result['2반']['수학'].append(line[5])    # 2반 데이터 모으기
            elif line[2] == "3반":
                result['3반']['전체'].append(line)    # 3반 데이터 모으기
                result['3반']['국어'].append(line[3])    # 3반 데이터 모으기
                result['3반']['영어'].append(line[4])    # 3반 데이터 모으기
                result['3반']['수학'].append(line[5])    # 3반 데이터 모으기
            result['국어'].append(int(line[3]))     # 전체 국어 점수 모으기
            result['수학'].append(int(line[4]))    # 전체 영어 점수 모으기
            result['영어'].append(int(line[5]))       # 전체 수학 점수 모으기

    # 과목별 학년 전체 평균 구하기
    total_sum_korean = get_subject_sum(result['국어'])
    total_sum_english = get_subject_sum(result['영어'])
    total_sum_math = get_subject_sum(result['수학'])
    
    # 반별 전체, 국어, 영어, 수학 평균 구하기
    for i in range(1, 4):
        sum_class = get_class_sum(result[f'{i}반']['전체'])
        sum_korean = get_subject_sum(result[f'{i}반']['국어'])
        sum_english = get_subject_sum(result[f'{i}반']['영어'])
        sum_math = get_subject_sum(result[f'{i}반']['수학'])

        t = PrettyTable([f'평균', '국어', '영어', '수학'])
        t.add_row([sum_class, sum_korean, sum_english, sum_math])
        table_text = t.get_string()

        # 반별 평균 결과 쓰기
        with open('Result.txt', 'a+') as f:  # '+a' 파일이 없으면 생성 있으면 추가
            # f.write(f"{'-'*27} '{i}반 평균 ' {'-'*27}\n")
            # f.write(f'{i}반 평균  : {sum_class} / 국어 평균  : {sum_korean} / 영어 평균  : {sum_english} / 수학 평균점수 : {sum_math}\n\n')
            f.write(f'{i}반 평균 점수\n')
            f.write(table_text)
            f.write('\n\n')

    t = PrettyTable(['국어', '영어', '수학'])
    t.add_row([total_sum_korean, total_sum_english, total_sum_math])
    table_text = t.get_string()
    # 과목 전체 평균 결과 쓰기
    with open('Result.txt', 'a+') as f:  # '+a' 파일이 없으면 생성 있으면 추가
        # f.write(f"{'-'*27} '전체 과목별 평균 ' {'-'*27}\n")
        # f.write(f'전체 국어 평균  : {total_sum_korean} / 전체 영어 평균  : {total_sum_english} / 전체 수학 평균 : {total_sum_math}\n\n')
        f.write(f'학년 과목별 평균 점수\n')
        f.write(table_text)
    
if __name__ == "__main__":
    main()
