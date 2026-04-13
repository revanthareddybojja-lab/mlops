FROM python:3.9
WORKDIR /app
COPY . .
CMD ["python", "train.py"]