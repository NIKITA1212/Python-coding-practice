Queure: first in first out

from collection import deque

q = deque(['nikita','darshan','unnati'])
q.append('shreyas')
q.popleft()
print(q)
print(lsit(q))

output::
deque(['darshan','unnati','shreyas'])
['darshan','unnati','shreyas']

