from flask import Flask, render_template, request, redirect, url_for    
import new_func
import sqlite3

app = Flask(__name__)       

def add_dbentry(ex):
    with sqlite3.connect("app.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS expenses (date TEXT NOT NULL,amount REAL NOT NULL, category TEXT DEFAULT Others, note TEXT DEFAULT Nil)")
        cursor.execute("INSERT INTO expenses VALUES(:date, :amount, :category, :note)",ex)
        db.commit()

def view_dbentry():
    ex = []
    with sqlite3.connect("app.db") as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS expenses (date TEXT NOT NULL,amount REAL NOT NULL, category TEXT DEFAULT Others, note TEXT DEFAULT Nil)")
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        for row in rows:
          ex.append(row)
    return ex

def total_db():
    total = 0
    with sqlite3.connect("app.db") as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS expenses (date TEXT NOT NULL,amount REAL NOT NULL, category TEXT DEFAULT Others, note TEXT DEFAULT Nil)")
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        for row in rows:
          total = total + row["amount"]
    return total

@app.route('/')             
def home():
    return render_template('home.html') 

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    error = None
    added = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'home':
            return redirect(url_for('home'))
        ex = {}
        ex["date"] = request.form.get('date')
        ex["amount"] = request.form.get('amount')
        ex["category"] = request.form.get('category')
        ex["note"] = request.form.get('note')
        if ex['date'] and ex['amount'] and ex['category'] and ex['note']:
            added = "Expense Added"
            add_dbentry(ex)
          #  new_func.add_entry(ex)

        else:
            error = 'Add all fields'


    return render_template('add.html', error=error, added = added)

@app.route('/view')
def view():
    #ex = new_func.view_entry()
    ex_db = view_dbentry()
    return render_template('view.html', ex_entry = ex_db)

@app.route('/total')
def total():
    total = 0
    total = total_db()
   # total = new_func.total_expense()
    return render_template('total.html', total = total)


app.run(debug=True)         