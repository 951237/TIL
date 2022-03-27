import re
text = "문의 사항이 잇으시면 032-232-3245으로 연락을 주시기 바랍니다."

regex = re.compile(r'(\d{3})-(\d{3}-\d{4})') # 그룹1 :숫자3개 , 그룹2 : 숫자3개-숫자4개
matchobj = regex.search(text)
area_code = matchobj.group(1)
num = matchobj.group(2)
full_num = matchobj.group()
print(f'그룹 전체 : {full_num}')
print(f'area_code - num : {area_code}-{num}')
