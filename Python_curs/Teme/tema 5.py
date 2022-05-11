# 1. Print first 10 natural numbers using while loop
# i = 1
# while i<11:
#     print(i)
#     i +=1

#2.  writhe a program to print the following number pattern using a loop
# 1
# 12
# 123
# 1234
# 12345
# i = int(input('alege un nr'))   # numara pana la 5
# for i in range(1, i+1,1):   #porneste de la 1 si pe urma aduna 1+1 si se opreste/ repeta operatiunea de cate ori este i
#     for x in range(1,i+1):
#         print(x,end='')
#     print('')               # empty line after each row

# Calculate the sum of all numbers from 1 to a given number
# numar = int(input('Alege un numar'))
# sum = 0
# for i in range(1,numar+1):
#     sum +=i
# print(f'suma este {sum}')

#4: Write a program to print multiplication table of a given number
# nr = int(input('alege un nr'))
# for numere in range(1,11,1): # la prima rulare numere = nr ales si il printeaza
#     m = nr*numere            # m = nr ales * numere si la fiecare rulare numere = nr ales* numere
#     print(m)                #printul se face in interiorului for
#sau
# nr= 8
# for i in range(1,20,2): # ruleaza de la primul nr-8 de 19 ori din 2 in 2 pasi-adica afiseaza pasul 1-8, pasul 3 8+8+8 si tot asa
#     mult = nr*i
#     print(mult)


#5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for numere in numbers:
#     if numere>500:
#         break
#     elif numere > 150:
#         continue
#     elif numere % 5 ==0:
#         print(numere)

#
# 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.
# nr = 12345678910
# count = 0
# while nr !=0:
#     nr = nr//10 # se imparte la 10 pentru a elimia cate o cifra de la caoada la cap, daca trecem 2 atunci nr se imparte la 2 de fiecare data cand ruleaza
#     count = count+1
# print(count)




# 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# nr = 5    # cate coloane sa faca+1
# rep = 5    # pana la cat sa numere in prima coloana-1 sau de la cat sa numere-1
# for i in range(0,nr+1,1):
#     for x in range(rep-i,0,-1):
#         print(x, end='')
#     print('')



# 8: Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])

# 9: Display numbers from -10 to -1 using for loop
# Expected output:
#
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
# for i in range(-10,0,1):
#     print(i)

# 10: Use else block to display a message “Done” after successful execution of for loop
#Given:

# for i in range(5):
#     print(i)
# else:
#     print("Done!")
# Expected output:
#
# 0
# 1
# 2
# 3
# 4
# Done!



#11: Write a program to display all prime numbers within a range
# start = 25
# end = 50
# Expected output:
#
# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47
# for numar in range(25,50+1):
#     if numar>1:
#         for i in range(2,numar): # nu inteleg de ce 'i' ia valori aleatorii si nu  de la 2 la valoarea numarului
#             if numar%i ==0:
#                 break
#         else:
#             print(numar)

#12: Display Fibonacci series up to 10 terms
# firtNum = 0
# secNum = 1
# for i in range(10):
#     print(firtNum,end='')
#     rez = firtNum+secNum
#     firtNum = secNum
#     secNum = rez



#13: Find the factorial of a given number
# number = int(input('Alege numarul'))
# fact = 1
# if number < 0:
#     print('Factorial number does not exist for negativ numbers')
# elif number ==0:
#     print('Factorial number of 0 is 1')
# else:
#     number>0
#     for i in range(1,number+1):
#         fact = fact*i
#     print(f'Factorial number of {number} si {fact}')


# 14: Reverse a given integer number
# number = 76542
# revNum = 0
# while number>0:
#     num2 = number % 10
#     revNum = (revNum*10)+num2
#     number= number//10
# print(revNum)



# nr= 56987
# while nr>0:
#     rev = nr%10   #ii atribuim lui rev prima cifra din noul numar(in cazul nostru este 7)
#     nr = nr//10    #noul numar care va fi rulat este fara ultima cifra, si tot asa pana se termina
#     print(rev,end='')

# numar = 9876543210
# while numar>0:
#     numar2 = numar%10
#     numar = numar//10
#     print(numar2,end='')


# 15: Use a loop to display elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for number in my_list:
#     if (number// 10) % 2 != 0:
#         continue
#     else:
#         print(number, end=' ')


#16: Calculate the cube of all numbers from 1 to a given number
# number = int(input('Alege un nr pt a afla cubul'))
# for i in range(1,number+1,1):
#     cub = i*i*i
#     print(f' For number {i}, cube is {cub}')



#18: Print the following pattern
# repetari = 5
# for i in range(0,repetari):
#     for x in range(0,i+1):
#         print('*',end='')
#     print('')
# for i in range(repetari,0,-1):
#     for x in range(0,i-1):
#         print('*',end='')
#     print('')


#1: Print First 10 natural numbers using while loop
# a = 1
# while a<=10:
#   print(a)
#   a +=1

# x = 5
# while x <=20:
#     print(x, end=' ')
#     x +=1


# 2: Print the following pattern
# Write a program to print the following number pattern using a loop.
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# a = 5
# b = 5
# for i in range(1,a+1):
#     for x in range(1,i+1,1):
#         print(x,end='')
#     print('')


# # 3: Calculate the sum of all numbers from 1 to a given number
# givenum = int(input('alege nr'))
# sum = 0
# for i in range(1,givenum+1):
#     sum +=i
# print(sum,end='')
