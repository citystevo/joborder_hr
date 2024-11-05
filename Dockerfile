FROM python:3.11.4-slim-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-server-dev-all \
    python3-dev \
    libpq-dev \
    gcc

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app

# Run gunicorn with the correct path
ENTRYPOINT ["gunicorn", "inventoryproject.wsgi:application", "-b", "0.0.0.0:8000"]
