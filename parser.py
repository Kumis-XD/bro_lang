class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        token = self.peek()
        self.pos += 1
        return token

    def parse(self):
        ast = []
        while self.peek():
            ast.append(self.parse_statement())
        return ast

    def parse_statement(self):
        token_type, value = self.consume()

        if token_type == "DEF":
            return self.parse_function()
        elif token_type == "PRINT":
            return self.parse_print()
        elif token_type == "IDENTIFIER":
            if self.peek() and self.peek()[0] == "ASSIGN":
                return self.parse_assign(value)
            elif self.peek() and self.peek()[0] == "PAREN_OPEN":
                return self.parse_function_call(value)

        raise SyntaxError(f"Token tidak dikenal: {value}")

    def parse_function(self):
        name = self.consume()[1]  # Ambil nama fungsi
        self.consume()  # PAREN_OPEN '('
        self.consume()  # PAREN_CLOSE ')'
        self.consume()  # COLON ':'

        body = []
        while self.peek() and self.peek()[0] not in ["DEF", "IDENTIFIER", "PRINT"]:
            body.append(self.parse_statement())

        return {"type": "FunctionDef", "name": name, "body": body}

    def parse_print(self):
        self.consume()  # PAREN_OPEN '('
        expr = self.parse_expression()  # Sekarang bisa membaca ekspresi
        self.consume()  # PAREN_CLOSE ')'
        return {"type": "Print", "value": expr}

    def parse_assign(self, name):
        self.consume()  # ASSIGN "="
        value = self.parse_expression()  # Sekarang bisa membaca ekspresi
        return {"type": "Assign", "name": name, "value": value}

    def parse_function_call(self, name):
        self.consume()  # PAREN_OPEN '('
        self.consume()  # PAREN_CLOSE ')'
        return {"type": "FunctionCall", "name": name}

    def parse_expression(self):
        # Mulai dengan nilai pertama
        left_type, left_value = self.consume()

        # Cek apakah ini adalah angka atau identifier
        if left_type == "NUMBER":
            left_value = int(left_value)
        elif left_type == "STRING":
            left_value = left_value.strip('"')
        elif left_type == "IDENTIFIER":
            # Jika ini identifier, ambil nilainya dari variabel yang sudah didefinisikan
            left_value = {"type": "Variable", "name": left_value}
        else:
            raise SyntaxError(f"Ekspresi tidak valid: {left_value}")

        # Cek operator dan ekspresi berikutnya
        while self.peek() and self.peek()[0] in ["PLUS", "MINUS", "MULT", "DIV"]:
            op_type, op_value = self.consume()
            right_type, right_value = self.consume()

            if right_type == "NUMBER":
                right_value = int(right_value)
            elif right_type == "STRING":
                right_value = right_value.strip('"')
            elif right_type == "IDENTIFIER":
                right_value = {"type": "Variable", "name": right_value}
            else:
                raise SyntaxError(f"Ekspresi tidak valid: {right_value}")

            left_value = {"type": "BinaryOp", "operator": op_value, "left": left_value, "right": right_value}

        return left_value