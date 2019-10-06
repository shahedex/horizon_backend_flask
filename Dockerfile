FROM python:3.7

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "manage.py", "runserver"]