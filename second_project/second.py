from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "hello world_ I have started with git."

if __name__=='__main__':
    app.run(debug=True)
