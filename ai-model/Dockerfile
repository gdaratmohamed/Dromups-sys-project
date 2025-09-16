# Use a lightweight Python base image
FROM python:3.10-slim

# Avoid creating .pyc files and enable unbuffered output (logs instantanés)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies needed by OpenCV and ultralytics
# RUN apt-get update && apt-get install -y \
   # libgl1 \
   # libglib2.0-0 \
   # && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code
COPY . .

# Expose port FastAPI will run on
EXPOSE 8000

# Command to start FastAPI server with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
