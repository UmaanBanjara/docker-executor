# Base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for safety
RUN useradd -ms /bin/bash sandboxuser
USER sandboxuser

# Copy Python dependencies and backend code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../app ./app

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
