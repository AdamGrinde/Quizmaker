#Adam Grinde
#TEINF-20
#16/03-2022
#Quizmaker

#This python file is made for the structure of the quiz

from saved_questions import question_data
from model import Question
from quiz import Quiz

#Classes

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.remaining_questions():
    quiz.next_question()

print("Game Over. Well played!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")


    






