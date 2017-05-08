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
