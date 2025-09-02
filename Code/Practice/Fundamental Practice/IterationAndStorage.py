questions = ["What is your name?", "How old are you?", "What is your favorite color?"]

def ask_questions(questions):
    answers = []

    for question in questions:
        response = input(question + ":")
        answers.append(f"{question}: {response}")
    
    for idx, answer in enumerate(answers, 1): # Start enumeration from 1
        print(f"Answer {idx}: {answer}")

def main():
    ask_questions(questions)

main()
