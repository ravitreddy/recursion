def isSubsequence(first,n,second,m,i,j):
    if i==n-1:
        return 'True'
    if i>=n or j>=m:
        return 'False'
    if first[i]==second[j]:
        return isSubsequence(first,n,second,m,i+1,j+1)
    else:
        return isSubsequence(first,n,second,m,0,j+1)

def main():
    first, second=input().split()
    n=len(first)
    m=len(second)
    print(isSubsequence(first,n,second,m,0,0))
main()
