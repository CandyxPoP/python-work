# def factorial(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact =  fact * i
#     return fact

# fact_of_5 = factorial(5)
# fact_of_10 = factorial(10)

# print (fact_of_5)
# print (fact_of_10)

# def merafunction(n):
#     total=0
#     for i in n :
#         total+=ord(i)
#     return total
# print(merafunction('lovjeet'))

# def generate_passwd(usrname,passwd):
#     name=usrname[:4]
#     passwrd=passwd[-4:]
#     return name+passwrd
# print(generate_passwd('push','12345))



def even_(val):
    for i in val:
        if i%2==0:
            print(i)
even_([1,2,3,4,77,44,22,55,33,226])            