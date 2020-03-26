
def isPalindrome(number_string):
    reverse_string = number_string[::-1]
    for x in range(len(number_string)):
        if number_string[x] != reverse_string[x]:
            return False
    return True


largest_palindrome = 0
string_factors = ""
n = 100
for x in range(100,999):
    for y in range(n,999):
        s = str(x*y)
        if isPalindrome(s):
            if x*y >= int(largest_palindrome):
                string_factors = str(x) + " " + str(y)
                largest_palindrome = s
    n+=1

print(string_factors)
print(largest_palindrome)
