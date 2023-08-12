FROM python:3.9-slim-buster

# Set the working directory to /
WORKDIR /

# Copy main.py and dataset.csv into the container root
COPY recorder.py dataset.csv /

# Create a volume to store the dataset in /usr/asd
VOLUME /usr/asd

# Install any dependencies
RUN pip install pandas requests

# Set the command to run
CMD [ "python3", "recorder.py" ]
