# Description

*recommended python version **3.12.3***

This repo is learning material for GenAI class, follow these steps to set up and activate the environment for the project:

## 1. Activate Conda Environment
Activate your Conda environment by running the following command:

```bash
conda activate <your_environment_name>
```

## 2. Install Dependencies
Install the required dependencies:

```bash
pip install uv
uv pip install -r requirements.txt
```

## 3. Create a `.env` File
Create a `.env` file in the root of your project directory with the following structure:

```env
GROQ_API_KEY=gsk_**********************
GROQ_API_URL=https://api.groq.com/openai/v1
GROQ_MODEL=meta-llama/llama-4-maverick-17b-128e-instruct
```

### Notes:
- Replace `gsk_**********************` with your actual **GROQ API Key**.
- Update the `GROQ_MODEL` field if you want to use a different model.

## 4. Additional Information
- Ensure you have the proper Python version installed as specified in your project requirements.
- Make sure `uv` is installed properly as a utility command.