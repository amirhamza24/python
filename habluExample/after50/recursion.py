# def my_rec():
#     print("Recursion")
#     my_rec()
#
# my_rec()


# factorial series using recursion
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)


n = 5
result = fact_rec(n)
print(f"The factorial of {n} is {result}")