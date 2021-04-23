def palindrome(s,start,end):
    if start == end or start +1 == end or len(s)==0:
        return "palindrome"
    if s[start]==s[end]:
        return palindrome(s,start+1,end-1)
    return "Not palindrome"

def main():
    s=input()
    n=len(s)
    start=0
    end=n-1
    print(palindrome(s,start,end))
main()
