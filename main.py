from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from huggingface_hub._login import login
import logging

# Define FastAPI instance
app = FastAPI()


# Define a Pydantic model for the request body
class InferenceRequest(BaseModel):
    prompt: str


# Load the LLaMA-7B model and tokenizer from Hugging Face
model_name = os.getenv("MODEL_NAME")
token = os.getenv("HUGGINGFACE_TOKEN")
login(token)

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    token=token,
)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    token=token,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print(device)

@app.post("/generate")
async def generate_text(request: InferenceRequest):
    prompt = request.prompt
    try:
        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        # Generate output using the model
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=100)

        # Decode the output tokens back to text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Return the generated text as a response
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Main entry point to run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
