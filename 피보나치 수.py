#!/usr/bin/env python
# coding: utf-8

# # 피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 예를 들어 n = 3이라면 2를 반환해주면 됩니다.

# In[4]:


def fib(num):
    l = []
    a, b = 0, 1
    while len(l) != num+1:
        l.append(a)
        a, b = b, a+b
    return l[-1]

print(fib(3))


# In[ ]:




