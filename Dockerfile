# STEP 1: Choose a "Base" (The Operating System)
# We use python:3.9-slim because it's small and fast.
FROM python:3.9-slim

# STEP 2: Install System Dependencies with extra resilience
RUN apt-get update --fix-missing && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# STEP 3: Set the Workspace
# This creates a folder inside the "virtual machine" called /app.
WORKDIR /app

# STEP 4: Copy the "Instructions"
# We copy the requirements file first to take advantage of Docker's caching.
COPY requirements.txt .

# STEP 5: Install Python Tools
RUN pip install --no-cache-dir -r requirements.txt

# STEP 6: Copy your Code
# This moves your processor.py and folders into the image.
COPY . .

# STEP 7: The Start Command
# What should happen when the "machine" turns on?
CMD ["python", "processor.py"]