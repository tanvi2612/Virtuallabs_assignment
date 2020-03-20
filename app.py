from blueprints import *
from model import Accuracy, Form
from controllers import *


@app.route("/")
def mainpage():
    """Renders the mainpage(Introduction.html)"""
    return render_template("Introduction.html")


@app.route("/Introduction.html")
def page1():
    """Renders Introduction.html"""
    return render_template("Introduction.html")


@app.route("/Experiment.html")
def page2():
    """Renders experiment page and adds initial data by querying the database"""
    form = Form()
    form.language.choices = list(set([(data.language, data.language)
                             for data in Accuracy.query.all()]))
    form.corpus.choices = [(data.corpus, data.corpus)
                           for data in Accuracy.query.filter_by(language="English").all()]
    form.algorithm.choices = [(data.algorithm, data.algorithm) for data in Accuracy.query.filter_by(
        language="English", corpus=form.corpus.choices[0][1]).all()]
    form.feature.choices = [(data.feature, data.feature) for data in Accuracy.query.filter_by(
        language="English", corpus=form.corpus.choices[0][1], algorithm=form.algorithm.choices[0][1]).all()]

    return render_template("/Experiment.html", form=form)


@app.route("/Further Readings.html")
def page3():
    """Renders Further Readings page"""
    return render_template("/Further Readings.html")


@app.route("/Objective.html")
def page4():
    """ Renders objectives """
    return render_template("Objective.html")


@app.route("/Procedure.html")
def page5():
    """ Renders the procedure """
    return render_template("Procedure.html")


@app.route("/Theory.html")
def page6():
    """ Renders the theory page """
    return render_template("Theory.html")


@app.route("/Quizzes.html") 
def page7():
    """ Renders the quizzes page """
    return render_template("Quizzes.html")





if __name__ == "__main__":
    """ Runs the flask app on localhost:5000 """
    app.run(host="0.0.0.0", port="5000", debug=True)
