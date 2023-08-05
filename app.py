from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def landing():
    return render_template('landing.html')


if __name__ == '__main__':
    app.run(debug=True)