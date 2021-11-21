FROM python:3

# set the directory
WORKDIR /server

# copy all files
COPY . /server

# dependencies
RUN pip install -r requirements.txt

# host
EXPOSE 5000

# run command
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
