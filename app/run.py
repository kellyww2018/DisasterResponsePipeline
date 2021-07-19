import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
import plotly.graph_objs as pgo
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('DisasterResponse', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    # create visuals
    graph_one= []
    graph_one.append(
        pgo.Bar(x=genre_names,
               y=genre_counts))
    layout_one=dict(title= 'Distribution of Message Genres',
                yaxis=dict(title= "Count"),
                xaxis=dict(title="Genre"))
    msg_category=df.iloc[:,4:].columns.tolist()
    msg_counts=df.iloc[:,4:].sum().tolist()
    msg_dict=dict(zip(msg_category,msg_counts))
    msg_dict_sorted=sorted(msg_dict.items(),key=lambda x:x[1],reverse=True)
    msg_category_sorted=[]
    msg_counts_sorted=[]
    for i in msg_dict_sorted:
        msg_category_sorted.append(i[0])
        msg_counts_sorted.append(i[1])
    graph_two= []
    graph_two.append(
        pgo.Bar(x=msg_category_sorted[:10],
               y=msg_counts_sorted[:10]))
    layout_two=dict(title='Top 10 Message Categories',
                yaxis=dict(title= "Count"),
                xaxis=dict(title="Category"))
    graph_three= []
    graph_three.append(
        pgo.Bar(x=msg_category_sorted[-10:],
               y=msg_counts_sorted[-10:]))
    layout_three=dict(title='Last 10 Message Categories',
                yaxis=dict(title= "Count"),
                xaxis=dict(title="Category")) 
    graphs=[]
    graphs.append(dict(data=graph_one, layout=layout_one))
    graphs.append(dict(data=graph_two, layout=layout_two))
    graphs.append(dict(data=graph_three, layout=layout_three))
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
