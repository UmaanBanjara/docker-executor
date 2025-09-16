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

# Copy app folder with all tutorials and sample files
COPY app ./app

# /app readonly for everyone (still root)
RUN chmod -R a-w /app

# Add non-root user for safe sandboxing
RUN useradd -ms /bin/bash sandboxuser

# Writable workspace for sandboxuser
RUN mkdir /workspace && chown sandboxuser:sandboxuser /workspace

# Switch to non-root
USER sandboxuser

# Expose port for FastAPI
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
