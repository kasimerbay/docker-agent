from smolagents import HfApiModel, ToolCallingAgent, tool
import subprocess

@tool
def pull_images(image_names: list) -> None:
    """
    This is a tool for pull multiple images
    
    Args:
        image_names: names of the images as python list
    """

    for image in image_names:
        yield pull_image(image_name=image, image_tag="latest")

@tool
def pull_image(image_name: str, image_tag: str) -> None:
    """
    This is a tool that runs the given command on the host machine

    Args:
        image_name: image to be pulled from image registry
        image_tag: tag or version of desired image
    """
    command = f"ansible-playbook ansible-folder/pull_image.yml -e image_name={image_name} -e image_tag={image_tag}"
    return subprocess.run(command.split(" "), cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8")

@tool
def remove_images(image_names: list) -> None:
    """
    This is a tool for remove multiple images
    
    Args:
        image_names: names of the images as python list
    """
    
    for image in image_names:
        yield remove_image(image_name=image, image_tag="latest")

@tool
def remove_image(image_name: str, image_tag: str) -> None:
    """
    This is a tool that runs the given command on the host machine

    Args:
        image_name: image to be pulled from image registry
        image_tag: tag or version of desired image
    """
    command = f"ansible-playbook ansible-folder/remove_image.yml -e image_name={image_name} -e image_tag={image_tag}"
    return subprocess.run(command.split(" "), cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8")

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
        # VisitWebpageTool(),
        pull_image,
        remove_image,
        pull_images,
        remove_images,
        # run,
        # run_remote,
    ],
    model=model, 

)

agent.run(input("How can I serve you?\n- "))