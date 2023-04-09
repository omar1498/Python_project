from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=int("18333"), debug=True)
 