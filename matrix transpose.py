
p = [[row[i] for row in matrix] for i in range(len(matrix))]
print(p)

output: 
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

--------------------------------------------------
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = []
  for i in range(len(matrix)):
     transposed.append([row[i] for row in matrix])

output: 
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
-----------------------------------------------

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print (list(zip(*matrix)))

output:
  [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
