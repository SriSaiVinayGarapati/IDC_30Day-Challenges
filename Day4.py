def is_prime(number):
    if number <= 1:
        print(f'{number} is not a prime number')
    else:
        for i in range(2 , number):
            if number % i == 0:
                print(f'{number} is not a prime number')
                return
        print(f'{number} is a prime number')

#testing with various user inputs....
test_set = list(map(int , input("Enter the test set numbers : ").split()))
for i in test_set:
    is_prime(i)
