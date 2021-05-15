class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        curr_q = self.questions_list[self.question_number]
        self.question_number += 1
        user_response = input(f'{self.question_number}: {curr_q.text} (True/False)? ')
        self.check_answer(user_response, curr_q.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_response, answer):
        if user_response.lower().strip() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f'The correct answer was: {answer}.')
        print(f'Your score is: {self.score}/{self.question_number}.')
        print('\n')
