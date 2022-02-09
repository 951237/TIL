import csv

PATH_FILE = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_TIL/210120_성적처리프로그램/sample_data.csv"
PATH_RESULT = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_TIL/210120_성적처리프로그램/Result.txt"

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
        total += i
    _sum = total / len(lst_subject)
    return _sum

def main():
    date = open(PATH_FILE)      # csv파일 열기
    reader = csv.reader(date)   # cdv 파일 읽어 객체로 저장

    # 각반별 및 과목별 리스트 선언
    result = {
        '1반' : [],
        '2반' : [],
        '3반' : [],
        '국어' : [],
        '영어' : [],
        '수학' : []
    }

    # csv 객체 읽기
    for i, line in enumerate(reader):
        if i != 0:
            if line[2] == "1반":
                result['1반'].append(line)    # 1반 데이터 모으기
            elif line[2] == "2반":
                result['2반'].append(line)    # 2반 데이터 모으기
            elif line[2] == "3반":
                result['3반'].append(line)    # 3반 데이터 모으기
            result['국어'].append(int(line[3]))     # 국어 점수 모으기
            result['수학'].append(int(line[4]))    # 영어 점수 모으기
            result['영어'].append(int(line[5]))       # 수학 점수 모으기
    
    sum_class_1 = get_class_sum(result['1반'])    # 1반 평균
    sum_class_2 = get_class_sum(result['2반'])    # 2반 평균
    sum_class_3 = get_class_sum(result['3반'])    # 3반 평균

    sum_korean = get_subject_sum(result['국어'])    # 국어 평균
    sum_english = get_subject_sum(result['영어'])  # 영어 평균
    sum_math = get_subject_sum(result['수학'])        # 수학 평균

    # 결과 쓰기
    with open(PATH_RESULT, 'w') as f:
        f.write(f"{'-'*27} '반별 평균 점수' {'-'*27}\n")
        f.write(f'1반 평균 점수 : {sum_class_1} / 2반 평균 점수 : {sum_class_2} / 3반 평균 점수 : {sum_class_3}\n\n')

        f.write(f"{'-'*27} '과목별 평균 점수' {'-'*27}\n")
        f.write(f' 국어 평균 점수 : {sum_korean} / 영어 평균 점수 : {sum_english} / 수학 평균 점수 : {sum_math}')

if __name__ == "__main__":
    main()
