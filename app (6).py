import gradio as gr
import os
# Replace 'your_hf_token' with the actual token
hf_token = os.getenv('hf_token')

# Load the private space using authentication
demo = gr.load("spaces/rowanm945/Cypher-Gradio", hf_token=hf_token)

demo.launch()