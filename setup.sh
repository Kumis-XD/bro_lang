#!/bin/bash

# Cek apakah menggunakan Termux atau Ubuntu
if [ -d "/data/data/com.termux" ]; then
    # Jika di Termux, tentukan direktori tujuan
    TARGET_DIR="/data/data/com.termux/files/usr/bin"
else
    # Jika di Ubuntu, tentukan direktori tujuan
    TARGET_DIR="/usr/bin"
fi

# Cek apakah direktori tujuan ada
if [ -d "$TARGET_DIR" ]; then
    # Pindahkan file `bro` ke direktori tujuan
    mv bro "$TARGET_DIR/"
    chmod +x /data/data/com.termux/files/usr/bin/bro
    sleep 2
    # Pindahkan folder `bro_lang` ke direktori tujuan
    mv bro_lang "$TARGET_DIR/"
    echo "Setup success! Now run 'bro your_file.bro'."
else
    echo "Error: Target directory $TARGET_DIR does not exist!"
    exit 1
fi
