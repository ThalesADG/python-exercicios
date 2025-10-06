a, op, b = int(input()), input(), int(input())
c = a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a // b if op == '/' and b != 0 else "Alerta! Alguém tentou usar um operador que não existe. Só um idiota faria isso. Provavelmente o Jim. Isso é claramente uma tentativa de sabotagem corporativa."
print(c)