'''WAP to check is list contains a palindrome of elements or not

[1,2,3,2,1]
What is a palindrome?


A palindrome is a word, number, or sequence that reads the same forward and backward.

Examples of Palindromes

| Original  | Reverse   | Palindrome? |
| --------- | --------- | ----------- |
| `madam`   | `madam`   | ✅ Yes       |
| `level`   | `level`   | ✅ Yes       |
| `racecar` | `racecar` | ✅ Yes       |
| `noon`    | `noon`    | ✅ Yes       |
| `radar`   | `radar`   | ✅ Yes       |
| `python`  | `nohtyp`  | ❌ No        |
| `apple`   | `elppa`   | ❌ No        |

'''
l2=[1,2,3,4,5,6,7,6,5,4,3,2,1]
a=l2.copy()

a.reverse()
if(a==l2):
    print("Yes, given list is a palindrome")
else:
    print("NO, given list is not a palindrome")

'''
now i wished to take the list input from the user
but the fact is that i will be able to do that only if i learn loops ,
because other wise i need to use append() function and that has a limitation that the code will be hardcoded
to a certain number of elements and we dont know how many elements user want to enter.'''
