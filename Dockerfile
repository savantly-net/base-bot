FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirement first to help cache the docker layer
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

ENV PORT=9000
ENV HOST=0.0.0.0

CMD [ "sh", "-c", "uvicorn main:app --reload --port ${PORT} --host ${HOST}" ]