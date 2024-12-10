questions = [
    {
        "prompt": "What is the Capital of Greece?",
        "options": ["A. Belgrade", "B. Sofia", "C. Madrid", "D. Athens"],
        "answer": "D"
    },
    {
        "prompt": "What is the colour of water?",
        "options": ["A. blue", "B. white", "C. colourless", "D. light blue"],
        "answer": "C"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 5", "B. 2", "C. 9", "D. 7"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Place your answer (A, B, C or D): ").strip().upper()
        if answer == question["answer"]:  # Διορθώθηκε εδώ
            print("You are right!")
            score += 1
        else:
            print("Wrong! The correct answer is", question["answer"], "!!")
    print("You got", score, "out of", len(questions), "correct answers!")

run_quiz(questions)
