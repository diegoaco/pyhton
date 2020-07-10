# Converts a Roman numeral into a number

def roman(s):
    roman_dict = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M':1000}
    n = roman_dict[s[-1]]
    
    for i in range(len(s)-1, 0, -1):
        if roman_dict[s[i]] <= roman_dict[s[i-1]]:
            n = n + roman_dict[s[i-1]]
        else:
            n = n - roman_dict[s[i-1]]
    return n

print(roman('DCCCXXVI'))
