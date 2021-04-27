import pandas as pd
import tqdm

# 데이터 찾기
    # 기상청 기상자료 개방포털에서 수집
    # https://data.kma.go.kr/data/grnd/selectAwosRltmList.do?pgmNo=638
    # 파일 경로
PATH_SRC = 'coding_TIL/TIL_2021/210426_데이터셋_2020년 기온 데이터_강수량 프로젝트.csv'

# 클래스로 리팩토링
class Weather_2020:
    def __init__(self, path_src=''):
        self.path_src = path_src

    def make_df_rain(self, path_src):
        df = pd.read_csv(path_src, encoding='cp949')
        # 원하는 칼럼만 추출 df[[,,,]]
        df = df[['일시', '평균기온(°C)', '최저기온(°C)', '최고기온(°C)',
                 '일강수량(mm)', '최대 풍속(m/s)', '평균 풍속(m/s)']]
        return df

    def count_rain_day(self, df):
        rain_amount = input('얼마이상의 강수량의 날을 알고 싶으세요? ')
        # 2020년 비가 온날 카운트하기
        day_rain = df.loc[df['일강수량(mm)'] > int(rain_amount)]
        print(f'2020년에 {rain_amount}mm이상 비가 온날은 {len(day_rain)}일 입니다.')

weather = Weather_2020()
df = weather.make_df_rain(PATH_SRC)
weather.count_rain_day(df)
