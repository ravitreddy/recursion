def reverseOrder(s,n):
    if n==1:
        return s[0]
    return s[n-1]+reverseOrder(s,n-1)

def main():
    s=input()
    n=len(s)
    rev=reverseOrder(s,n)
    if s==rev:
        print('Palindrome')
    else:
        print('not palindrome')
main()
