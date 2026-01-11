# 💸 Expense Tracker (Console Application)

A simple and clean **console-based expense tracker** built with **Python**, designed to help users record, manage, and analyze their personal expenses.

This project focuses on **clean logic, input validation, and data persistence**, without using external libraries or frameworks.

---

## ✨ Features

- Add new expenses with:
  - Amount
  - Category
  - Date
  - Description
- Predefined expense categories
- View all recorded expenses
- Expense summary by category
- Delete expenses safely using index selection
- Persistent storage using JSON (save & load)
- Strong input validation to prevent crashes

---

## 🧱 Technologies Used

- Python 3
- Standard Library (`json`, `datetime`, `time`)

---

## 📂 Project Structure

expense-tracker/
│
├── main.py # Main application logic
├── expenses_data.json # Stored expense data (auto-created)
└── README.md

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed
2. Clone the repository
3. Run the application:

```bash
python main.py

🧠 Design Decisions
-Expenses are stored as dictionaries inside a list
-Dates are validated using datetime but stored as strings for JSON compatibility
-Deleting expenses is done using list indexing for clarity and safety
-No external libraries are used to keep the project lightweight and educational

🚀 Future Improvements
-Monthly / yearly summaries
-Filtering expenses by date or category
-Export data to CSV
-Web version using Flask

📌 Notes
This project was built as a learning exercise to practice:
    1.Python fundamentals
    2.Data structures
    3.Input validation
    4.File handling
    5.Writing clean and readable code

👤 Author
Kostas Kanellopoulos