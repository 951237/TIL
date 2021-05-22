import sys
import time
import twitter_bot_tweet as tb

# 작업시작 메세지
print("Prodess Start.")

# 시작시간 기록하기
start_time = time.time()

# 아이디 입력 받기
id = sys.argv[1]

# 패스워드 입력 받기
ps = sys.argv[2]

# 트윗할 내용이 적힌 파일 입력받기
filename = sys.argv[3]

# 크롤러 불러오기
BOT = tb.TwitterBot(filename)

# 로그인 시도하기
BOT.login(id, ps)

# 로그인후 스크린샷 찍기
BOT.save_screenshot(str(time.time) + ".png")

# 트위터에 모든 멘션 올리기
BOT.tweet_all()

# 결과화면 올리기 위해 10초동안 방치하기
time.sleep(10)

# 크롤러 닫기
BOT.kill()

# 작업종료 메세지 출력
print("Process Done.")

# 작업시간 출력
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
