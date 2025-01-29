class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def run(self):
        for statement in self.ast:
            self.execute(statement)

    def execute(self, node):
        if node["type"] == "FunctionDef":
            pass
        elif node["type"] == "Print":
            value = self.evaluate(node["value"])
            print(value)
        elif node["type"] == "Assign":
            value = self.evaluate(node["value"])
            self.variables[node["name"]] = value

    def evaluate(self, node):
        if isinstance(node, int):
            return node
        elif isinstance(node, str):
            return node  # String langsung dikembalikan (untuk print)
        elif isinstance(node, dict):
            if node["type"] == "Variable":
                return self.variables.get(node["name"], 0)  # Ambil nilai dari variabel
            elif node["type"] == "BinaryOp":
                left_value = self.evaluate(node["left"])
                right_value = self.evaluate(node["right"])
                if node["operator"] == "+":
                    return left_value + right_value
                elif node["operator"] == "-":
                    return left_value - right_value
                elif node["operator"] == "*":
                    return left_value * right_value
                elif node["operator"] == "/":
                    return left_value / right_value
        return node  # Jika tidak ada yang cocok, kembalikan nilai asli (mungkin string literal)