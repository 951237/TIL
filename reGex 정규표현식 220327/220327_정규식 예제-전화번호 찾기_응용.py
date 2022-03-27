import re
text = "문의 사항이 잇으시면 032-232-3245으로 연락을 주시기 바랍니다."

regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})') # ?P<str> 로 그룹에 이름을 짓기

matchobj = regex.search(text)
area_code = matchobj.group("area")
num = matchobj.group("num")
print(area_code, num)