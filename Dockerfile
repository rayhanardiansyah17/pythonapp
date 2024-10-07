FROM python

WORKDIR /usr/src/myapp

COPY . /usr/src/myapp

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]