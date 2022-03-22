#Adam Grinde
#TEINF-20
#16/03-2022
#Quizmaker

#Classes

#class Question:
   # def __init__(self, question, answer, alternatives) -> None:
      #  self.question = question
        #self.alternatives = alternatives
       # self.answer = correct_answer

#class Quiz:
   # def __init__(questions, alternatives) -> None:
      #  self.questions = questions
      #  self.alternatives = alternatives

# functions
#def save_question(question : list()):
   # save_list = []
   # for question in question:
    #    question, alternatives, answer = question.get_attributes()
    #    save_string = f"{question}/{alternatives}/{answer}\n"
    #    save_list.append(save_string)
        
   # with open("saved_questions.txt", "w", encoding="utf8") as f:
   #     for line in save_list:
   #         f.write(line)
   #     print("Questions has been saved!")

#def load_q
# uestions():
  #  Questions = []
  #  with open("saved_questions.txt", "r", encoding="utf8") as f:
   #     for line in f.readlines():
     #       attributes = line.split("/")
    #        question = question
    #        questions.append(question)
   # return Questions   



from saved_questions import question_data

#Classes

class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list [self.question_number]
        self.question_number +=1
        player_answer = input(f"{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

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

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.remaining_questions():
    quiz.next.question()

print("Game Over. Well played!")
print("Your final score was: {quiz.score}/{quiz.question_number}")


    






