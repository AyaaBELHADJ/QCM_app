import json
import os
from datetime import datetime


class UserManager:
    def __init__(self, data_file="users.json"):
        self.data_file = data_file
        self.users = self._load_users()

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
                print(f"{i}. Score: {record['score']}, Date: {record['date']}")

    def save_result(self, user, score):
        """
        Save the result of a test to the user's history.
        Args:
            user (dict): The user data.
            score (int): The test score.
        """
        result = {
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        user["history"].append(result)
        self._save_users()
