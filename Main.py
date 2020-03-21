from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


DATABASE = [
    ['BOB', 'BOB_IS_COOL', 'doctor'],
    ['JON SNOW', 'KNOWS NOTHING']
]


@app.route('/')
def main_page():
    return render_template('main_page2.html')


@app.route('/login_page', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for listy in DATABASE:
            if listy[0] == username:
                if listy[1] == password:
                    error = 'LOGGED IN!'
                else:
                    error = 'WRONG PASSWORD'
    return render_template('login_page.html', error=error)


@app.route('/staff_page', methods=['GET', 'POST'])
def staffPage():
    error = None
    if request.method == 'Post':
        print(6)
    return render_template('staff_page.html')


if __name__ == '__main__':
    app.run(debug=True)
