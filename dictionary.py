 tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

tel['jack']
4098
del tel['sape']
tel['irv'] = 4127
print( tel)
{'guido': 4127, 'irv': 4127, 'jack': 4098}

list(tel.keys())
['irv', 'guido', 'jack']

sorted(tel.keys())
['guido', 'irv', 'jack']

'guido' in tel
True
'jack' not in tel
False

The dict() constructor builds dictionaries directly from sequences of key-value pairs:

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}

Diffrent ways of creating dictionary

{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

------

dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}

-------

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

output:

gallahad the pure
robin the brave

----------

When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

 for i, v in enumerate(['tic', 'tac', 'toe']):
     print(i, v)

Output: 
 
0 tic
1 tac
2 toe

-----

To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))
  
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
