FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install flask nltk scikit-learn

RUN python -c "import nltk; nltk.download('punkt')"
RUN python backend/train_model.py

EXPOSE 5000
CMD ["python", "backend/app.py"]