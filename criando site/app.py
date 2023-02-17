from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def ex001():
    return render_template('001.html')

@app.route("/002")
def ex002():
    return render_template('002.html')
@app.route("/003")
def ex003():
    return render_template('003.html')
@app.route("/004")
def ex004():
    return render_template('004.html')
@app.route("/005")
def ex005():
    return render_template('005.html')

if __name__ == "__main__":
    app.run(debug=True)