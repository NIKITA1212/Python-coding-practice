Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format 
The first line contains an integer .

Output Format 
Output the answer as explained in the task.

Sample Input

3
Sample Output

123
---------------------------------------------------------------------------
from __future__ import print_function
if __name__ == '__main__':
   
    n = int(raw_input())
    for x in range(n):
        print((x+1), end="")
    
