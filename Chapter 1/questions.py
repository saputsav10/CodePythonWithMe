#Question1
# a = [[1, 2]] * 3
# a[0][0] = 9
# print(a)
# # Explain the output

a=[[1,2],[1,2],[1,2]]
a[0][0]=9
print(a) #it should give the output as a[[9,2],[1,2],[1,2]]

#Question2
#nested = [[1, 2], [3, 4, [5, 6]], 7]
# Write a function to flatten it into [1, 2, 3, 4, 5, 6, 7]

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [[1, 2], [3, 4, [5, 6]], 7]
print(flatten(nested))





