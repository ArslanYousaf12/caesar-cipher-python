#Write your code below this line 👇
def prime_checker(number):
    for num in range(1, number):
        if num == number or num == 1:
            continue
        if number % num == 0:
            print(f'Its not a prime number its divisible by {num}')
            return
    print("Its a prime number")
        
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



