from user_management import UserManager

# Initialize UserManager
manager = UserManager()

# Step 1: Get or create a user
username = input("Enter your username: ")
user = manager.get_or_create_user(username)

# Step 2: Display user history
print("\nDisplaying user history:")
manager.display_history(user)

# Step 3: Save a new test result
score = int(input("\nEnter a new test score: "))
manager.save_result(user, score)

# Step 4: Display updated history
print("\nUpdated user history:")
manager.display_history(user)
