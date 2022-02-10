from itertools import count
num = int(input("Enter 4 digit number :"))
def num_to_list(x):
    #n = int(input("Enter 4 digit number: "))
    return [x for x in str(x)]
#print(number_array(n))
def sort_list(l, reverse=False):
    return sorted(l, reverse=reverse)
#print(reverse_array(n))
def run_kaprekar_step(n):
    number = num_to_list(n)
    asc = sort_list(number)
    desc = sort_list(number, True)
    smallest = int("".join(asc))
    largest = int("".join(desc))
    return largest-smallest
def k_number(n):
    count = 0       
    while True:
        if n == 0:
            return None
        if n == 6174:
            break
        else:
            count += 1
        n = run_kaprekar_step(n)
    return count
print("Your step count is: ", k_number(num))
