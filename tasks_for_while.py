# для заданної кількості ітерацій
# for i in щось:
#   дія

# for i in range(5):
#     print(i, end=", ")

# for i in "string":
#     print(i, end=" ")
#     print(1, end=" ")

# n = 10
# while n > 0:
#     print(1, end=" ")
#     n -= 1

# n = 10
# while n > 0:
#     if n % 2 == 0:
#         n -= 1
#         continue
#     elif n == 3:
#         break
#     print(n, end=" ")
#     n -= 

n = int(input())
p1 = "  __  "
p2 = "(o  o)"
p3 = "(    )"

print(p1 * n)
print(p2 * n)
print(p3 * n)

nums = "123456789"[:5]