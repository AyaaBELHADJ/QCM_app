# QCM Application

Welcome to the **QCM Application** repository! This project is a Python-based interactive quiz application that supports multi-language functionality, user management, and dynamic question categorization. The application is designed to be engaging, user-friendly, and customizable.

---

## Features

1. **Language Support**
   - Choose between English and French at the start of the quiz.

2. **Dynamic Quiz Generation**
   - Questions are stored in a JSON file and loaded dynamically.
   - Users can select a category (e.g., Python, Networking, Algorithms) before starting the quiz.

3. **User Management**
   - Create and manage user profiles.
   - View quiz history, including scores and test dates.

4. **Settings Customization**
   - Enable or disable penalty scoring.
   - Adjust the timer duration to suit your preferences.

5. **Real-Time Interaction**
   - Interactive console interface with colorful text and user prompts.
   - Feedback provided for every question.

6. **Result Export**
   - Export quiz results to `.txt` and `.csv` files for detailed review.

---

## Installation

### Prerequisites
Ensure you have Python installed on your system (version 3.6 or higher).

### Required Libraries
Install the required Python libraries using the following command:

```bash
pip install ascii-magic rich questionary colorama pyfiglet alive-progress
```

---

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/AyaaBELHADJ/QCM_app.git
   cd QCM_app
   ```

2. Navigate to the `src` directory:
   ```bash
   cd src
   ```

3. Run the main Python file:
   ```bash
   python main.py
   ```

4. Follow the prompts in the console to:
   - Select your language.
   - Enter your username.
   - Choose an action (e.g., start a quiz, view history, edit settings).

---

## File Structure

```
QCM_app/
├── src/
│   ├── main.py                # Entry point of the application
│   ├── export.py              # Handles exporting results
│   ├── question_manager.py    # Manages quiz questions and categories
│   ├── timer.py               # Implements the quiz timer functionality
│   ├── user_management.py     # Manages user profiles and history
│   ├── python.json            # Contains quiz questions and categories
│   ├── translations.json      # Stores translations for multi-language support
│   └── users.json             # Stores user profiles and histories
└── README.md                  # This file
```

---

## Usage Guide

### Starting a Quiz
- Select a category from the available options.
- Answer the questions within the allotted time.
- Receive feedback on your answers.

### Viewing History
- Check your past quiz results, including scores and dates.

### Editing Settings
- Enable or disable penalty scoring.
- Adjust the timer duration as needed.

### Exporting Results
- Quiz results are automatically saved in `.txt` and `.csv` formats.

---

## Future Enhancements

- Add more question categories.
- Improve user interface for better accessibility.
- Implement a graphical user interface (GUI).
- Add support for more languages.



##Repport
[Rapport (5).pdf](https://github.com/user-attachments/files/18512738/Rapport.5.pdf)
