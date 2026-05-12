#8. Write a program to create a duplicate of an existing list. It should not point to
#same list.

original = [10, 20, 30, 40]

duplicate = original.copy()

print("Original list:", original)
print("Duplicate list:", duplicate)

print("Same object?", original is duplicate)