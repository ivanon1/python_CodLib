#Libraries 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn import model_selection
from sklearn.model_selection import learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

#Read in data
df = pd.read_csv("C:\\Users\\Jake Ivanov\\Desktop\\qsar_oral_toxicity\\qsar_oral_toxicity.csv")
#Shape of dataframe 
df.shape, df.head()
#Rename target labels 
df.rename(columns = {'negative':'labels'}, inplace =True)
#Create a new labels column to factorize 
df['labels'] = pd.factorize(df['labels'])[0]

def class_plotter(): 

    #Plot class imbalances 
    df['labels'].value_counts().plot(kind = "barh")
    plt.xlabel("Count")
    plt.ylabel("Classes")
    plt.show()

#Function to upscale data for class imbalances
def upsample_class_balances():
    
    #Seperate majority and minority classes 
    df_major = df[df.labels==0]
    df_minor = df[df.labels==1]

    #Upsample minority class 
    df_minor_upsample = resample(df_minor, replace=True,n_samples=8250,random_state= 123)
    #Combine majority and upsampled minority 
    df_upsampled = pd.concat([df_major,df_minor_upsample])
    #Show new class labels 
    df_upsampled.labels.value_counts()
    
    return df_upsampled

#Seperate input features and target variables 
X = pd.DataFrame(upsample_class_balances(), columns = df.drop("labels",axis =1 ).columns)
Y = upsample_class_balances().labels
#train-test split data
X_train, X_test,Y_train,Y_Test = train_test_split(X,Y, test_size = 0.20, stratify = Y, random_state = 1)
#create Random Forest Model with 100 trees 
rf_model = RandomForestClassifier(n_estimators=100,bootstrap=True,max_features='sqrt')
#Logit model 
logit_model = LogisticRegression()
classifier_1 = LogisticRegression().fit(X_train,Y_train)    #Fit logit on training data  
classifier_2 = rf_model.fit(X_train,Y_train)                #Fit RM model on training data 

def classifier_accuracy():
    #Predict on training data 
    pred_y_1 = classifier_1.predict(X_train)
    print(np.unique(pred_y_1))

    #Print accuracy 
    print("Training accuracy score: %.3f" % accuracy_score(Y_train,pred_y_1))
     
def classification_metrics():
    #Generate classification report 
    predicted = classifier_1.predict(X_test) #Model needs to be fitted before calling predict on estimator 
    report = classification_report(Y_Test,predicted)
    print(report)

    #Generate confusion matrix 
    matrix = confusion_matrix(Y_Test,predicted)
    print(matrix)

def accuracy_evaluation():
    #Measure accuracy using  AUC Curve metrics for training data 
    kfold = model_selection.KFold(n_splits=10,random_state=7)
    model = logit_model
    results = model_selection.cross_val_score(model,X_train,Y_train,cv=kfold,scoring='roc_auc')
    print(("AUC: %.2f (%.2f)") % (results.mean(),results.std()))

    #Measure log loss of logistric regression algorithm (0 is perfect log loss)
    log_loss_results = model_selection.cross_val_score(model,X_train,Y_train,cv=kfold,scoring='neg_log_loss')
    print(("\nLog Loss: %.2f (%.2f)") % (log_loss_results.mean(),log_loss_results.std()))


def learning_C():
    pipe_lr = make_pipeline(StandardScaler(),RandomForestClassifier(random_state=1)) 
    train_sizes, train_scores, test_scores = learning_curve(estimator=pipe_lr,X=X_train, y=Y_train, train_sizes=np.linspace( 0.1, 1.0, 10), cv=10, n_jobs=1)
    train_mean = np.mean(train_scores, axis=1) 
    train_std = np.std(train_scores, axis=1) 
    test_mean = np.mean(test_scores, axis=1) 
    test_std = np.std(test_scores, axis=1) 
    plt.plot(train_sizes, train_mean,color='blue', marker='o',markersize=5, label='training accuracy') 
    plt.fill_between(train_sizes,train_mean + train_std,train_mean - train_std, alpha=0.15, color='blue')
    plt.plot(train_sizes, test_mean,color='green', linestyle='--',marker='s', markersize=5,label='validation accuracy') 
    plt.fill_between(train_sizes,test_mean + test_std,test_mean - test_std, alpha=0.15, color='green') 
    plt.grid()
    plt.xlabel('Number of training samples')
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')
    plt.ylim([0.8, 1.0]) 
    plt.show()

