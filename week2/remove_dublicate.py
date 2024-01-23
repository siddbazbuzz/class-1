original_list = [1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 8, 9]


unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)


print("Original List:", original_list)
print("List after removing duplicates:", unique_list)