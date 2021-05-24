class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_numbers(self):
        return len(self.question_list)-self.question_number
    
    def next(self):
        ques = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number+1}:{ques.question} (True/False)?: ")
        self.question_number +=1
        self.check_answer(ans,ques.correct_answer)
        
    
    def check_answer(self,U_ans,C_ans):
        if U_ans.lower() in C_ans.lower():
            print("You Got it Right")
            self.score +=1
        else:
            print("You Got it Wrong")
            self.question_number = len(self.question_list)
        print(f"The correct ans was {C_ans}")    
        print(f"Your current score was {self.score}/{self.question_number}")






