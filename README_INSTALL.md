# MimiClaw Installation Guide (Custom Setup)

This guide documents the successful installation steps for MimiClaw on ESP32-S3 using OpenRouter and ESP-IDF 5.5.

## 1. Environment Setup (ESP-IDF)

MimiClaw requires ESP-IDF **v5.5**.

```bash
mkdir -p ~/projects
cd ~/projects
git clone --recursive -b release/v5.5 https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh esp32s3
```

### Permanent Environment Access
Add this line to your `~/.bashrc` or `~/.zshrc`:
```bash
source ~/projects/esp-idf/export.sh
```

## 2. Clone MimiClaw

```bash
cd ~/projects
git clone https://github.com/memovai/mimiclaw.git
cd mimiclaw
```

## 3. Configuration (.env)

MimiClaw uses a `.env` file for credentials. This file is ignored by Git for security.

1. Create your `.env` file from the example:
```bash
cp .env.example .env
```

2. Edit the `.env` file and fill in your secrets (WiFi, API keys, etc.):
```bash
nano .env
```

3. Generate the secrets header:
```bash
python3 scripts/gen_secrets.py
```

This will automatically create/update `main/mimi_secrets.h` with the values from your `.env`.

## 4. Custom Patches for OpenRouter

The original MimiClaw project was patched to support OpenRouter. These changes are already included in this repository:
- `main/mimi_config.h`: Overridable API host/path.
- `main/llm/llm_proxy.c`: Dynamic endpoint selection.
- `main/tools/tool_web_search.c`: Tavily Search integration.

## 5. Build and Flash (The Easy Way)

I've created a script to handle everything for you:

```bash
chmod +x build_and_flash.sh
./build_and_flash.sh
```

This script will:
1. Sync `.env` to `mimi_secrets.h`
2. Load the ESP-IDF environment
3. Build the project
4. Flash to `/dev/ttyUSB0`

## 6. Manual Steps (If needed)

### Build
```bash
. ~/projects/esp-idf/export.sh
idf.py build
```

### Flash
```bash
idf.py -p /dev/ttyUSB0 flash
```

### Monitor
```bash
idf.py -p /dev/ttyUSB0 monitor
```

## 7. How to Update from Original (Upstream)

If the original MimiClaw repository has new updates, you can sync them into your project:

```bash
# 1. Add upstream (if not already added)
git remote add upstream https://github.com/memovai/mimiclaw.git

# 2. Pull updates
git fetch upstream
git merge upstream/main
```

*Note: If merge conflicts occur in `mimi_config.h` or `llm_proxy.c`, keep your OpenRouter patches.*
