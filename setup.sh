#!/bin/bash

# Dapatkan path dari script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Tentukan target directory berdasarkan sistem
if [ -d "/data/data/com.termux" ]; then
    TARGET_DIR="/data/data/com.termux/files/usr/bin"
else
    TARGET_DIR="/usr/bin"
fi

# Pindahkan file `bro` jika ada
if [ -f "$SCRIPT_DIR/bro" ]; then
    mv "$SCRIPT_DIR/bro" "$TARGET_DIR/"
    chmod +x "$TARGET_DIR/bro"
else
    echo "Warning: File 'bro' tidak ditemukan di $SCRIPT_DIR!"
fi

# Pindahkan folder `bro_lang` jika ada
if [ -d "$SCRIPT_DIR/bro_lang" ]; then
    rm -rf "$TARGET_DIR/bro_lang"
    mv "$SCRIPT_DIR/bro_lang" "$TARGET_DIR/"
else
    echo "Warning: Folder 'bro_lang' tidak ditemukan di $SCRIPT_DIR!"
fi

echo "Setup success! Now run 'bro your_file.bro'."
