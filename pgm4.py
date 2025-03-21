n = int(input("Enter the number of terms in Fibonacci series: "))


a, b = 0, 1


if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci series up to {n} term: {a}")
else:
    print("Fibonacci series:")
    print(a, b, end=" ")

    
    for _ in range(2, n):
        next_term = a + b
        print(next_term, end=" ")
        a, b = b, next_term
