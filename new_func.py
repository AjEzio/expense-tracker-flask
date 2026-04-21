import csv
import os

expense_file = "expense.csv"

def add_entry(ex):
    file_exist = os.path.exists(expense_file)
    with open(expense_file,"a", newline ='') as file:
        writer = csv.DictWriter(file, fieldnames = ["date","amount","category", "note"])
        if not file_exist:
            writer.writeheader()
        writer.writerow(ex)

def view_entry():
    ex_entry =[]
    file_exist = os.path.exists(expense_file)
    if not file_exist:
        with open(expense_file,"a", newline ='') as file:
            writer = csv.DictWriter(file, fieldnames = ["date","amount","category", "note"])
    with open(expense_file,"r", newline ='') as file:
        reader = csv.DictReader(file, fieldnames =["date","amount","category", "note"])
        for row in reader:
            ex_entry.append(row)
    return ex_entry

def total_expense():
    total = 0.00
    file_exist = os.path.exists(expense_file)
    if file_exist:
        with open(expense_file,"r", newline ='') as file:
            reader = csv.DictReader(file, fieldnames =["date","amount","category", "note"])
            for row in reader:
                total = total + float(row["amount"])

    return total      
