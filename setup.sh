# setup.sh - Installation script
#!/bin/bash

# Update and install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Set up environment file
touch .env

echo "Setup complete. Don't forget to configure your .env file!"
