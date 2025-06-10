FROM python:3.12-slim

WORKDIR /code

RUN apt-get update \
  && apt-get -y install libpq-dev gcc postgresql \
  && apt-get clean

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]