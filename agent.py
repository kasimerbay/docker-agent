from smolagents import HfApiModel, ToolCallingAgent
from docker_tools import *

model = HfApiModel(
    # Available model options:
    # model="meta-llama/Llama-2-7b-chat-hf"
    # model="mistralai/Mixtral-8x7B-Instruct-v0.1"
    # model="tiiuae/falcon-7b"
    # model="google/flan-t5-xxl"
    # model="bigscience/bloom"
    model="qwen2.5",
    token="<YOUR_HUGGINGFACE_TOKEN>"
)

agent = ToolCallingAgent(
    tools=[

        pull_image,
        pull_images,
        remove_container,
        remove_image,
        run_container,
        stop_container,
        remove_all_containers,
        remove_all_images,
    ],
    model=model,

)

while True:
    user_prompt = input("How can I serve you?\n- ")

    if user_prompt == "exit":
        break
    agent.run(user_prompt)
    
    