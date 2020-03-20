from blueprints import *
from model import Accuracy, Form


@app.route("/query/<language>")
def retcorpsize(language):
    """ Returns a JSON object containing a list of possible corpus sizes for the language specified in the route by querying the DB """
    corp = Accuracy.query.filter_by(language=language).all()
    return jsonify({'corpus': list(set([data.corpus for data in corp]))})


@app.route("/query/<language>/<corpus>")
def retalgo(language, corpus):
    """ Returns a JSON object containing a list of possible algorithms for the language,corpus specified in the route by querying the DB """
    res = Accuracy.query.filter_by(language=language, corpus=corpus).all()
    return jsonify({'algorithm': list(set([data.algorithm for data in res]))})


@app.route("/query/<language>/<corpus>/<algorithm>")
def retalfeat(language, corpus, algorithm):
    """ Returns a JSON object containing a list of possible features for the language,corpus,algorithm specified in the route by querying the DB """
    res = Accuracy.query.filter_by(language=language, corpus=corpus, algorithm=algorithm).all()
    return jsonify({'feature': list(set([data.feature for data in res]))})


@app.route("/query/<language>/<corpus>/<algorithm>/<feature>")
def retacc(language, corpus, algorithm, feature):
    """ Returns a JSON object containing the accuracy for the language,corpus,algorithm,feature specified in the route by querying the DB """
    res = Accuracy.query.filter_by(language=language, corpus=corpus, algorithm=algorithm, feature=feature).all()
    return jsonify({'accuracy': list(set([data.accuracy for data in res]))})
