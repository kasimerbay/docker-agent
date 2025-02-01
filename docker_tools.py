from smolagents import tool
import subprocess

def run(command: str) -> None:
    """
    This is a tool that runs the given command on the host machine

    Args:
        command: command to be run on the host machine
    """
    return subprocess.run(command.split(" "), cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8")


@tool
def pull_image(image_name: str, image_tag: str) -> None:
    """
    pull, install an image from the image registry

    Args:
        image_name: image to be pulled from image registry
        image_tag: tag or version of desired image. default is "latest" 
    """
    command = f"ansible-playbook ansible-folder/pull_image.yml -e image_name={image_name} -e image_tag={image_tag}"
    return run(command)


@tool
def remove_image(image_name: str, image_tag: str) -> None:
    """
    remove or uninstall an image from the host machine

    Args:
        image_name: image to be pulled from image registry
        image_tag: tag or version of desired image. default is "latest"
    """
    command = f"ansible-playbook ansible-folder/remove_image.yml -e image_name={image_name} -e image_tag={image_tag}"
    return run(command)

@tool
def stop_container(image_name: str) -> None:
    """
    stops the given container

    Args:
        image_name: name of the container to be stopped
    """
    command = f"ansible-playbook ansible-folder/stop_container.yml -e image_name={image_name}"
    return run(command)

@tool
def run_container(image_name: str, image_tag: str) -> None:
    """
    run or start a container from the given image

    Args:
        image_name: image to be pulled from image registry
        image_tag: tag or version of desired image. default is "latest"
        
    """
    command = f"ansible-playbook ansible-folder/run_container.yml -e image_name={image_name} -e image_tag={image_tag}"
    return run(command)

@tool
def remove_container(image_name: str) -> None:
    """
    delete or remove the given container

    Args:
        image_name: name of the container to be stopped
    """
    command = f"ansible-playbook ansible-folder/remove_container.yml -e image_name={image_name}"
    return run(command)

@tool
def remove_all_containers() -> None:
    """
    delete or remove all containers from the host machine. Use this method only if you are promted "remove all containers"
    """
    command = f"ansible-playbook ansible-folder/remove_all_containers.yml"
    return run(command)

@tool
def remove_all_images() -> None:
    """
    delete or remove all images from the host machine. Use this method only if you are promted "remove all images"
    """
    command = f"ansible-playbook ansible-folder/remove_all_images.yml"
    return run(command)

@tool
def pull_images(image_names: list) -> None:
    """
    pull, install multiple images from the image registry. Give a list of image names of the format ['image1', 'image2', 'image3']
    
    Args:
        image_names: list of images to be pulled from image registry
    """
    command = f"""ansible-playbook ansible-folder/pull_images.yml -e "image_names={image_names}" """
    return run(command)