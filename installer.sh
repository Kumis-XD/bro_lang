#!/bin/bash

# Cek apakah sedang menggunakan Termux atau Ubuntu
if [ -d "/data/data/com.termux" ]; then
    # Jika di Termux, pindahkan ke /data/data/com.termux/files/usr/bin
    mv bro /data/data/com.termux/files/usr/bin/
    cd
    chmod +x /data/data/com.termux/files/usr/bin/bro
    mv bro_lang /data/data/com.termux/files/usr/bin/
    echo "Setup success now run 'bro your_file.bro'."
else
    # Jika di Ubuntu (atau sistem lain), pindahkan ke /usr/bin
    sudo mv bro /usr/bin/
    cd
    chmod +x /usr/bin/bro
    sudo mv bro_lang /usr/bin/
    echo "Setup success now run 'bro your_file.bro'."
fi
