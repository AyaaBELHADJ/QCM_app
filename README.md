# Interactive Quiz Application
## Overview
This interactive quiz application allows users to take quizzes in multiple languages, customize settings, track their results, and export their performance. It features a dynamic quiz generation system, user management, customizable quiz settings, and robust error handling to ensure smooth user experience.<br>
## Features
Language Support: Choose between French and English at the start of the quiz.
Dynamic Quiz Generation: Quiz questions are loaded dynamically based on the selected category and stored in a JSON file.
User Management: Create profiles, track quiz history, and view past results.
Settings Customization: Adjust quiz settings such as penalty scoring and timer duration.
Results Export: Export quiz results to text and CSV files for detailed review.
<br>
## Libraries Used
questionary: For creating interactive prompts and question selection.
rich: To display colorful, user-friendly console output.
colorama: For terminal text styling (e.g., colors, bold text).
pyfiglet: For stylized text headers.
alive-progress: For progress bars during loading.
