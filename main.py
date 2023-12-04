def psum(a, b):
    return a + b

def pmultiply(a, b):
    return a * b

import mod

num1 = 5
num2 = 7

result_sum = mod.psum(num1, num2)
result_multiply = mod.pmultiply(num1, num2)

import platform
platform_contents = dir(platform)
print(platform_contents)