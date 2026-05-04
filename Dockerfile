FROM python:3.9

ARG GROUP_NAME

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_DEBUG=true
ENV DATABASE_NAME=${GROUP_NAME}

CMD [ "python", "./simple_python_app/app.py" ]