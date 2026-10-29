import timeit

def merge_sorted_list(list1, list2):
    i, j = 0, 0
    merged_list = []

    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:            
            merged_list.append(list1[i])   
            i += 1
        else:
            merged_list.append(list2[j])   
            j += 1

    
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list


l1 = [10, 20, 30, 40, 50, 55]
l2 = [10, 40, 50, 60, 70, 80]
print("list1 :",l1)
print("print :", l2)

print((merge_sorted_list(l1, l2)))