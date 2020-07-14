## Using sklearn lib-package: C:\Users\User\AppData\Local\Programs\Python\Python37\Lib\site-packages\sklearn\
## Installing: pip install -U scikit-learn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import pandas as pd
import numpy as np
import sys
from subprocess import call
import matplotlib.pyplot as plt
from PIL import Image


def RunforIris():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['Class'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .50
    train_num, test_num = df[df['is_train']==True], df[df['is_train']==False]
    label = pd.factorize(train_num['Class'])[0]
    features = df.columns[:4]
    print("\n")
    print(df)
    
    
    return train_num, test_num, label, features

def RunforCross200():
    data_in = np.loadtxt("cross200.txt")
    df = pd.DataFrame(data_in, columns=['Condiction_1','Condiction_2','Class'])
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    train_num, test_num = df[df['is_train']==True], df[df['is_train']==False]
    label = pd.factorize(train_num['Class'])[0]
    features = df.columns[:2]
    print("\n")
    print(df)
    
    return train_num, test_num, label, features
    
def RunforEllipse100():
    data_in = np.loadtxt("Ellipse100.txt")
    df = pd.DataFrame(data_in, columns=['Condiction_1','Condiction_2','Class'])
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
    train_num, test_num = df[df['is_train']==True], df[df['is_train']==False]
    label = pd.factorize(train_num['Class'])[0]
    features = df.columns[:2]
    print("\n")
    print(df)
    
    return train_num, test_num, label, features
    
def thresholdfortree(clf ,train_num, label, value, features): 
    print("\n\n================== Threshold Setting =======================")
    #train_num = train_num.drop(columns=['Class','is_train'])
    threshold = value
    predicted_proba = clf.predict_proba(train_num[features])
    #print(predicted_proba)
    predicted = (predicted_proba[:,1] >= threshold).astype('int')
    #print(predicted)
    #print(label)
    accuracy = accuracy_score(label, predicted)
    print("Accuracy: "+str(accuracy))
    print("============================================================")
    
def RFC(train_num, test_num, label, features):
    clf = RandomForestClassifier( n_estimators=10, criterion='gini', max_depth=None, 
                                  min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
                                  max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, 
                                  min_impurity_split=None, bootstrap=True, oob_score=True, n_jobs=1, 
                                  random_state=None, verbose=0, warm_start=False, class_weight=None)
    clf.fit(train_num[features], label)
    preds = clf.predict(test_num[features])
    predicted_proba = clf.predict_proba(train_num[features])
    #df = pd.DataFrame(predicted_proba, columns=['Condiction_1','Condiction_2'])
    #df['Class'] = label
    #print(df.to_string())
    print("Training Accuracy: "+str(accuracy_score(label, clf.predict(train_num[features]))))
    feature_persent = clf.feature_importances_
    return clf, preds, feature_persent
    
def PrintResult(train_num, test_num, features, preds, feature_persent):
    print("\n") 
    print(pd.crosstab(test_num['Class'], preds, rownames=['v Actual Class'], colnames=['Predicted Class > ']))
    print("\n") 
    print(list(zip(train_num[features], feature_persent)))
    print("\n") 
    label = pd.factorize(test_num['Class'])[0]
    print("Testing Accuracy: "+str(accuracy_score(label, preds)))

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

    
def run():
    choice = input("Select datasets for input: 1)Cross200.txt 2)Ellipse100.txt 3)Iris :  (1/2/3)  ")
    
    if choice.isdigit() is False:
        print("You must enter INTERGER for one of 1 , 2 , 3.")
        sys.exit(0)
    if int(choice) == 1:
        print("Select Set 1 : Cross200.txt")
        train_num, test_num, label, features = RunforCross200()
    elif int(choice) == 2:
        print("Select Set 2 : Ellipse100.txt")
        train_num, test_num, label, features = RunforEllipse100()
    elif int(choice) == 3:
        print("Select Set 2 : Iris dataset")
        train_num, test_num, label, features = RunforIris()
    else:
        print("You must select one of 1 , 2 , 3.")
        sys.exit(0)
    clf, preds, feature_persent = RFC(train_num, test_num, label, features)
    PrintResult(train_num, test_num, features, preds, feature_persent)
    
    estimator = clf.estimators_[0]
    #print(clf.estimators_)
    if int(choice) == 1 or int(choice) == 2 :
        export_graphviz(estimator, out_file='tree.dot', 
                        feature_names = ['Condiction_1','Condiction_2'],
                        class_names = ['1','2'],
                        rounded = True, proportion = False, 
                        precision = 2, filled = True)
    else:
        export_graphviz(estimator, out_file='tree.dot', 
                        feature_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
                        class_names = ['setosa', 'versicolor', 'virginica'],
                        rounded = True, proportion = False, 
                        precision = 2, filled = True)
    
    call('dot -Tpng tree.dot -o tree.png -Gdpi=600')
        
    print(clf.oob_score_)
    
    '''
    quit = ''
    print( "Threshold Checker: type 'quit' to stop" )
    while quit.lower() != 'quit':
        quit = input("Input threshold value: ( 0 <= x <= 1 ) :  ")
        if isfloat(quit) is True:
            thresholdfortree(clf, train_num, label ,float(quit) ,features)
    '''
        
    
    
    

if __name__ == "__main__":
    run()