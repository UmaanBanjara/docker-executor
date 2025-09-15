# Base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install minimal system dependencies
RUN apt-get update && apt-get install -y bash coreutils curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies (as root)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user
RUN useradd -ms /bin/bash sandboxuser
USER sandboxuser

# Copy app folder
COPY app ./app

# Expose port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
