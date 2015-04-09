from math import pow
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
        
if __name__ == '__main__':
    projectList = {
    "Project1" : Project1,
    "Project2" : Project2,
    "Project3" : Project3,
    "Project4" : Project4,
    "Project5" : Project5,
    "Project6" : Project6
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
                
                """this is a git test"""
                
        
    