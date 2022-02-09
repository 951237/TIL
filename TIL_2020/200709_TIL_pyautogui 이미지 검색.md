# 200709_TIL_pyautogui 이미지 검색

```python

impourt pyautogui as pa

print(pa.position())		# 마우스 위치값 출력하기
pa.screenshot("1.png", region=(1324, 739, 30, 30))

num1 = pa.locateCenterOnScreen("1.png")		# 이미지파일의 센터값을 저장

pa.click(num1)	# 이미지파일의 센터값을 클릭


```