squares = [x**2 for x in range(10)]

Is same as 

squares = []
for x in range(10):
squares.append(x**2)


----------
combine two list into tuple

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

is similar to

combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
              combs.append((x, y))

------------------
combine nested list into one list 

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
