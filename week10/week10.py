# --------- Exercise 1 -------------- #

# myList = [76,92.3,"hello",True,4,76]
# myList.append("apple")
# myList.append(76)
# myList.insert(3,"cat")
# myList.insert(3,99)
# print(myList.index("hello"))
# print(myList.count(76))
# myList.remove(76)
# myList.pop(myList.index(True))
# print(myList)

# --------- Exercise 2 -------------- #

# def sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total = total + number**2
#     return total
# my_list = [3,4,5]
# print(sum_of_squares(my_list))

# --------- Exercise 3 -------------- #
#
# def sum_evens(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             sum += number
#     return sum
# my_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_List))


# --------- Exercise 4 -------------- #

# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
# my_list = [ 'apple','cat','lemon','python','tiger']
# print(count_five_letter(my_list))


# --------- Exercise 5 -------------- #

# def sum_until_even(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             break
#         sum += number
#     return sum
# my_list= [1,3,3,7,5,6]
# print(sum_until_even(my_list))


# --------- Exercise 6 -------------- #

# def count_until_sam(words):
#     count =0
#     for word in words:
#         count = count +1
#         if word == 'sam':
#          break
#     return count
# my_List = ["joe","ali","veli","sam","sami"]
# print(count_until_sam(my_List))



# --------- Exercise 7 -------------- #

# def replace (s,old,new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test (actual,expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# test(replace('Mississippi','i', 'I'),'MIssIssIppI')

# --------- Exercise 8 -------------- #

# def find_max_val_in_list(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# print(find_max_val_in_list([1,2,3,4,5,6,7,8,9,10]))
# print(find_max_val_in_list([-34, -35, -60, -5]))
























