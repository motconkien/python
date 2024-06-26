from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#create list
question_bank = []

for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_question = Question(question,answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_questions()

print("You're completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")