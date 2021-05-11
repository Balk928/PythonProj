# Take something return something nature
def evenly_divisible(a, b, c):
    sum = 0
    for i in range(a, b + 1):
        if i % c == 0:
            sum = sum + i
    return sum


for de in range(1, 4):
    x = evenly_divisible(int(input('First:')), int(input('Second')), int(input('Third')))
    print(x)


def replace_vowel(string, charcter):
    vowel = 'aeiou'
    for i in vowel:
        sting = string.replace(i, charcter)
    return string


x = replace_vowel("the aarvark", '#')
print(x)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


x = factorial(input())
print(x)


def evla():
    x = eval(input("enter the string"))
    print(x)


print(evla())
