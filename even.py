def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


ask = input("give me numbeer")
print(is_even(int(ask)))



def cal_total(list):
    for num in list:
        sum += num
    return sum
print(calc_total(list))

list = [1,2,3,4,5,6,7,8,9]
