from flask import Flask, render_template  
  
app = Flask(__name__)  
 
  
@app.route("/")  
def main_():  
    return render_template('main.html')

@app.route("/genre_selection")  
def genre_selection():  
    return render_template('genre_selection.html')  

@app.route("/wave")  
def wave():  
    return render_template('wave.html')

@app.route("/add_to_playlist")  
def add_to_playlist():  
    return render_template('add_to_playlist.html')

@app.route("/author")  
def author():  
    return render_template('author.html')

@app.route("/search")  
def search():  
    return render_template('search.html')

@app.route("/user_1")  
def user_1():  
    return render_template('user_1.html')

@app.route("/user_2")  
def user_2():  
    return render_template('user_2.html')

@app.route("/user_3")  
def user_3():  
    return render_template('user_3.html')

  
if __name__ == "__main__":  
    app.run()  