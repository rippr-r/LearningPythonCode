## Guided by https://www.youtube.com/watch?v=4TZ1K8EHT2M

questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "prompt": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["prompt"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    print(f"You got {score} out of {len(questions)} correct.")
    grade = score / len(questions) * 100
    print(f"Your grade: {grade}%")

run_quiz(questions)
