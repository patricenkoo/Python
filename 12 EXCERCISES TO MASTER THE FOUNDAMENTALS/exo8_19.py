#Write a function called count_capital_consonants. This
#function should take as input a string, and return as output
#a single integer. The number the function returns should be
#the count of characters from the string that were capital
#consonants. For this problem, consider Y a consonant.
#
#For example:
#
# count_capital_consonants("Georgia Tech") -> 2
# count_capital_consonants("GEORGIA TECH") -> 6
# count_capital_consonants("gEOrgIA tEch") -> 0


#Write your function here!
def count_capital_consonants(a_string):
    result = 0
    index = 0
    vowels = [a,e,u,i,o]
    for char in a_string:
        if char not in vowels[index] and ord(char) > 65:
            result += 1
            index += 1
    return result     
                                                 

#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.
print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))