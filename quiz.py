#Adam Grinde
#TEINF-20
#16/03-2022
#Quizmaker

#This python file is made only for the Quiz class

class Quiz:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list [self.question_number]
        self.question_number +=1
        player_answer = input(f"{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(player_answer, current_question.answer)

    def remaining_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, player_answer, answer):
        if player_answer.lower() == answer.lower():
            self.score +=1
            print("Good job, the answer is correct!")
        else:
            print("Too bad, your answer is wrong.")
        print(f"The answer is: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")