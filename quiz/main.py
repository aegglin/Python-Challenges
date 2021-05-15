from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q_entry['text'], q_entry['answer']) for q_entry in question_data]
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print('You\'ve completed the quiz!')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')
