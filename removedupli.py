def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [6, 4, 10, 10, 3, 2, 20, 4]
print(remove(duplicate))