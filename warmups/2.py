def sumOfDigits(n):
    if n<10:
        return n
    return int(n%10 + sumOfDigits(n/10))
def main():
    n=int(input())
    print(sumOfDigits(n))
main()
