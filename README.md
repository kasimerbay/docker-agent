# Docker Agent

`docker-agent` is a Python-based tool that leverages AI agents to manage Docker images on a host machine. It provides functionalities to pull and remove Docker images using predefined Ansible playbooks.

This tool uses your prompts as input, leverages Ansible as the main tool, and provides artificial intelligence capabilities for your docker operations

## Features

- Pull Docker images from a registry
- Remove Docker images from the host machine

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/docker-agent.git
    cd docker-agent
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install Ansible and the Docker community collection:
    ```sh
    pip install ansible:2.18
    ansible-galaxy collection install community.docker
    ```
## Configuration

Update the `agent.py` file to include your Hugging Face API token:

```python
model = HfApiModel(
    model="qwen2.5",
    token="<YOUR_HUGGINGFACE_TOKEN>"
)
```

## Usage

To interact with `docker-agent`:

```python
python3 agent.py
```

### Pull Docker Images

To pull Docker images, prompt:

- **pull <image_name> with <image_tag>**, or
- **pull <image_name> with <image_tag> on my local machine**, or
- **pull <image_name> with <image_tag> to my local**, or even multiple images at the same time:
- **pull haproxy and jenkins images to my local machine**...


### Remove Docker Images

To remove Docker images, prompt:

- **remove <image_name> with <image_tag>**, or
- **remove <image_name> with <image_tag> from my local machine**, or
- **remove <image_name> with <image_tag> from my local**, or even multiple images at the same time:
- **remove haproxy and jenkins images from my local machine**...


## Citing
- smolagents,
- ansible

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.