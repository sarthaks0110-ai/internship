class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("\n🎯 Welcome to the Quiz Platform!\n")
        name = input("Enter your name: ")
        print(f"\nHello, {name}! Let's start the quiz.\n")

        for i, q in enumerate(self.questions):
            print(f"\nQ{i+1}: {q['question']}")
            for idx, option in enumerate(q['options']):
                print(f"  {idx + 1}. {option}")

            try:
                answer = int(input("Your answer (1-4): "))
                if q['options'][answer - 1] == q['answer']:
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Wrong! Correct answer: {q['answer']}")
            except:
                print("⚠️ Invalid input. Skipping question.")

        self.show_result(name)

    def show_result(self, name):
        total = len(self.questions)
        percentage = (self.score / total) * 100

        print("\n📊 Quiz Completed!")
        
        # ✅ Added name in result
        print(f"\n👤 Player Name: {name}")
        print(f"🏆 Score: {self.score}/{total}")
        print(f"📈 Percentage: {percentage:.2f}%")

        if percentage >= 80:
            print(f"🔥 Excellent work, {name}!")
        elif percentage >= 50:
            print(f"👍 Good job, {name}!")
        else:
            print(f"📘 Keep practicing, {name}!")


def load_questions():
    return [
        {"question": "What is the capital of France?",
         "options": ["Berlin", "Madrid", "Paris", "Rome"],
         "answer": "Paris"},

        {"question": "Which language is used for web development?",
         "options": ["Python", "JavaScript", "C++", "Java"],
         "answer": "JavaScript"},

        {"question": "What does CPU stand for?",
         "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Power Unit"],
         "answer": "Central Processing Unit"},

        {"question": "What is 8 × 7?",
         "options": ["54", "56", "58", "60"],
         "answer": "56"},

        {"question": "Which data structure uses FIFO?",
         "options": ["Queue", "Stack", "Tree", "Graph"],
         "answer": "Queue"},

        {"question": "Who is the father of computers?",
         "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
         "answer": "Charles Babbage"},

        {"question": "Which keyword defines a function in Python?",
         "options": ["func", "define", "def", "function"],
         "answer": "def"},

        {"question": "What is the output of 3 + 2 * 2?",
         "options": ["10", "8", "7", "12"],
         "answer": "7"},

        {"question": "Which planet is known as the Red Planet?",
         "options": ["Earth", "Saturn", "Jupiter", "Mars"],
         "answer": "Mars"},

        {"question": "What is the largest ocean on Earth?",
         "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
         "answer": "Pacific"}
    ]


def main():
    while True:
        questions = load_questions()
        quiz = Quiz(questions)
        quiz.start()

        again = input("\nDo you want to try again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thank you for using the Quiz Platform!")
            break


if __name__ == "__main__":
    main()