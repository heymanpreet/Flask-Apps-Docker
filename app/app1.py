from cassandra.cluster import Cluster
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import socket

cors = CORS()
app=Flask(__name__);
cors.init_app(app);

@app.route("/movies",methods=['GET'])
def getMovies():
    cluster = Cluster(["cassandra-docker-1"])
    session = cluster.connect()
    session.execute('USE netflix')
    moviesList = [];
    if request.method == 'GET':
        url = request.args.get('url');
        rows = session.execute('SELECT * FROM reference_list')
        for row in rows:
            moviesList.append({
                'uuid':row.uuid,
                'genre':row.genre,
                'title':row.title,
                'thumbnail':row.thumbnail,
                'year':row.year
            });

        print("Container Id",socket.gethostname())
        # print(moviesList);
        return jsonify(moviesList);
    else:
        return jsonify({'Error': "This is a GET API method"})

    cluster.shutdown()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cluster = Cluster(port=9842)
    # session = cluster.connect()
    # session.execute('USE netflix')
    # rows = session.execute('SELECT * FROM reference_list')
    # for row in rows:
    #     print({row.genre, row.title, row.year})
    app.run(debug=True,host='0.0.0.0', port=5000)
    # getMovies();
    # print_hi('PyCharm')

