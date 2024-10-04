# AdsGencyAI Interview
# 
# 
# 
# 
'''
Python3 ( no libraries to import )
Standard python sufficient.
set up your python environment.

Whatever helps crystallize your thought process.
Print series of operations on your terminal.
Data structure requirements + data structure contstraints.

Clarifying the question :
- O(1) time performance
- Just integer
- stack fits into RAM reasonably sized input
- can have empty stacks
- check stack sizes for valid operations
- tradeoff : time and space -> put more space to get better time
- insert(x) -> x can be the next min insert(y) -> y is not a min until an element is removed
- history of record notion in each cell
- integer values -inf to inf

Categorize : Stack, List, FILO order, PriorityQueue ( heap )
Implement operations : push(), pop(), top(), getMin() in O(1) time complexity

Target Complexity Analysis :
N = #-element pushed onto the stack during lifetime
O := #-operations to execute
Time = O(1)
Space = O(N) (explicit) O(1) (implicit call stack )

Test Cases :
a. push(5),push(4),push(6),push(3),push(7),pop(),getMin(),pop(),getMin(),pop(),getMin(),...
    3,3,4,4,5
b. push(5),getMin(),pop(),getMin()
    5,-inf
c. getMin(), push(5),push(5),push(5), pop(), getMin(), pop(), getMin(), pop(), getMin(), getMin()
    -inf,5,5,5,-inf
d. All ascending order : push(1), push(2), ...
e. All descending order
f. Please get python working here! Python interpreter environment for windows.


'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.numItems = 0
        self.globalMin = float('inf')

    # update global min as we go
    def push(self, x:int):
        if(x <= self.globalMin):
            self.globalMin = x
        record = [x,self.globalMin]
        self.stack.append(record)

    # global min under possible update?
    # single record stack ( no future minimum ) or stack with 2 records
    def pop(self) -> int:
        if(len(self.stack) == 0):
            # throwing Exceptions or raising errors to caller scope
            return ""
        targetRecord = self.stack[-1]
        targetEl = targetRecord[0]
        lastIdx = len(self.stack) - 1
        self.stack.pop(lastIdx)
        if(len(self.stack) == 0):
            self.globalMin = float('inf')
        elif(len(self.stack) > 0):
            curLastRecord = self.stack[-1]
            self.globalMin = curLastRecord[1]
        return targetEl

    def top(self) -> int:
        if(len(self.stack) == 0):
            return ""
        targetRecord = self.stack[-1]
        targetEl = targetRecord[0]
        return targetEl
    
    def getMin(self) -> int:
        if(len(self.stack) == 0):
            return float('inf')
        return self.globalMin

def main():
    print("Entered into main()")
    minStack = MinStack() 
    # minStack.push(-2)
    # minStack.push(0) 
    # minStack.push(-3) 
    # print(minStack.getMin())
    # print(minStack.pop())
    # print(minStack.top())
    # print(minStack.getMin())
    # print(minStack.getMin())
    # minStack.push(5)
    # print(minStack.getMin())
    # minStack.push(4)
    # print(minStack.getMin())
    # minStack.push(3)
    # print(minStack.getMin())
    # minStack.push(2)
    # print(minStack.getMin())
    # minStack.push(1)
    # print(minStack.getMin())
    # minStack.pop()
    # print(minStack.getMin()) #2
    # minStack.pop()
    # print(minStack.getMin()) #3
    # minStack.pop()
    # print(minStack.getMin()) #4
    # minStack.pop()
    # print(minStack.getMin()) #5
    # minStack.pop()
    # print(minStack.getMin())
    minStack.push(5)
    minStack.push(4) 
    minStack.push(6)
    minStack.push(3)
    minStack.push(7)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop())

main()




