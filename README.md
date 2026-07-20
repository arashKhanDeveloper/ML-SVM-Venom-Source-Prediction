# Venom Source Prediction - SVM -> SVC 

## Portfolio Project

Machine Learning project using SVM for venum source prediction with data visualization, preprocessing, feature scaling, and model evaluation.

## Features

- Data preprocessing
- Data analysis 
- EDA 
- Visulization
- Data summary 
- remove Duplicates
- Removing Outliers 
- Fill nan data by "mean"
- Encoding string data by OneHotEncoder
- StandardScaler 
- ColumnTransformer 
- Model evaluation (Accuracy, confusion_matrix, classification_report)  
- Cross Val Score
- Make Pipeline 
- Saved Model and Preprocesser as pickle 

## model 
 
- SVM -> SVC

## Data

- Dataset Source : Kaggle 
- Dataset License : CC0: Public Domain
- Dataset Link: https://www.kaggle.com/datasets/jacopoferretti/emergency-triage-venomous-bites-dataset

## Accuracy

Test Accuracy: 99.63 % 

## About Files 

- app/venumSource.py : for running model and get result 
- data/silent_sting_triage_data_sample.csv
- pickles/pipeline.pickle: model and preprocessor pickle 
- pickles/column_transformer.pickle: just ct pickle
- pickles/classifier.pickle: just model(without preprocess) pickle
- notebook.ipynb: notebook project
- README.md
- requirements.txt
- .gitignore
- LICENSE

# For runnig project
- go to app folder -> venumSource.py
- this is the file that you can run the model and get answer 

# Full Model
- go to -> notebook.ipynb 
- this is all code about visulization-preprocessing-model-evaluation-make pickles and ... 