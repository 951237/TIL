# 숫자 글자 붙이기
def add_cm(height):
    return str(height) + "cm"
df['키'] = df['키'].apply(add_cm)

# 영어 첫글자 대문자로 바꾸기
def capitalize(lang):
    if pd.notnull(lang):  # nan값이 아닌경우에
        return lang.capitalize()
    return lang

df['SW특기'] = df['SW특기'].apply(capitalize)
