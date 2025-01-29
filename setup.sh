#!/bin/bash

# Dapatkan path dari script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Tentukan target directory berdasarkan sistem
if [ -d "/data/data/com.termux" ]; then
    TARGET_DIR="/data/data/com.termux/files/usr/bin"
else
    TARGET_DIR="/usr/bin"
fi

# Pindah ke parent directory terlebih dahulu
cd "$PARENT_DIR"

# Pastikan folder script masih ada sebelum memindahkan
if [ -d "$SCRIPT_DIR" ]; then
    # Hapus folder yang lama jika ada
    rm -rf "$TARGET_DIR/$(basename "$SCRIPT_DIR")"
    
    # Pindahkan folder script ke target directory
    mv "$SCRIPT_DIR" "$TARGET_DIR/"

    echo "Setup success! Folder telah dipindahkan ke $TARGET_DIR"
else
    echo "Error: Folder source tidak ditemukan!"
    exit 1
fi
