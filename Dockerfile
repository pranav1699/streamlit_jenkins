FROM python:3.8-slim-buster

RUN pip install --upgrade pip
RUN apt-get update -y

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8502
RUN mkdir ~/.streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
