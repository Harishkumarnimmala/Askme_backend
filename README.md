# 🚀 AskMe Chatbot - Backend

## Overview
This repository contains the **backend** for the **AskMe Chatbot**, built with **FastAPI** and powered by **Llama 3.2** via **Hugging Face** and **LangChain**. The backend provides an **LLM-powered conversational AI** that can be accessed via API.

### LLM Model:
* **Llama-3.2-1B** - Text generation Model
  * Input modalities: Multilingual Text
  * Output modalities: Multilingual Text and code
  * Model size: **1.23B** ;Tensor Type: **BF16**; Context length: **128k**; Token count: **up to 9T**
  * knowledge cutoff: December 2023 

---

## 📌 Features
- **FastAPI**: High-performance backend for handling chatbot requests.
- **Llama 3.2**: State-of-the-art LLM loaded via Hugging Face.
- **LangChain**: For handling prompt engineering and LLM interactions.
- **Dockerized**: Runs in a container for easy deployment.
- **Azure Deployment**: Deployed on **Azure Virtual Machine** or **Azure App Service**.
- **MongoDB/PostgreSQL Support**: For storing conversation history.
- **JWT Authentication**: Secure API endpoints.
- **Logging & Monitoring**: Integrated with **Azure Monitor**.

---

## 🛠️ Tech Stack
- **FastAPI** (Backend framework)
- **Hugging Face Transformers** (Model loading)
- **LangChain** (Conversational AI framework)
- **Llama 3.2** (LLM model)
- **Docker** (Containerization)
- **MongoDB/PostgreSQL** (Database)
- **Azure Virtual Machine / App Service** (Deployment)

---

## 🔧 Installation & Setup

1. Create & Activate Conda Environment

```
conda create backend-llm python==3.11
conda activate backend-llm
```
2. Clone the Repository

```sh
git clone https://github.com/your-org/askme-backend.git
cd askme-backend
```

3. Install dependencies
```
pip install requirements.txt
```

4. Start the backend using FastAPI

```
python main.py
```

**Note:** 
  * Backend will listen on port 2000 in localhost

### For querying:

1. Open port 2000 in a browser
2. Write your Query

````sh
http:\\localhost:2000/search?query="write your Query"
````


### Docker Instructions:

1. Download and install Docker

2. Build Docker Image

```
docker compose build --no-cache --progress=plain | tee build.log
```
**Note:** Docker build log will be saved **build.log** file

3. Start container

```
docker compose up
```
**Note:** 
  * Backend will listen on port 2000 in localhost


### Incase of LLama 3.2 download from HuggingFace:

* Download and install HuggingFace CLI
```
pip install -U "huggingface_hub[cli]"
```
* Login into HuggingFace using token

```
huggingface-cli login --token $HF_TOKEN
```
