import random

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.question} (True/False)? ").strip().capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}.\n")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

random.shuffle(question_bank)

quiz = QuizBrain(question_bank)

print("🎉 Welcome to the Quiz Game! 🎉\n")
while quiz.still_has_questions():
    quiz.next_question()

print(f"\n🎯 Quiz Complete! Your final score is: {quiz.score}/{len(question_bank)}")
