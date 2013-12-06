from flask import Flask
a='a'
app = Flask(a)

@app.route('/xd')
def we():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
