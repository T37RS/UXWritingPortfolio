import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Initialize an empty DataFrame for expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Function to add an expense
def add_expense(date, category, amount):
    global expenses
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)

# Function to get a summary of expenses
def expense_summary():
    summary = expenses.groupby('Category').sum()
    return summary

@app.route('/')
def home():
    summary = expense_summary().to_html(classes='table table-blue')
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e0f7fa;
            color: #004d40;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #add8e6;
            color: white;
            padding: 20px;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        h1 {
            margin: 0;
        }

        section {
            padding: 20px;
            animation: slideIn 1s ease-in-out;
        }

        @keyframes slideIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        form {
            background-color: #add8e6;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            margin: auto;
            transition: transform 0.3s ease-in-out;
        }

        form:hover {
            transform: scale(1.05);
        }

        form label {
            display: block;
            margin-bottom: 8px;
        }

        form input {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #b0bec5;
            border-radius: 5px;
            box-sizing: border-box;
        }

        form button {
            background-color: #grey;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }

        form button:hover {
            background-color: #00001b;
        }

        h2 {
            text-align: center;
            color: ##00796b;
            margin-top: 40px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            animation: fadeInTable 1.5s ease-in-out;
            background-color: #00008b;
        }

        @keyframes fadeInTable {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        table, th, td {
            border: 1px solid #b0bec5;
        }

        th, td {
            padding: 12px;
            text-align: left;
            color: white; /* Make text white */
        }

        th {
            background-color: #00008b;
            color: white;
        }

        td {
            animation: slideInTable 1s ease-in-out;
        }

        @keyframes slideInTable {
            from { transform: translateY(10px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .table-container {
            max-width: 800px;
            margin: auto;
            animation: fadeInTable 1.5s ease-in-out;
        }

        .table-blue th {
            background-color: #add8e6;
        }

        .table-blue td {
            background-color: #add8e6;
        }
    </style>
    <title>Budget Application</title>
</head>
<body>
    <header>
        <h1>Budget Application</h1>
    </header>
    <section>
        <form action="/add_expense" method="post">
            <label for="date">Date:</label>
            <input type="date" id="date" name="date" required><br>
            <label for="category">Category:</label>
            <input type="text" id="category" name="category" required><br>
            <label for="amount">Amount:</label>
            <input type="number" id="amount" name="amount" required><br>
            <button type="submit">Add Expense</button>
        </form>
        <h2>Expenses Summary</h2>
        <div class="table-container">{{ summary | safe }}</div>
    </section>
</body>
</html>
''', summary=summary)

@app.route('/add_expense', methods=['POST'])
def add_expense_route():
    date = request.form['date']
    category = request.form['category']
    amount = request.form['amount']
    add_expense(date, category, float(amount))
    return home()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
