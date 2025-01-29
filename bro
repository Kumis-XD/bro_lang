#!/usr/bin/env python3
import sys
import os

# Menambahkan direktori 'bro_lang' ke PYTHONPATH agar modul dapat diimpor
sys.path.append('/data/data/com.termux/files/home/usr/bin/bro_lang')

from bro_interpreter import main

if __name__ == "__main__":
    main()
