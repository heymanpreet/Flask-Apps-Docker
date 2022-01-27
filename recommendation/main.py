import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
# libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# define a function that creates similarity matrix
# if it doesn't exist
recommendedMoviesObj = [];
def create_sim():
    data = pd.read_csv('data.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    sim = cosine_similarity(count_matrix)
    return data,sim


# defining a function that recommends 10 most similar movies
def rcmd(m):
    m = m.lower()
    # check if data and sim are already assigned
    data, sim = create_sim()
    # check if the movie is in our database or not
    print("Movie",m)
    if m not in data['movie_title'].unique():
        return('This movie is not in our database.\nPlease check if you spelled it correct.')
    else:
        # getting the index of the movie in the dataframe
        print(data.columns)
        i = data.loc[data['movie_title']==m].index[0]
        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        selectedMovieObj = {'title': data['movie_title'][lst[0][0]], 'imdb_url': data['movie_imdb_link'][lst[0][0]],'video':data['movie_video'][lst[0][0]]}
        lst = lst[1:11]
        print("r movie title", lst);

        # making an empty list that will containing all 10 movie recommendations
        l = []

        recommendedMoviesObj = [];
        recommendedMoviesObj.append(selectedMovieObj)
        print("reccccc",recommendedMoviesObj)
        for i in range(len(lst)):
            a = lst[i][0]
            obj = {'title': data['movie_title'][a], 'imdb_url':data['movie_imdb_link'][a], 'video':data['movie_video'][a]};
            recommendedMoviesObj.append(obj);
            l.append(data['movie_title'][a])
        print(recommendedMoviesObj)
        return recommendedMoviesObj;
        # return l


app = Flask(__name__)
CORS(app)

@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/recommend", methods=["GET"])
#@cross_origin(origin='*')
def recommend():
    movie = request.args.get('movie')
    r = rcmd(movie)
    movie = movie.upper()

    return jsonify(r);

if __name__ == '__main__':
    app.run()
