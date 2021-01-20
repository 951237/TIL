# 각 칼럼별 상위 5위 텍스트 출력 및 그래프 그리기
show_graph = ['지역', '소속', '이름', '주민번호','1희망']   # 그래프 그릴 칼럼
lst_col = df.columns.tolist()       # 칼럼을 리스트로 만들기
for i in lst_col:       # 반복 - 칼럼 리스트
    try:    # 오류가 없을 경우
        if i not in show_graph:     # 그래프 표현 칼럼이 아닌 경우
            print(f'{i}')
            t = df[f'{i}'].value_counts()[:5]
            print(t, '\n')
        else:       # 그래프 표현 칼럼일 경우 
            show_col(df, i)
    except: # 오류가 생기면 텍스트 출력
        print('오류발생', '\n')
