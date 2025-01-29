#!/bin/bash

# Cek apakah menggunakan Termux atau Ubuntu/Linux lainnya
if [ -d "/data/data/com.termux" ]; then
    # Jika di Termux, tentukan direktori tujuan
    TARGET_DIR="/data/data/com.termux/files/usr/bin"
    OS_NAME="Termux"
elif [ -f "/etc/os-release" ]; then
    # Jika di sistem Linux, cek apakah itu Ubuntu atau distro lainnya
    . /etc/os-release
    if [ "$NAME" == "Ubuntu" ]; then
        TARGET_DIR="/usr/bin"
        OS_NAME="Ubuntu"
    else
        TARGET_DIR="/usr/bin"
        OS_NAME="$NAME"
    fi
else
    # Jika OS tidak dikenali
    echo "Unknown operating system"
    exit 1
fi

# Cek apakah direktori tujuan ada
if [ -d "$TARGET_DIR" ]; then
    # Pindahkan file `bro` ke direktori tujuan
    mv bro "$TARGET_DIR/"
    chmod +x "$TARGET_DIR/bro"
    sleep 2
    # Pindahkan folder `bro_lang` ke direktori tujuan
    cd $HOME
    mv bro_lang "$TARGET_DIR/"
    echo "Setup success on $OS_NAME! Now run 'bro your_file.bro'."
else
    echo "Error: Target directory $TARGET_DIR does not exist!"
    exit 1
fi
