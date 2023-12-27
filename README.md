# Employee Management System

Welcome to the Employee Management System project. This system allows users to register, list, edit, and delete employees.

## Environment Setup

Before running the application, make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

Open a terminal and navigate to the project directory.

```bash
pip install -r requirements.txt

This command installs the necessary dependencies for the project.

Database Setup
The application uses a SQLite database. To initialize the database, run the following commands:
python
from app import db
db.create_all()
exit()

Running the Application
Now that the environment is set up, you can run the application.
python app.py

Visit http://127.0.0.1:5000/ in your web browser to access the Employee Management System.

Usage
Registration
Click on "新入社員登録" in the home page to register a new employee. Enter the employee ID and name in the provided form.

Employee List
To view the list of registered employees, click on "従業員リストを見る" in the home page.

Editing
Click on "編集" next to an employee in the list to edit their details.

Deletion
Click on "削除" next to an employee in the list to delete them.

Issues and Support
If you encounter any issues or need assistance, please create an issue on the GitHub repository.
