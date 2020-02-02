#리스트 colors
colors = ['1','2','3','4','5','6']

#2개씩 나눠서 출력
div = '2'
#colors를 colors_copy로 복사
colors_copy = colors
#임시 리스트 - templist 선언
templist = []
#반복문 color in colors:
for color in colors:
    #만약 colors의 갯수가 분할의 수보다 작으면
    if colors.__len__() < div:
        #사본 컬러 출력
        print(colors_copy)
        #나가rl
        break

    #임시리스트에 컬러 추가
    templist.append(color)

    #colors_copy에서 color삭제
    colors_copy.remove(color)

    #만약 임시리스트의 갯수가 분할수와 같으면
    if templist.__len__() == div:
        #임시리스트 출력
        print(templist)

        #임시리스트 초기화
        templist = []

    #만약 color_copy의 수가 분할 수보다 작거나 같으면
    if colors_copy.__len__() <= div:
        #만약 color_copy가 비어 있지 않다면
        if colors_copy != []:
            #color_copy 출력
            print(colors_copy)
        #나가기
        break

    #아니면:
    else:
        continue
    #계속하기
