import json

# Define quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the 'language of AI'?",
        "options": ["A) Python", "B) Java", "C) C++", "D) JavaScript"],
        "answer": "A"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0

    for q in quiz_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

    print(f"\n🎉 Quiz completed! Your final score: {score}/{len(quiz_questions)}")

if __name__ == "__main__":
    run_quiz()
