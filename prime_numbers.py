def number_is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

start = min(a, b)
end = max(a, b)

print(f"Прості числа між {a} і {b}:")
for number in range(start, end + 1):
    if number_is_prime(number):
        print(number)
