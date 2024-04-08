import pickle
import boto3
import json
import nltk
from nltk.tokenize import TreebankWordTokenizer

def lambda_handler(event, context):
    
    text = "Input Text"
    bucket = "jack-bucket-ml-code"
    vectoriser_file = ""
    
    s3 = boto3.resource('s3')
    lambda_ = boto3.client('lambda')

    nltk.download('punkt')
    nltk.download('stopwords')

    vectoriser = pickle.loads(
        s3.Bucket(bucket)\
            .Object(f"{vectoriser_file}.pickle")\
            .get()['Body'].read()
    )
    preprocessed_text = vectoriser.transform([text])


    lambda_name = ""
    processed_text = json.dumps({"text_vector": preprocessed_text})

    response = lambda_.invoke(
        FunctionName=lambda_name,
        Payload=processed_text,
    )
    print(response)
    return response["Payload"]


import pickle
import boto3
import sklearn

def lambda_handler(event, context):
    print(event)
    bucket = "jack-bucket-ml-code"
    model_file = ""
    
    s3 = boto3.resource('s3')

    model = pickle.loads(
        s3.Bucket(bucket)\
            .Object(f"{model_file}.pickle")\
            .get()['Body'].read()
    )

    preprocessed_text = event["text_vector"]
    prediction = model.predict(preprocessed_text)

    if prediction == 1:
        response = '\nYOUR TEXT SEEMS THREATENING!\n'
    else:
        response = '\nYOUR TEXT SEEMS NON-THREATENING!\n'
    
    return {"response": response}