from blueprints import *

class Accuracy(db.Model):
    """

    This is a class for the database containing accuracies
    Attributes:
        id: The database id of the record
        language: The language used
        corpus: The size of the corpus used
        algorithm: The type of algorithm used
        feature: The feature that is being considered such as bigram, trigram etc.
        accuracy: The accuracy thus obtained

    """

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(80), unique=False)
    corpus = db.Column(db.String(80), unique=False)
    algorithm = db.Column(db.String(80), unique=False)
    feature = db.Column(db.String(80), unique=False)
    accuracy = db.Column(db.String(80), unique=False)

    def __init__(self, language, corpus, algorithm, feature, accuracy):
        """
        Constructor for Accuracyclass

        Parameters:
            id: The database id of the record
            language: The language used
            corpus: The size of the corpus used
            algorithm: The type of algorithm used
            feature: The feature that is being considered such as bigram, trigram etc.
            accuracy: The accuracy thus obtained

        """
        self.language = language
        self.corpus = corpus
        self.algorithm = algorithm
        self.feature = feature
        self.accuracy = accuracy




class Form(FlaskForm):
    """

    This is a class for the form in the experiment
    
    Attributes:
        language: The language used
        corpus: The size of the corpus used
        algorithm: The type of algorithm used
        feature: The feature that is being considered such as bigram, trigram etc.

    """
    language = SelectField('language', choices=[])
    corpus = SelectField('corpus', choices=[])
    algorithm = SelectField('algorithm', choices=[])
    feature = SelectField('feature', choices=[])

