# Use the official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code (but not your local files)
COPY . /app/

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app in development mode, accessible from outside
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
