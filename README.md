# Defense Trend Detector RAG

## Install dependencies

1. **Set Up a Python Virtual Environment**  
   Before installing dependencies, create and activate a virtual environment to keep packages isolated.

   - **Create a virtual environment**:
     ```sh
     python3 -m venv venv
     ```
   - **Activate the virtual environment**:
     - **MacOS/Linux**:
       ```sh
       source venv/bin/activate
       ```
     - **Windows (Command Prompt)**:
       ```sh
       venv\Scripts\activate
       ```
     - **Windows (PowerShell)**:
       ```sh
       venv\Scripts\Activate.ps1
       ```
    - **(WHEN FINISHED) Deactivate the virtual environment**:
       ```sh
       deactivate
       ```

2. **Do the following before installing the dependencies found in `requirements.txt` file because of current challenges installing `onnxruntime` through `pip install onnxruntime`.**

   - For MacOS users, a workaround is to first install `onnxruntime` dependency for `chromadb` using:

     ```sh
     conda install onnxruntime -c conda-forge
     ```
     See this [thread](https://github.com/microsoft/onnxruntime/issues/11037) for additional help if needed.

   - For Windows users, follow the guide [here](https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file) to install the Microsoft C++ Build Tools. Be sure to follow through to the last step to set the environment variable path.

3. **Now run this command to install dependencies in the `requirements.txt` file.** 

   ```sh
   pip3 install -r requirements.txt
   ```

4. **Install markdown depenendies with:** 

    ```sh
    pip3 install "unstructured[md]"
    ```

## Create vector-embedding database

Create the Chroma DB.

```python
python3 create_database.py
```

## Query the database

Query the Chroma DB.

```python
python3 query_data.py "How does Alice meet the Mad Hatter?"
```

> You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.

## Important setup notes

Before use, ensure that you have an AWS account setup, have installed the AWS CLI client, ran `aws configure` to configure your access keys and secret access keys available through your account console, and requested access to AWS Bedrock text embedding models (granted immediately).
