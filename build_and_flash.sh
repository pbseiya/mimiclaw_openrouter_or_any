#!/bin/bash

# Configuration
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IDF_PATH_LOCAL="$HOME/projects/esp-idf"
PORT="/dev/ttyUSB0"

echo "🚀 Starting MimiClaw Automation Script..."

# 1. Check .env file
if [ ! -f "$PROJECT_DIR/.env" ]; then
    echo "❌ Error: .env file not found in $PROJECT_DIR"
    exit 1
fi

# 2. Synchronize Secrets
echo "🔐 Synchronizing secrets from .env..."
python3 "$PROJECT_DIR/scripts/gen_secrets.py"
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to generate secrets."
    exit 1
fi

# 3. Load ESP-IDF Environment
echo "📦 Loading ESP-IDF environment..."
if [ -f "$IDF_PATH_LOCAL/export.sh" ]; then
    . "$IDF_PATH_LOCAL/export.sh"
else
    echo "❌ Error: ESP-IDF export.sh not found at $IDF_PATH_LOCAL"
    exit 1
fi

# 4. Build Project
echo "🏗️ Building project..."
cd "$PROJECT_DIR"
idf.py build
if [ $? -ne 0 ]; then
    echo "❌ Error: Build failed."
    exit 1
fi

# 5. Flash to Board
echo "⚡ Flashing to $PORT..."
# Attempt to fix permission using the provided password if necessary, 
# but usually chmod 666 lasts until reboot
idf.py -p "$PORT" flash
if [ $? -ne 0 ]; then
    echo "⚠️ Flash failed. Trying to fix permissions and retry..."
    echo "Seiya010" | sudo -S chmod 666 "$PORT"
    idf.py -p "$PORT" flash
fi

echo "✅ All done! Your MimiClaw is ready."
