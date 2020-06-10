# 200610_TIL_부동산 프로그램 작성

# 출력예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/5 2000년

class House:
    # 매물초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물정보 표시
    def show_detail(self):
        print(
            f'{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}')


apt = House('강남', '아파트', '매매', '10억', '2010년')     # 아파트 오브젝트 생성
officetel = House('마포', '오피스텔', '전세', '5억', '2007년')     # 오피스텔 오브젝트 생성
billa = House('송파', '빌라', '월세', '500/5', '2000년')        # 빌라 오브젝트 생성

houses = [apt, officetel, billa]        # 오브젝트 리스트에 넣기
print(f'총 {len(houses)}의 매물이 있습니다.')       # 매물 수량 출력
for i in houses:
    i.show_detail()     # 오브젝트 디테일 출력
