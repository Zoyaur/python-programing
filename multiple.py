def fizzBuzz(number):
    multiple_three =[3, 6, 9, 12, 15, 18 , 21, 24, 27, 30]
    multiple_five  =  [5 , 10 , 15, 20 , 25 ,30, 35 ,40 , 45,50]
    len1=len(multiple_three)
    

    for i in range(1, 16):
     if i in multiple_five and multiple_three:
        print("fizzbuzz")
     elif i % 3 == 0:
        print("fizz")
     elif i % 5 == 0:
        print("buzz")
     else:
        print(i)

    


fizzBuzz(50)
