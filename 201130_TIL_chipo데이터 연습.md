# 201130_TIL_chipo데이터 연습
```python
# 데이터 타입 변경
df['x'] = df['x'].astype(str)

# groupby 활용
df_x = df.groupby('item_name')['order_id'].count()
df_y = df.groupby('item_name')['quanty'].sum()

# apply함수 사용하기
# $1.23이 포함된 칼럼의 값을 숫자로 변환하기
chipo['item_price'] = chipo['item_price'].apply(lamda x: float(x[1:]))
```

#코딩/TIL