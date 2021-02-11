total = 0
for fizzBuzz_checker in range(1, 101):
    if  fizzBuzz_checker % 3 == 0:
        print('fizz')
    elif fizzBuzz_checker % 5 == 0:
        print('buzz')
    elif fizzBuzz_checker % 3 == 0 and fizzBuzz_checker % 5 == 0 :
            print('fizzbuzz')
    else:
        print(fizzBuzz_checker)