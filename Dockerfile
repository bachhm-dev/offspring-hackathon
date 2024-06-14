# Use an official Python runtime as the base image
# FROM python:3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11


# Set the working directory in the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    libopencv-dev \
    python3-opencv \
    python3-pip \
    tar \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install onnxruntime==1.17.0
RUN pip install fastapi
RUN pip install "uvicorn[standard]"

RUN pip install torchvision
RUN pip install --upgrade transformers==4.39.2
RUN pip install --upgrade requests
RUN pip install -q -U git+https://github.com/huggingface/peft.git
RUN pip install -q -U git+https://github.com/huggingface/accelerate.git
RUN pip install -q -U datasets scipy ipywidgets matplotlib



# Install the required dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application code to the working directory
COPY . /code/app

# Expose the port on which the application will run
EXPOSE 8000

# Define the command to run the application
# CMD ["fastapi", "run", "fast_api.py"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
