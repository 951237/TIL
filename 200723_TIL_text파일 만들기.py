names = ["아이언맨tv", "토르코딩", "헐크에러"]

for name in names:
    with open("{}.txt".format(name), "w") as email_file:
        contents = (
            f"{name}안녕"
        )
        email_file.write(contents)
