FROM python:3

# set the directory
WORKDIR /app

# copy all files
COPY . /app

# dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Entry point
ENTRYPOINT [ "flask" ]

# run command
CMD ["run", "--host","0.0.0.0"]
