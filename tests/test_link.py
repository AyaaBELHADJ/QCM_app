import os 
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from user_managment import UserManager
from question_manager import QuestionManager

data_file = os.path.join(os.path.dirname(__file__), "../data/QCM_Reseaux.json")



# Initialize managers
question_manager = QuestionManager(data_file)
user_manager = UserManager(question_manager=question_manager)

# Conduct a quiz for a user
username = input("Enter your username: ")
category = input("Enter the category of the quiz: ")
if category == "reseau":
    data_file = os.path.join(os.path.dirname(__file__), "../data/QCM_Reseaux.json")
else:
    data_file = os.path.join(os.path.dirname(__file__), "../data/QCM_Python.json")

question_manager = QuestionManager(data_file)
user_manager = UserManager(question_manager=question_manager)

user_manager.conduct_quiz(username, category)






# # Initialize managers
# user_manager = UserManager()
# question_manager = QuestionManager(data_file, user_manager)

# # Set the user in the QuestionManager
# username = input("Enter your username: ")
# question_manager.set_user(username)

# # Conduct the quiz
# for question in question_manager.questions:
#     question_text = question_manager.get_question_text(question)
#     options = question_manager.get_options_text(question)

#     print(f"\n{question_text}")
#     for idx, option in enumerate(options, 1):
#         print(f"{idx}. {option}")

#     user_answer_idx = int(input("Enter the option number: ")) - 1
#     user_answer = options[user_answer_idx]
#     _, feedback = question_manager.check_answer(question, user_answer)
#     print(feedback)

# # Save the score
# question_manager.save_score()

# question_manager.display_score()
