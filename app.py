import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Enable CORS (Prevents loading issues)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define Gradio Interface
def interactive_function(input_text):
    return f"You entered: {input_text}"

demo = gr.Interface(
    fn=interactive_function,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.Textbox(label="Output"),
    title="Interactive Cypher",
    theme="default"
)

# ✅ Redirect `/` to `/gradio`
@app.get("/")
async def redirect_to_gradio():
    return RedirectResponse(url="/gradio")

# ✅ Mount Gradio app under `/gradio`
app.mount("/gradio", gr.mount_gradio_app(app, demo, path="/gradio"))

# ✅ Run FastAPI & Gradio Together
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
