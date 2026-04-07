FROM --platform=linux/arm64 python:3.11-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["pytest", "--alluredir=allure-results"]