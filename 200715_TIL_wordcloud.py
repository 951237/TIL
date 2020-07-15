# 라이브러리 호출
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 워드클라우드 소스
text = "coffee phone phone phone phone phone phone phone phone phone cat dog dog"


# 워드클라우드 이미지 마스크
# mask_something = np.array(Image.open("cat.png"))

# 폰트 경로
PATH_FONT = "/Users/mac/Documents/coding_TIL/font/NanumBarunGothic.otf"


wordcloud = WordCloud(font_path=PATH_FONT, background_color="white", max_font_size=100).generate(text)
# wordcloud = WordCloud(font_path=PATH_FONT, background_color="white", max_font_size=100, mask=mask_something) # 이미지에 워드클라우드 구현할때

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('wordcloud.png')

