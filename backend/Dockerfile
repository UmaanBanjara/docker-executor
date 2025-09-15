# Base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install essential and fun tools
RUN apt-get update && apt-get install -y \
    bash coreutils tree procps \
    figlet toilet fortune-mod boxes \
    net-tools iproute2 \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user for safe sandboxing
RUN useradd -ms /bin/bash sandboxuser
USER sandboxuser

# Copy app folder with all tutorials and sample files
COPY app ./app

# Expose port for FastAPI
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
