class Word:
    def __init__(self, newword, q_word1, q_word2, answer):
        self.newword = newword
        self.q_word1 = q_word1
        self.q_word2 = q_word2
        self.answer = answer

    def show_question(self):
        print(f'"{self.newword}"의 뜻은?')
        print(f'1. {self.q_word1}')
        print(f'2. {self.q_word2}')

    def check_answer(self, user_input):
        if self.answer == user_input:
            print("정답입니다.")
        else:
            print("틀렸습니다.")


# word = Word("예빼시", "애교 빼면 시체", "애들은 빼빼로 시시해", 1)
word = Word("혼코노", "혼자서 코딩 노노", "혼자 코인 노래방", 2)

word.show_question()
word.check_answer(int(input('==> ')))