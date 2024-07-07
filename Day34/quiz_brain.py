import html

class QuizBrain:
    def __init__(self,q_list) :
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.high_score = self.load_high_score()
    
    def load_high_score(self):
        try:
            with open("Day34/score.txt") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
    
    def save_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("Day34/score.txt", "w") as file:
                file.write(f"{self.high_score}")
                
    def get_high_score(self):
        return self.high_score

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number+=1
        q_text = html.unescape(self.current_question.text)
        return f"Q:{self.question_number}: {q_text}"

    def check_answer(self,user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            self.save_high_score()
            return True
        else:
            return False

  