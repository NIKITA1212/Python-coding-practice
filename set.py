fruit = {apple,banana,orange,grapes,kiwi,apple,orange,kiwi}

print(fruit)

output:
{apple,banana,orange,grapes,kiwi} # will remove duplicate values

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(b)
output: {'a','l','c','z','m'}
output: {'a', 'r', 'b', 'c', 'd'}

a - b                              # letters in a but not in b
output: {'r', 'd', 'b'}

a | b                              # letters in either a or b
output: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

a & b                              # letters in both a and b
output: {'a', 'c'}

a ^ b                              # letters in a or b but not both
output: {'r', 'd', 'b', 'm', 'z', 'l'}
