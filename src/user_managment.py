import json
import os
from datetime import datetime
from question_manager import QuestionManager

class UserManager:
    def __init__(self, data_file=None, question_manager=None):
        """
        Initialize the UserManager and optionally link a QuestionManager.
        Args:
        - data_file (str): Path to the JSON file with user data.
        - question_manager (QuestionManager): Optional QuestionManager instance.
        """
        self.data_file = data_file or os.path.join(os.path.dirname(__file__), "../data/users.json")
        self.question_manager = question_manager
        self.users = self._load_users()

    def set_question_manager(self, question_manager):
        """
        Link a QuestionManager to this UserManager.
        """
        self.question_manager = question_manager

    def conduct_quiz(self, username, category):
        """
        Conduct a quiz for a given user and save the category.
        Args:
        - username (str): Name of the user taking the quiz.
        - category (str): The category of the quiz (e.g., "python" or "reseaux").
        """
        user = self.get_or_create_user(username)
        if self.question_manager:
            self.question_manager.score = 0  # Reset score for the new quiz
            for question in self.question_manager.questions:
                question_text = self.question_manager.get_question_text(question)
                options = self.question_manager.get_options_text(question)

                print(f"\n{question_text}")
                for idx, option in enumerate(options, 1):
                    print(f"{idx}. {option}")

                user_answer_idx = int(input("Enter the option number: ")) - 1
                user_answer = options[user_answer_idx]
                _, feedback = self.question_manager.check_answer(question, user_answer)
                print(feedback)
            
            # Save the score and category to the user's history
            self.save_result(user, self.question_manager.score, category)
        else:
            print("No QuestionManager linked.")

    def _load_users(self):
        """
        Load user data from a JSON file or initialize an empty dictionary if the file doesn't exist.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        return {}

    def _save_users(self):
        """
        Save user data to the JSON file.
        """
        with open(self.data_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def user_exists(self, username):
        """
        Check if a user already exists.
        Args:
            username (str): The username to check.
        Returns:
            int: 1 if the user exists, 0 otherwise.
        """
        return 1 if username in self.users else 0

    def get_or_create_user(self, username):
        """
        Retrieve a user by username or create a new entry if the user doesn't exist.
        Args:
            username (str): The username to search for.
        Returns:
            dict: The user data.
        """
        if username not in self.users:
            self.users[username] = {"history": []}
            self._save_users()
        return self.users[username]

    def display_history(self, user):
        """
        Display the user's history of test results.
        Args:
            user (dict): The user data.
        """
        history = user.get("history", [])
        if not history:
            print("No history available.")
        else:
            print("Test History:")
            for i, record in enumerate(history, 1):
                print(f"{i}. Score: {record['score']}, Date: {record['date']}, Category: {record['category']}")

    def save_result(self, user, score, category):
        """
        Save the result of a test to the user's history.
        Args:
            user (dict): The user data.
            score (int): The test score.
            category (str): The category of the test (e.g., "python" or "reseaux").
        """
        result = {
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category
        }
        user["history"].append(result)
        self._save_users()
