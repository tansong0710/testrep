#! /usr/bin/env python3
# -*- coding utf-8 -*-
height = 1.75
wight = 80.5
bmi= wight/(height**2)
print(bmi)
if bmi < 21.5:
    print("过轻");
elif bmi < 23:
    print("normal");
else:
    print("default");

n = 1
while n < 100:
    print(n);
    n = n+1;
    if n < 50:
        continue
    print("continue")
    if n > 80:
        break;