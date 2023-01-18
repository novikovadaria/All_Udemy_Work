# ----------------Creating First Flask Application-------------

# 1 - Jinja
# 2 - Werkzeug


from flask import Flask, render_template
from model import db
app = Flask(__name__)

# ----------------------MTV--------------------
m = 'Transmitting from the view function'


@app.route('/')
def welome():
    return render_template('home.html', message=m, first_name='Dasha', last_name='Novikova')

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
    questions_db = db[index]
    return render_template('quiz.html', question=questions_db)


if __name__ == "__main__":
    app.run(debug=True)
