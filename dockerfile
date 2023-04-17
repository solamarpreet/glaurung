# Set the base image
FROM python:slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the container
COPY .env /app
COPY src/. /app

# Set the command to run the application
CMD [ "python", "main.py" ]
