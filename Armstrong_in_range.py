def armstrong_in_range(start,end):
    result = []
    for num in range(start,end+1):
        digits = str(num)
        k = len(digits)


        total= sum(int(d)**k for d in digits)
        if total == num:
         result.append(num)

    return result

nums=armstrong_in_range(100,500)
print(nums)

    

