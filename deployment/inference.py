import pickle
import pandas as pd


class Inference:
    def __init__(self) -> None:
        self.onehot = pickle.load(open("../model/_enc_onehot.pkl", "rb"))
        self.ordinal = pickle.load(open("../model/_enc_ordinal.pkl", "rb"))
        self.model = pickle.load(open("../model/_model_linreg.pkl", "rb"))

    def __preprocess(self, data):
        df = pd.DataFrame([data])
        # transform parental level of education into learned ordinal encoder
        parent_edu = df.loc[:, "parental level of education"]
        df.loc[:, "parental level of education"] = self.ordinal.transform(
            parent_edu.values.reshape(parent_edu.shape[0], 1)
        )
        # transform another category variable into learned onehot encoder
        category = ["gender", "race/ethnicity", "lunch", "test preparation course"]
        onehot = pd.DataFrame(
            self.onehot.transform(df[category]),
            columns=self.onehot.get_feature_names_out(category),
        )
        # set index again, bcs onehot encoding remove index
        onehot.index = df.index
        # drop original category variable
        df.drop(category, inplace=True, axis=1)
        # concat encoded variable
        df = pd.concat([df, onehot], axis=1)

        return df

    def make_prediction(self, data):
        # preprocess data first
        X = self.__preprocess(data)
        # predict
        pred_score = self.model.predict(X)

        return {"predicted_score": pred_score}
