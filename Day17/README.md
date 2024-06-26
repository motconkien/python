How to create a Class in Python
Working with Attributes, Class Constructors and the init() Function
Adding Methods to a Class

Problem breakdown:
1. Create the class question on question_model file:
+ Attributes: text, answer

2. Create quiz_brain file:
+ Asking the questions
+ Cheking if the answer was correct
+ cheking if we're the end of the quiz
+ Attributes: question_number, questions_list, score
+ Methods: next_question() which retrieve the item ad use input() to show the user question text and ask for the user's answer
+ Methods: still_has_question() returns boolean value depending on the value of question_number
+ Methods: check_answer()
