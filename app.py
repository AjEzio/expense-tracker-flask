from flask import Flask, render_template, request, redirect, url_for    # import Flask
import new_func

app = Flask(__name__)       # create the app

@app.route('/')             # when someone visits /
def home():
    return render_template('home.html') # send this back

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
            new_func.add_entry(ex)

        else:
            error = 'Add all fields'


    return render_template('add.html', error=error, added = added)

@app.route('/view')
def view():
    ex = []
    ex = new_func.view_entry()
    return render_template('view.html', ex_entry = ex)

@app.route('/total')
def total():
    total = new_func.total_expense()
    return render_template('total.html', total = total)


app.run(debug=True)         # start the server