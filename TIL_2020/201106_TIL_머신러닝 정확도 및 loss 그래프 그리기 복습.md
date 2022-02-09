# 201106_TIL_머신러닝 정확도 및 loss 그래프 그리기 복습
```python
print(result.history.keys())

import matplotlib.pyplot as plt

# 정확도 요약
plt.plot(result.history["accuracy"] # history key 값
plt.plot(result.history["val_accuracy"] # history key 값
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.regend(['train', 'test'], loc = 'upper_left')
plt.show()

# 로스 요약
plt.plot(result.history['loss']
plt.plot(result.history['val_loss']
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.regend(['train','test'], loc='upper left')
plt.show()
```

#snippet/python #코딩/TIL/복습