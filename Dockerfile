FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && \
    pip install flask
CMD ["python3", "echo_service.py"]