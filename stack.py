from collections import deque

class Stack:
    def __init__(self):
     self.stack = deque()

    def append_value(self,val):
        self.stack.append(val)

    def pop_value(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

        
def  is_match(ch1, ch2):
    match_dict = {
        ')' : '(',
        '}' : '{',
        '[' : ']'
    }
    return match_dict[ch1] ==  ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch == '{' or ch == '[':
            stack.append_value(ch)
        if ch == ')' or ch =='}' or ch == ']':
            if stack.size() == 0 :
                return False
            if  not is_match(ch,stack.pop_value()):
                return False

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


    