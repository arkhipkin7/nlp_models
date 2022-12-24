import pickle


class PipeLine:
    def __init__(self, model_file: str, tfidf_file: str):
        self.model = self.load_model(model_file)
        self.tfidf = self.load_model(tfidf_file)

    def load_model(self, file: str):
        model = pickle.load(open(file, 'rb'))
        return model

    def featurize(self, text):
        features = self.tfidf.transform(text)
        return features

    def predict(self, X):
        return self.model.predict(X).tolist()
