#!/usr/bin/env python3
import os
import sys


def main():
    env_file = ".env"
    output_file = "main/mimi_secrets.h"

    if not os.path.exists(env_file):
        print(f"Error: {env_file} not found.")
        sys.exit(1)

    secrets = {}
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                secrets[key.strip()] = value.strip().strip('"').strip("'")

    content = [
        "#pragma once",
        "",
        "/* Generated from .env by scripts/gen_secrets.py */",
        "",
        "/* WiFi */",
        f'#define MIMI_SECRET_WIFI_SSID       "{secrets.get("WIFI_SSID", "")}"',
        f'#define MIMI_SECRET_WIFI_PASS       "{secrets.get("WIFI_PASS", "")}"',
        "",
        "/* Telegram Bot */",
        f'#define MIMI_SECRET_TG_TOKEN        "{secrets.get("TG_TOKEN", "")}"',
        "",
        "/* LLM */",
        f'#define MIMI_SECRET_API_KEY         "{secrets.get("API_KEY", "")}"',
        f'#define MIMI_SECRET_MODEL           "{secrets.get("MODEL", "minimax/minimax-m2.5")}"',
        f'#define MIMI_SECRET_MODEL_PROVIDER  "{secrets.get("MODEL_PROVIDER", "openai")}"',
        "",
        "/* Overrides */",
    ]

    if "OPENAI_API_URL" in secrets:
        content.append(
            f'#define MIMI_OPENAI_API_URL         "{secrets["OPENAI_API_URL"]}"'
        )
    if "OPENAI_API_HOST" in secrets:
        content.append(
            f'#define MIMI_OPENAI_API_HOST        "{secrets["OPENAI_API_HOST"]}"'
        )
    if "OPENAI_API_PATH" in secrets:
        content.append(
            f'#define MIMI_OPENAI_API_PATH        "{secrets["OPENAI_API_PATH"]}"'
        )

    with open(output_file, "w") as f:
        f.write("\n".join(content) + "\n")

    print(f"Successfully generated {output_file}")


if __name__ == "__main__":
    main()
