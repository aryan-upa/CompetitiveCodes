# Google Kickstart 2021, Round B, Ques 3
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6#problem

from math import ceil,floor,sqrt


def prime(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        val = ceil(sqrt(x))
        for p in range(2, val+1):
            if x % p == 0:
                return 0
        else:
            return 1


z= input()
fp = ceil(sqrt(int(z)))
while True:
    if prime(fp):
        break
    fp+=1
p = fp-1
while True:
    if prime(p):
        break
    p-=1
r = fp+1
while True:
    if prime(r):
        break
    r+=1

if r*fp<=int(z):
    print(fp,r)
    print(fp*r)
else:
    print(p,fp)
    print(p*fp)

# For Solution in C++:
# The actual solution used yarin's sieve to store data which is multiplication of those prime numbers.
# Actually we needed to find first prime number smaller than root of z and then a prime no. just smaller than that
# and a prime number just greater than that. Our answer will lie in only the two possibilities given.
# If those prime numbers are [p,q,r] then our possible answer will be either p*q or q*r, not anything else than this.
# We need to keep this in mind as well that the greatest difference between any two prime numbers is in range of 10^9,
# and so we need to calculate prime check for all the values in between, but in C++ this primality check is much faster
# and it runs in about 7 seconds for all the values.
# Also there's a corner case for numbers less than 15 as, for those the only solution is 2,3 i.e. 6.
