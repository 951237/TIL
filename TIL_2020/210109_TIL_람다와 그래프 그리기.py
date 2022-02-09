# 21010-2719-97199_TIL_데이터프레임 칼람으로 그래프 그리기

# 빈도수에 의한 소팅으로 그래프 그리기
lst_df = ['지역', '1희망', '우대사항', '나이']
for i in lst_df:
   df_temp[i].value_counts(ascending=True).plot.barh(title = i, figsize=(10, 5)) # 
    plt.show()

# 인덱스 소팅에 의해서 그래프 그리기
lst_df = ['지역', '1희망', '우대사항', '나이']
for i in lst_df:
    df_temp[i].value_counts().sort_index(ascending = False).plot.barh(title = i, figsize=(10, 5))
    plt.show()


#snippet/python #코딩/TIL

# 21010-2719-97199_TIL_주민번호로 나이구하기
- map와 람다를 이용
# 주민번호를 통해서 나이구하기 -  map활용
def get_age(df):
    import datetime
    this_year = datetime.datetime.today().year - 1900
    f1 = lambda x: this_year - int(x[:2]) # 인자를 받아서 앞자리 2개를 숫자로 바꿔서 120에서 빼서 나이 구하기
    df['나이'] = df['주민번호'].map(f1)
    return df

#snippet/python
