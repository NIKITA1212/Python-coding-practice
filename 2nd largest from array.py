
You are given  numbers. Store them in a list and find the second largest number.

Input Format 
The first line contains . The second line contains an array [] of  integers each separated by a space.

Constraints 
 

Output Format 
Output the value of the second largest number.

Sample Input

5
2 3 6 6 5
Sample Output

5
-------------------------------
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = list(reversed(sorted(arr)))
    for x in range(n):
        if(a[x]==a[x+1]):
            continue
        else:
            print(a[x+1])
            break
  
