from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    # return "hello world   drr"
    return render_template('home.html')

@app.route('/about')
def about():
    return 'About'


def information():
    print("hello")

if __name__ == '__main__':
    app.run(debug=True)