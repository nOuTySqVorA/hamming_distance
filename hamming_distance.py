
def hamming_distance(bStrOne,bStrTwo):
    # check if two strings have the same length
    if len(bStrOne) != len(bStrTwo):
        print('Hamming distance method intends the equal length of two strings. The length of introduced strings {0} and {1} are not equal'.format(bStrOne, bStrTwo))
    else:
        return len(list(k for k in range(len(bStrOne)) if bStrOne[k] != bStrTwo[k]))
        
str1 = "abcde"
str2 = "bcdef"
str3 = "strong"
str4 = "strung"
str5 = "ABBA"
str6 = "abba"

print(hamming_distance(str1,str2))
print(hamming_distance(str1,str1))
print(hamming_distance(str3,str4))
print(hamming_distance(str5,str6))

