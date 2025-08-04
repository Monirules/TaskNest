FROM python:3.10-slim

# Install system dependencies for mysqlclient and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    libmariadb-dev-compat \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Use gunicorn instead of flask's built-in server
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]

