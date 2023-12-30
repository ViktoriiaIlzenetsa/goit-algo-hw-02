from collections import deque

def is_palindrome(text):
    text = text.lower()
    dq = deque()
    for i in text:
        if i not in ' ':
            dq.append(i)
    flag = True
    while flag and (len(dq) not in [0,1]):
        if dq.pop() != dq.popleft():
            flag = False
    return flag

print(is_palindrome('abccba'))
print(is_palindrome('Ab  cd cBa'))
print(is_palindrome('   dfjkffkjv  '))
print(is_palindrome('  a roza uPALA na lapu Azora   '))


