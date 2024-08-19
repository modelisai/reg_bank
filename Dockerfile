FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Don't copy the app files, they will be mounted as a volume

CMD ["streamlit", "run", "./research/research.py"]