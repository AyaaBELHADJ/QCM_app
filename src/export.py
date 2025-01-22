import csv

def export_results(category, questions, user_answers, correct_answers, score, total_questions):
    """
    Exports quiz results to both a text file and a CSV file.

    Args:
        category (str): The category of the quiz.
        questions (list): List of question texts.
        user_answers (list): List of user-provided answers.
        correct_answers (list): List of correct answers.
        score (int): User's final score.
        total_questions (int): Total number of questions in the quiz.
    """
    # File names
    txt_filename = "quiz_results.txt"
    csv_filename = "quiz_results.csv"

    # Export to .txt
    with open(txt_filename, "w") as txt_file:
        txt_file.write(f"Quiz Results - {category}\n")
        txt_file.write("=" * 40 + "\n")
        txt_file.write(f"Total Questions: {total_questions}\n")
        txt_file.write(f"Final Score: {score}/{total_questions}\n\n")
        txt_file.write("Questions and Answers:\n")
        for i, question in enumerate(questions):
            txt_file.write(f"{i + 1}. {question}\n")
            txt_file.write(f"   Your Answer: {user_answers[i]}\n")
            txt_file.write(f"   Correct Answer: {correct_answers[i]}\n")
            txt_file.write(f"   Result: {'Correct' if user_answers[i] == correct_answers[i] else 'Incorrect'}\n\n")
        txt_file.write("=" * 40 + "\n")
        txt_file.write("End of Quiz\n")

    # Export to .csv
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Question #", "Question", "Your Answer", "Correct Answer", "Result"])
        for i, question in enumerate(questions):
            result = "Correct" if user_answers[i] == correct_answers[i] else "Incorrect"
            csv_writer.writerow([i + 1, question, user_answers[i], correct_answers[i], result])
        csv_writer.writerow([])  # Blank row for separation
        csv_writer.writerow(["Total Questions", total_questions])
        csv_writer.writerow(["Final Score", f"{score}/{total_questions}"])

    print(f"Results exported to {txt_filename} and {csv_filename}")