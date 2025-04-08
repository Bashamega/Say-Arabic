FROM python:3

# Install system dependencies
RUN apt-get update && apt-get install -y \
    imagemagick \
    ffmpeg \
    libsndfile1 \
    fonts-dejavu-core \
    fontconfig \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Fix ImageMagick security policy (allow text rendering)
RUN sed -i 's/rights="none"/rights="read|write"/g' /etc/ImageMagick-6/policy.xml || true

# Set workdir
WORKDIR /app


# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the script
ENTRYPOINT ["python", "main.py"]
