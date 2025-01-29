import re

# Token map dengan bahasa gaul Indonesia
TOKEN_MAP = {
    "bikin": "DEF",          # Fungsi
    "cetak": "PRINT",        # Print / Cetak
    "kalo": "IF",            # If statement
    "gaes": "ELSE",          # Else statement
    "selama": "WHILE",       # While loop
    "buat": "FOR",           # For loop
    "balikin": "RETURN",     # Return statement
    "skip": "PASS",          # Pass (melewatkan blok kode)
    "lanjut": "CONTINUE",    # Continue (lanjutkan iterasi berikutnya)
    "berenti": "BREAK",      # Break (keluar dari loop)
    "nunggu": "AWAIT",       # Await (untuk async)
    "janji": "ASYNC",        # Async (fungsi asinkron)
    "cuy": "CLASS",          # Class (untuk membuat kelas)
    "selfie": "SELF",        # Self (dalam OOP)
    "superior": "SUPER",     # Super (memanggil parent class)
    "ambil": "YIELD",        # Yield (generator)
    "bener": "TRUE",         # Boolean true
    "salah": "FALSE",        # Boolean false
    "kosong": "NONE",        # Null atau None
    "lempar": "RAISE",       # Raise (lempar exception)
    "tangkep": "TRY",        # Try (blok percobaan)
    "kecuali": "EXCEPT",     # Except (penanganan error)
    "akhirnya": "FINALLY",   # Finally (blok yang selalu dieksekusi)
    "impor": "IMPORT",       # Import (mengimpor modul)
    "dari": "FROM",          # Dari (import dari modul)
    "sebagai": "AS",         # As (alias)
    "hapus": "DEL",          # Del (menghapus variabel atau objek)
    "global": "GLOBAL",      # Global (deklarasi variabel global)
    "nonlokal": "NONLOCAL",  # Nonlocal (mengakses variabel dari luar scope)
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
}

def lexer(code):
    tokens = []
    # Mencocokkan semua kata, string, dan tanda baca
    words = re.findall(r'"[^"]*"|\w+|[^\w\s]', code)  # Menangani string dan kata serta tanda baca

    for word in words:
        if word in TOKEN_MAP:
            token_type = TOKEN_MAP[word]  # Menggunakan token yang sudah dipetakan
        elif word.isidentifier():  # Mengidentifikasi kata sebagai variabel atau fungsi
            token_type = "IDENTIFIER"
        elif word.isdigit():  # Mengidentifikasi angka
            token_type = "NUMBER"
        elif word.startswith('"') and word.endswith('"'):  # Mengidentifikasi string
            token_type = "STRING"
        else:
            token_type = "UNKNOWN"  # Untuk token yang tidak diketahui (jika ada)
        
        # Menambahkan token ke dalam daftar
        tokens.append((token_type, word))
    
    return tokens
