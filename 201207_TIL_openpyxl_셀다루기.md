# 201207_TIL_openpyxl_셀다루기
```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "NadoSheet"

# A1셀에 1 이라는 값을 입력
ws["A1"] = 1
ws.cell(row = 1, column = 1).value = 1

# A1셀의 값을 출력
print(ws["A1"].value)


# 반복문을 이용해서 랜덤 숫자 채우기
for x in range(1, 11):
	for y in range(1, 11):
		ws.cell(row = x, column = y, value = randint(0, 100) # 0 ~ 100사이의 숫자

```
#코딩/TIL #python/openpyxl
