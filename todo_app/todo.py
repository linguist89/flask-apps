from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def todo_list():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = response.json()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run()
