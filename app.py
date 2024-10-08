from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000/api/movies'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        requests.post(
            API_URL, JSON={'title':title, 'genre' :genre} 
        )
        return redirect('/')
    else:
        response= requests.get(API_URL) 
        if response.status_code == 200:
            movies = response.json()
        else:
            movies = []
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(port=5001, debug=True)