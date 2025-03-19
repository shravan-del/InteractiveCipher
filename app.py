import os
import gradio as gr
from fastapi import FastAPI

app = FastAPI()

# Define Gradio Interface
def interactive_cypher(input_text):
    return f"Processing: {input_text}"

interface = gr.Interface(fn=interactive_cypher, inputs="text", outputs="text")

@app.get("/")
def home():
    return {"message": "Interactive Cypher is running!"}

@app.get("/gradio")
def launch_gradio():
    return interface.launch(share=True)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
