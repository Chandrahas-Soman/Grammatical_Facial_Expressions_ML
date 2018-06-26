import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
import main
import numpy as np
from scipy import stats

import warnings
warnings.filterwarnings("ignore")

ab_accuracy=[]
a_accuracy=[]
b_accuracy=[]

scoring_metrics = ['accuracy', 'precision', 'recall', 'roc_auc', 'f1']

list1 = ['affirmative_datapoints', 'conditional_datapoints', 'doubt_question_datapoints', 'emphasis_datapoints',
         'negative_datapoints', 'relative_datapoints', 'topics_datapoints', 'wh_question_datapoints',
         'yn_question_datapoints']


# Loading the data
def load_data(file_name):
    input_data = pd.read_csv('/Users/chandrahasmakarandsoman/Downloads/grammatical_facial_expression/'+file_name[0]+'.txt',
                             sep = " ")
    input_target = pd.read_csv('/Users/chandrahasmakarandsoman/Downloads/grammatical_facial_expression/'+file_name[1]+'.txt',
                             sep = " ")
    input_data_without_timestamp = input_data.drop(input_data.columns[[0]], axis=1)
    print("Shape of Data frame before removing Outliers: {}".format(input_data_without_timestamp.shape))
    outlier_index=[]
    input_data_without_outliers=input_data_without_timestamp[(np.abs(stats.zscore(input_data_without_timestamp)) < 3).all(axis=1)]
    len(input_data_without_outliers)
    a = (np.abs(stats.zscore(input_data_without_timestamp)) < 3).all(axis=1)
    i=0
    for k in a:
        if not k:
            outlier_index.append(i)
        i += 1

    for i in outlier_index[::-1]:
        input_target = input_target.drop(input_target.index[i])
    print("Shape of Data frame after removing Outliers: {}".format(input_data_without_outliers.shape))
    return input_data_without_outliers, input_target

#Model Development
def log_reg_model(file1, cv):
    log_class = LogisticRegression()
    print("\nLogistic Regression:")
    scoring(log_class, file1, cv)
    get_accuracy(log_class, file1, cv)
    feature_sel(log_class, file1[0], file1[1], "Logistic Regression")


def lda_model(file1, cv):
    lda = LinearDiscriminantAnalysis()
    print("\nLinear Discriminant Analysis:")
    scoring(lda, file1, cv)
    get_accuracy(lda, file1, cv)
    feature_sel(lda, file1[0], file1[1],"Linear Discriminant Analysis")


def qda_model(file1, cv):
    qda = QuadraticDiscriminantAnalysis()
    print("\nQuadratic Discriminant Analysis:")
    scoring(qda, file1, cv)
    get_accuracy(qda, file1, cv)
    feature_sel(qda,file1[0],file1[1],"Quadratic Discriminant Analysis")


def rf_model(file1, cv):
    rf_class = RandomForestClassifier(n_estimators=10)
    print("\nRandom Forest Classifier: ")
    scoring(rf_class, file1, cv)
    get_accuracy(rf_class, file1, cv)
    feature_sel(rf_class, file1[0], file1[1],"Random Forest Classifier")


#Using Different models
def perform_modelling(data, target, cv_value):
    log_reg_model([data, target], cv_value)
    lda_model([data, target], cv_value)
    qda_model([data, target], cv_value)
    rf_model([data, target], cv_value)
    print('\n')


#Performance using different metrics
def scoring(model_type, file, cv):
    for i in scoring_metrics:

        cross_val = cross_val_score(model_type, file[0], file[1].values.ravel(), scoring=i, cv=cv)
        score = cross_val.mean() * 100
        print("{} is: ".format(i), score)


def get_accuracy(model_type, file, cv):
    cross_val = cross_val_score(model_type, file[0], file[1].values.ravel(),scoring='accuracy', cv=cv)
    accuracy = cross_val.mean() * 100
    ab_accuracy.append(accuracy)


def feature_sel(model,data,target, name):
    #print(data)
    rfe = RFE(model, 1)
    rfe = rfe.fit(data, target)
    print("Best Feature using {} model is : {} ".format(name, rfe.ranking_[0]))


def comparison():
    a_accuracy=ab_accuracy[:36]
    b_accuracy=ab_accuracy[36:]

    for i in range(len(a_accuracy)):

        if i%4 == 0:
            print(list1[(i//4)])
            print("                                          \t\t   user a\tuser b")
            print("Logistic Regression Accuracy:             \t\t"+ str(a_accuracy[i]) + "\t" + str(b_accuracy[i]))
        elif i % 4 == 1:
            print("Linear Discriminant Analysis Accuracy:    \t\t"+ str(a_accuracy[i]) + "\t" + str(b_accuracy[i]))
        elif i % 4 == 2:
            print("Quadratic Discriminant Analysis Accuracy: \t\t"+ str(a_accuracy[i]) + "\t" + str(b_accuracy[i]))
        else:
            print("Random Forest Accuracy:                   \t\t"+ str(a_accuracy[i]) + "\t" + str(b_accuracy[i])+"\n")


if __name__ == '__main__':
    main.main()