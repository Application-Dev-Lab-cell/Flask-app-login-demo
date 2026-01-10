# 1. Use an official lightweight Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements file first (so dependencies can be cached)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install -r requirements.txt

# 5. Copy all project files into the container
COPY . .

# 6. Run the app using Gunicorn (production server)
CMD ["gunicorn", "app:app"]

ENV WEB_CONCURRENCY=1