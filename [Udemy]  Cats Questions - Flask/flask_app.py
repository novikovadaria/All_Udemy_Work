# ----------------Creating First Flask Application-------------

# 1 - Jinja
# 2 - Werkzeug


from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db
app = Flask(__name__)

# ----------------------MTV--------------------
m = 'Transmitting from the view function'


@app.route('/')
def welcome():
    return render_template('home.html', questions=db)

# ------------------Flow Control----------------------


@app.route('/cool')
def cool():
    return 'Flask is AWESOME!!!'


# --------------------------Debugging----------------------
counter = 0


@app.route('/count')
def view_counter():
    global counter
    counter += 1
    return f'this page has been viewed {counter} time(s)'


# ----------------------Maps URLs-------------------------------
# ----------json----------
@app.route('/quiz/<int:index>')
def questins_view(index):
    try:
        questions_db = db[index]
        return render_template('quiz.html', question=questions_db, index=index, max_index=len(db)-1)
    except IndexError:
        abort(404)

# ---------------------Adding a question----------------------


@app.route('/add_new_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question_dict = {
            "question": request.form['question'],
            "answer": request.form['answer']
        }
        db.append(question_dict)
        save_db()
        return redirect(url_for('questins_view', index=len(db)-1))
    else:
        return render_template('add.html')


# --------------------Creating a rest API for our Full-Stack Multi-Page App-----------------


@app.route('/api/question/')
def api_question_list():
    return jsonify(db)


@app.route('/api/question/<int:index>')
def api_question_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

# -----------------Deleting a question------------------------


@app.route('/remove_a_question/<int:index>', methods=['GET', 'POST'])
def deleting(index):
    try:
        if request.method == 'POST':
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template('remove.html', question=db[index])
    except IndexError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
