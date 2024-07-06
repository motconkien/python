from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for item in question_data:
    q_text = item["question"]
    q_answer = item["correct_answer"]
    question = Question(q_text,q_answer)
    question_bank.append(question)

# for question in question_bank:
#     print(question.text)    

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)
# while quiz.still_has_question():
#     quiz.next_question()
