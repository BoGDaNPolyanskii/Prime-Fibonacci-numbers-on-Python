def fib(k):
    # перевірка введеного числа
    if k <= 0:
        raise ValueError("Помилка, число k має бути більше 0.") # виведення помилки

    # база рекурсії
    if k == 1:
        return [0]
    elif k == 2:
        return [0, 1]
    else:
        fib_sequence = fib(k - 1)
        # додавання наступного числа Фібоначчі
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) # додавання 2 останніх чисел Фібоначчі для отримання нового
        return fib_sequence


def main():
    try:
        k = input("Введіть кількість чисел Фібоначчі: ")
        if not k.isdigit():
            raise ValueError("Помилка, було введено не число.")
        k = int(k)
        fibonacci_numbers = fib(k)
        print(f"Перші {k} чисел Фібоначчі: {fibonacci_numbers}")
    except ValueError as e:
        print(f"Помилка: {e}")

main()