#Task 9: Prime Number 
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True


print(is_prime(7))
print(is_prime(10))


#Task 10: Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


n = 1234
print(f"The sum of digits in (n) is {sum_of_digits(n)}")


#Task 11: LCM and GCD
import math 
def lcm_gcd(a,b):
    gcd = math.gcd(a,b)
    lcm = (a * b) // gcd
    return lcm, gcd


print(lcm_gcd(12, 18))
print(lcm_gcd(7, 5))


#Task 12: List Reversal
def reverse_list(lst):
    return lst[::-1]


print(reverse_list([1,2,3,4]))
print(reverse_list([7,8,9]))


#Task 13: Sort a List
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


print(bubble_sort([5, 3, 8, 1, 2]))



#Task 14: Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))


print(remove_duplicates([1, 2, 2 , 3, 4, 4, 5]))


#Task 15:String length
def string_length(s):
    count = 0 
    for _ in s:
        count +=1
    return count


print(string_length("HelloWorld"))
print(string_length("Python"))



#Task 16: Count Vowels and Consonants
def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v_count, c_count = 0, 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count +=1
            else:
                 c_count +=1

    return v_count, c_count


s = "hello world"
vowels, consonants = count_vowels_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")
