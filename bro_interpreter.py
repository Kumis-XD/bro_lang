import sys
from lexer import lexer  # Memastikan lexer sudah ada dan fungsi lexer berjalan dengan baik
from parser import Parser  # Pastikan kelas Parser sudah benar
from interpreter import Interpreter  # Pastikan kelas Interpreter sudah benar

def main():
    if len(sys.argv) < 2:
        print("Gunakan: python bro_interpreter.py nama_file.bro")
        return

    try:
        with open(sys.argv[1], "r") as file:
            code = file.read()
            tokens = lexer(code)  # Tokenisasi kode dengan lexer
            parser = Parser(tokens)  # Parsing token menggunakan Parser
            ast = parser.parse()  # Dapatkan AST (Abstract Syntax Tree)
            interpreter = Interpreter(ast)  # Eksekusi AST dengan Interpreter
            interpreter.run()  # Menjalankan interpreter
    except FileNotFoundError:
        print(f"File {sys.argv[1]} tidak ditemukan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()