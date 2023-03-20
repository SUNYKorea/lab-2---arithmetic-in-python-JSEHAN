# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 
    

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y

def neg(x):
    return -x

def exp(x,y):
    return x**y

def sqrt(x):
    return x**0.5

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 1
b = -4
c = 1

# quadratic equation ax**2 + bx + c = 0, where a, b, c are real numbers and a =/= 0
# (-b +/- (b**2 - 4 * a * c) ** 0.5) / (2 * a)
import cmath
d = c^2 - 4 * a * c
print: cmath
denom = mult(2,a)
nom1 = add(neg(b), sqrt(sub(exp(b,2), (mult(mult(4, a),c)))))
nom2 = sub(neg(b), sqrt(sub(exp(b,2), (mult(mult(4, a),c)))))

x1 = nom1 / denom 
x2 = nom2 / denom
print("First root:" + str(x1))
print("Second root:" + str(x2))