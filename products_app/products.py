from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def products():
    response = requests.get('https://dummyjson.com/products')
    data = response.json()['products']
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
