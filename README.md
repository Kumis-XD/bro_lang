# bro_lang

bro_lang adalah bahasa pemrograman dengan sintaks bahasa gaul Indonesia.

## Cara Menggunakan

### Instalasi:
Untuk menggunakan **bro_lang**, Anda bisa mengunduh kode sumber dari repositori ini dan menjalankannya di perangkat Anda.

1. **Clone repositori:**
   
   Jika Anda memiliki Git, jalankan perintah berikut di terminal untuk meng-clone repositori:

   ```bash
   git clone https://github.com/username/bro_lang.git
   cd bro_lang
   chmod +x setup.sh
   ./setup.sh

### TOKEN_MAP

```python
TOKEN_MAP = {
    "bikin": "DEF",          # Fungsi
    "cetak": "PRINT",        # Print / Cetak
    "kalo": "IF",            # If statement
    "gaes": "ELSE",          # Else statement
    "selama": "WHILE",       # While loop
    "buat": "FOR",           # For loop
    "balikin": "RETURN",     # Return statement
    "=": "ASSIGN",           # Penugasan
    "+": "PLUS",             # Penambahan
    "-": "MINUS",            # Pengurangan
    "*": "MULT",             # Perkalian
    "/": "DIV",              # Pembagian
    "%": "MOD",              # Modulus
    "**": "POW",             # Pemangkatan
    "(": "PAREN_OPEN",       # Kurung buka
    ")": "PAREN_CLOSE",      # Kurung tutup
    ":": "COLON",            # Titik dua
    ",": "COMMA",            # Koma
    ".": "DOT",              # Titik untuk akses method
    ";": "SEMICOLON",        # Titik koma (untuk akhir statement)
    "==": "EQUALS",          # Pengecekan kesamaan
    "!=": "NOTEQUALS",       # Pengecekan ketidaksamaan
    "<": "LESS",             # Lebih kecil
    ">": "GREATER",          # Lebih besar
    "<=": "LESS_EQUAL",      # Lebih kecil atau sama dengan
    ">=": "GREATER_EQUAL",   # Lebih besar atau sama dengan
    "dan": "AND",            # Operator logika AND
    "atau": "OR",            # Operator logika OR
    "tidak": "NOT",          # Operator logika NOT
    "bener": "TRUE",         # Boolean true
    "salah": "FALSE",        # Boolean false
    "kosong": "NONE",        # Null atau None
    "import": "IMPORT",      # Import
    "dari": "FROM",          # Dari untuk import
}
