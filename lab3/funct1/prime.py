def filter_prime(my_list):
    prime_list = []
    for i in my_list:
        cnt = 0
        if i == 2:
            prime_list.append(i)
            continue
        elif i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            prime_list.append(i)
    return prime_list

my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))


print(filter_prime(my_list))
