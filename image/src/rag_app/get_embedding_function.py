# from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_aws import BedrockEmbeddings
import boto3
from dotenv import load_dotenv
import os
load_dotenv()

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")

bedrock_client = boto3.client(
    "bedrock-runtime", 
    aws_access_key_id=AWS_ACCESS_KEY_ID, 
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def get_embedding_function():
    embeddings = BedrockEmbeddings(
        client=bedrock_client, region_name="us-east-1", model_id="amazon.titan-embed-text-v1"
    )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings