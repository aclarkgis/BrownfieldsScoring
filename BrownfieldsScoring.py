def get_scores(num_questions):
    scores = []
    
    for i in range(num_questions):
        while True:
            try:
                score = int(input(f"Enter score for question {i + 1} (1-10): "))
                if 1 <= score <= 10:
                    scores.append(score)
                    break
                else:
                    print("Please enter a score between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return scores

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def main():
    num_questions = int(input("Enter the number of questions: "))
    scores = get_scores(num_questions)
    average_score = calculate_average(scores)

    print(f"The average score is: {average_score:.2f}")

if __name__ == "__main__":
    main()