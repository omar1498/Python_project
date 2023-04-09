FROM python:3
WORKDIR /NEW_PROJECT
COPY . /NEW_PROJECT/
RUN pip install -r Requirements.txt
EXPOSE 18333
CMD python /NEW_PROJECT/app.py
