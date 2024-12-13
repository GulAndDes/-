from itertools import product


def find_expression(target):
    digits = "9876543210"
    operators = ["+", "-", ""]

    # Перебираем все комбинации операций
    for ops in product(operators, repeat=(len(digits) - 1)):
        # Формируем выражение, вставляя операторы между цифрами
        expression = "".join(d + o for d, o in zip(digits, ops)) + digits[-1]

        if eval(expression) == target:
            print(f"Найдено выражение: {expression} = {target}")
            return expression

    print("Решение не найдено")
    return None


if __name__ == "__main__":
    target_value = 200
    find_expression(target_value)
