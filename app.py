from flask import Flask, render_template,request,redirect,flash
from gPodder_funcs import basic_search, popularity_search, genre_search, user_suggestions, user_subscriptions, headers_generator

app= Flask(__name__)
app.secret_key = '89 ca 6b fe 9e a3 01 e4 bf 50'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/subscriptions',methods=['POST', 'GET'])
def subscriptions():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username == ''or password == '':
                flash("Not a valid login", category='message')
                return redirect('/subscriptions')
            subscriptions = user_subscriptions(username,password)
            return render_template('subscriptions.html', subscriptions=subscriptions)
        return render_template('subscriptions.html')
@app.route('/smart_sort')
def smart_sort():
    return render_template('smart_sort.html')

@app.route('/suggestions',methods=['POST', 'GET'])
def suggestions():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '' or password == '':
            flash("Not a valid login", category='message')
            return redirect('/suggestions')
        suggestions = user_suggestions(username, password)
        if suggestions == []:
            flash("No suggestions currently, subscribe to more podcasts and try again later", category='message')
            return redirect('/suggestions')
        return render_template('suggestions.html')
    return render_template('suggestions.html')
@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        searched_term = request.form['text']
        if searched_term:
            searched_term = basic_search(searched_term)
            return render_template('search.html', searched_term=searched_term)
        else:
            flash("Not a valid search", category='message')
    return render_template('search.html')

@app.route('/search_by_popularity', methods=['POST','GET'])
def search_by_popularity():
    if request.method == 'POST':
        topPodcast_Range = request.form['text']
        if topPodcast_Range:
            topPodcast_Range = int(topPodcast_Range)
            if topPodcast_Range < 1 or topPodcast_Range > 100:
                flash("Not a valid Range",category='message')
                return redirect('/search_by_popularity')
            topPodcast_Range = popularity_search(topPodcast_Range)
            return render_template('search_by_popularity.html', topPodcast_Range = topPodcast_Range)
        else:
            flash("Not a valid search", category='message')
    return render_template('search_by_popularity.html')

@app.route('/search_by_genre', methods=['POST', 'GET'])
def search_by_genre():
    if request.method == 'POST':
        searched_genre = request.form['text']
        if searched_genre:
            searched_genre = genre_search(searched_genre)
            return render_template('search_by_genre.html', searched_genre=searched_genre)
        else:
            flash("Not a valid search", category='message')
    return render_template('search_by_genre.html')



if __name__=="__main__":
    app.run()



