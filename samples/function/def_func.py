#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
	
#一元二次方程求解 ax2+bx+c=0
def quadratic(a, b, c):	
	if a == 0:
        raise TypeError('a不能为0')
    if not isinstance(a,(int,float)) or  not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
    delta = math.pow(b,2) - 4*a*c
    if delta < 0:
        return '无实根'
    x1= (math.sqrt(delta)-b)/(2*a)
    x2=-(math.sqrt(delta)+b)/(2*a)
    return x1,x2

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
my_abs('123')
