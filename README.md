# Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Description:
The dataset contains pre-labelled tweet and messages from real-life disaster events. The project aim is to build a Natural Language Processing (NLP) model to categorize messages on a real time basis.

This project is divided in the following key sections:

Processing data, building an ETL pipeline to extract data from source, clean the data and save them in a SQLite DB
Build a machine learning pipeline to train the which can classify text message in various categories
Run a web app which can show model results in real time

This is an example of a message we can type to test the performance of the model
![image](https://user-images.githubusercontent.com/44659532/126101152-82bffe24-17d2-4163-af55-a5c50741647e.png)

After clicking Classify Message, we can see the categories which the message belongs to highlighted in green
![image](https://user-images.githubusercontent.com/44659532/126101666-6cb9beb6-6c62-42b0-b646-c13655b184d5.png)
