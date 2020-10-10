from collections import Counter
def socks(n, ar):
  n=input()
  ar = input().strip().split()
  soc=0
  for value in Counter(ar).values():
    soc+=value//2
    return soc
socks(n, ar)