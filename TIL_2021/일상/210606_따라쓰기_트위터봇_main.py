import sys
import time
import twitter_bot_news as tb

print("Process Start")
start_time = time.time()
_id = sys.argv[1]
_ps = sys.argv[2]
keyword = sys.argv[3].strip()

BOT = tb.NewsBot()
BOT.login(_id, _ps)
hashtag = "#뉴스 #자동화 #코드"

BOT.tweet_all_news(keyword, hashtag)
time.sleep(10)
BOT.kill()
print("Process Done")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + "Second")

