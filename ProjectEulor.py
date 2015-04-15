from math import pow
import math
import sys

### the following is for timeit testing
def run():
    number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    limit = 13
    thirteen = []
    digits = []
    largest = 0
    i = 0

    while i < len(number):
        num = number[i:i+limit]
        zero_pos = num.find('0')
        if zero_pos < 0:
            product = reduce(lambda x,y: int(x)*int(y), num)
            if product > largest:
                largest = product
                thirteen = [int(x) for x in num]
        elif zero_pos >= 0:
            i += zero_pos
        elif len(num) < 13:
            break

        i += 1    

class Help():
    def run(self):
        print "Enter an integer that corresponds to the Eulor Project Number"
        print "Solutions are available for the following projects:"
        for proj in projectList:
            print proj + "\n"
            
class Project1():
    def run(self):
        n = 0
        for i in xrange(1,1000):
            if not i % 5 or not i % 3:
                n = n + i
        print n
        
class Project2():
    def run(self):
        arr = []
        a,b = 0, 1
        while b <= 4000000:
            a,b = b, a+b
            if b%2 == 0:
                arr.append(b) 
        sum=0
        for x in arr:
            sum = x + sum
        print sum

class Project3():
    '''
        We want to know what the largest prime factor is of 
        600851475143
    '''
    def run(self):
        n = 600851475143
        i = 2
        while i * i <n:
            while n%i == 0:
                n = n/i
            i+=1
        print n
        
class Project4():
    """
    Find the largest palindrome made from the product of two 3-digit numbers:
       
    So we start with 999, the largest 3 digit number (a).
    We multiply that by all the other numbers less than it.  We compare that number to it's
    reversed string (s[::-1]), and if they are the same, we break out of the loop
    """
    def run(self):
        n = 0
        for a in xrange(999, 100, -1):
            for b in xrange(a, 100, -1):
                x = a * b
                if x > n:
                    s = str(x)
                    if s == s[::-1]:
                        n = a*b
                        break
        print n

class Project5():
    """
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    def run(self):
        n = 20
        p = 0
        while(p == 0):
            for x in xrange(1, 21):
                if n%x != 0:
                    break
            if x == 20:
                p = n
            else:
                n +=1
        print n
        
class Project6():
    """
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    def run(self):
        n = 10
        r = xrange(1, n+1)
        a = sum(r)
        print a * a - sum(i * i for i in r)
        
class Project7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
    def run(self):
        n = 0
        for x in xrange(2, sys.maxint):
            if self.is_prime(x):
                if n == 10000:
                    reqprime = x
                    break
                else:
                    n += 1
        print reqprime
    def is_prime(self, a):
        return all(a % i for i in xrange(2, a))
        
class Project8():
    """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    def run(self):
        number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
        limit = 13
        thirteen = []
        digits = []
        largest = 0
        i = 0

        while i < len(number):
            num = number[i:i+limit]
            zero_pos = num.find('0')
            if zero_pos < 0:
                product = reduce(lambda x,y: int(x)*int(y), num)
                if product > largest:
                    largest = product
                    thirteen = [int(x) for x in num]
            elif zero_pos >= 0:
                i += zero_pos
            elif len(num) < 13:
                break

            i += 1    
        print largest
    
    def run_slower_butEasyToRead(self):
        x = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
        n = 0
        for i in xrange(0, len(x)-12):
            m = 1
            if 0 not in xrange(i, i+13):
                for q in xrange(i, i+13):
                    m = m * int(x[q])
                if m > n: n = m
                
        print n
        
class Project9():
    """
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    def run(self):
        for a in xrange(1, 1000):
            for b in xrange(1, 1000):
                c = 1000 - a - b
                if a*a + b*b == c*c:
                    print a*b*c
                    
class Project10():
    def sieveOfAtkin(self,limit):
        P = [2,3]
        sieve=[False]*(limit+1)
        sieve[2] = True
        sieve[3] = True
        for x in xrange(1,int(math.sqrt(limit))+1):
            for y in range(1,int(math.sqrt(limit))+1):
                n = 4*x**2 + y**2
                if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
                n = 3*x**2+y**2
                if n<= limit and n%12==7 : sieve[n] = not sieve[n]
                n = 3*x**2 - y**2
                if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
        for x in xrange(5,int(math.sqrt(limit))):
            if sieve[x]:
                for y in xrange(x**2,limit+1,x**2):
                    sieve[y] = False
        return sieve
        

    def run(self):
        """
        Find the sum of all the primes below two million.
        """
        """
        We'll use a Atkin Sieve, refer to:
        http://www.codeproject.com/Articles/429694/Finding-prime-numbers
        """
        limit = 2000000
        sieve = self.sieveOfAtkin(limit)
        print sum(x for x in xrange(2, len(sieve)) if sieve[x])
        
        
if __name__ == '__main__':
    projectList = {
    "Project1" : Project1,
    "Project2" : Project2,
    "Project3" : Project3,
    "Project4" : Project4,
    "Project5" : Project5,
    "Project6" : Project6,
    "Project7" : Project7,
    "Project8" : Project8,
    "Project9" : Project9,
    "Project10": Project10
    }
    while True:
        projNum = raw_input("Please enter the Euler Project Number: ")
        try: 
            projNum = int(projNum)
            if projNum != 0:
                projNum = "Project" + str(projNum)
                try:
                    proj = projectList[projNum]()
                    proj.run()
                except Exception as e:
                    print "I don't have a solution for that one yet"
                    print e
            else:
                break

        except: 
            if projNum == "-h":
                h = Help()
                h.run()
            else:
                print "Please enter an Integer or -h for help"
