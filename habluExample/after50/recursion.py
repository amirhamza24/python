# recursion declaration
# def my_rec():
#     print("Recursion")  # this print printed 995+- times.. cause recursion er limits 1000 er ektu kom (995+-)
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
