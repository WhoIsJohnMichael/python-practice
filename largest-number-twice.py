number = int(input("Enter the number of integers: "))
dominant_index = -1
max_num = 0

print("Enter the integers: ")

for i in range(number):
    entered_num = int(input())
    if entered_num >= (max_num * 2):
        max_num = entered_num
        dominant_index = i
    elif max_num >=  (entered_num * 2):
        dominant_index = dominant_index
    else:
        max_num = entered_num
        dominant_index = -1
print('Dominant Index:', dominant_index)
