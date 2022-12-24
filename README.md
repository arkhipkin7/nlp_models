# Intro

The goal of this project is to learn the entire pipeline process using an NLP project, that contans:
- data loading;
- fit model;
- building an application;
- deployment using docker and Kubernet.


# About data

You can load data from [kagle page](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification?resource=download)

# Stepts

## Run as python project

Create and run enviroment

```
conda create -n model-deploy python=3.9.7
conda activate model-deploy
```

Then install necessary libraries
```
pip install Flask scikit-learn
```

Now you can run local python application and test it

```
python deploy.py
```
Open python console and write this:

```
import requests
requests.post(
    'http://127.0.0.1:5000/predict', 
    json={
      "text": """
      You are a winner U have been specially selected 2 receive ¬£1000 or
      a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810910p/min (18+)"
     }
).text
```

You should see something like this:

```
{"Predictions": ["spam"]}
```
