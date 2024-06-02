# ASS no 1

# a = int(input('Enter a number: '))
# b = int(input('Enter another number: '))
# c = int(input('Enter last number: '))

# def max_number(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c

# max = (max_number(a, b, c))
# print("maximum number:", max)

# ASS no 2

# sample_list=(8, 2, 3, 0, 7)
# def sum(a,b,c,d,e):
#     total = a+b+c+d+e
#     return total
# print(sum(8,2,3,0,7))


# ASS no 3

# multiply = 1
# sample_list=(8, 2, 3, -1, 7)
# for i in sample_list:
#      multiply *= i
    
# print("Multiply =", multiply)


# ASS no 4

# sample_string= "1234abcd"
# def reverse(s_string):
#      return s_string[::-1]
# string_output = reverse(sample_string)
# print(string_output)



# ASS no 5

# def fact(n):
#      if n<0:
#           return "Not possible for this number"
#      elif n == 0:
#         return 1
#      else:
#           output = 1
#           for i in range(1, n + 1):
#                output *= i
#                print(output)
#           return output
        

# factorial = int(input("Find factorial of: "))
# print(factorial,"! =", fact(factorial) )



# ASS no 6

# def range_check(actual,range_start,range_end):
#      return range_start <= actual <= range_end

# actual_num = int(input("Is this number in range of below numbers?= "))
# start_num = int(input("From: "))
# end_num = int(input("To= "))

# if range_check(actual_num, start_num, end_num):
#      print(actual_num, "is in range")
# else:
#      print(actual_num, "not in range")


# ASS no 7

# sample_string = "The quick Brow Fox"

# def accept_count(string):
#     upper_case = 0
#     lower_case = 0
#     for i in string:
#         if i.isupper():
#             upper_case += 1
#         elif i.islower():
#             lower_case += 1
#     return lower_case, upper_case
        
# lower_case, upper_case = accept_count(sample_string)

# print("No of UpperCase: ", upper_case)
# print("No of LowerCase: ", lower_case)


# ASS no 8

# sample_lst = [1,2,3,3,3,3,4,5]
# new_lst = []

# for distinct_elements in sample_lst:
#     if distinct_elements not in new_lst:
#         new_lst.append(distinct_elements)
#     print(new_lst)


#ASS no 9


# def is_it_prime(n):
#     if n <= 1:
#         return False
#     elif n<= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False 
#         i += 6
#     return True
    
# prime_number = int(input("Confirm if it's prime number: "))  

# if is_it_prime(prime_number):
#         print(prime_number, "Is a Prime Number")
# else:
#         print(prime_number, "Is Not a Prime Number")


# ASS no 10

def even_num(n):
  even_set = []
  for i in n:
    if i % 2 == 0:
      even_set.append(i)
    
  return even_set
sample_list = [1,2,3,4,5,6,7,8,9]    
even_set = even_num(sample_list)
print(even_set)

     