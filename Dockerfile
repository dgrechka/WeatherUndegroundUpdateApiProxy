FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY api.py ./
CMD python api.py
EXPOSE 5000