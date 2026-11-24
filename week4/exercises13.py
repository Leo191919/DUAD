#FizzBuzz

number:0
divisible_by_3 = "Fizz"
divisible_by_5 = "Buzz"
divisible_final = divisible_by_3 + divisible_by_5

number= float(input("Please, enter the number: "))

if number%3==0 and number%5 ==0:
    print(divisible_final)
elif number % 3 ==0  :

    print(divisible_by_3)
elif number % 5 ==0 :
    print(divisible_by_5)