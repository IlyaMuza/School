def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, int(result**0.5)+1):
            if result % i == 0:
                return 'Составное'
        return 'Простое'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

res = sum_three(2,1,8)
print(res)