from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#  convert list of dicts to list of questions objects
question_bank = []
for q in question_data:
    question_bank.append( Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("End of quiz")
print(f"Final score is {quiz.score}/{len(quiz.question_list)}")