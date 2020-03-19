########################################
#                                      
# This program implements heap sort which is a sorting algorithm 
# based on Binary Heap data structure. It will first find the max
# element and place it at the end. The process is repeated until
# it is sorted.            
#  
########################################

import math as m

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        #write your code here
        if self.top == None:
            return True 
        else: 
            return False

    def __len__(self):
        #write your code here
        return self.count

    
    def peek(self):
        #write your code here
        if self.top == None:
            return 'Stack is empty'
        else: 
            return self.top.value

    def push(self,value):
        #write your code here
        nn = Node(value)
        nn.next = self.top
        self.top = nn 
        self.count += 1

    def pop(self):
        #write your code here
        if self.top == None:
            return 'Stack is empty'
        else: 
            x = self.top.value
            self.top = self.top.next 
            self.count -= 1
            return x

class MaxHeapPriorityQueue:

    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        return self.size


    def parent(self,index):
        if index <= 1 or index > self.size:
            return None
        else:
            n = int(index/2) 
            return self.heap[n - 1]

        

    def leftChild(self,index):
        try:
            x = 2*index
            return self.heap[x - 1]
        except:
            return None


    def rightChild(self,index):
        try: 
            x = (2*index) + 1
            return self.heap[x - 1]
        except:
            return None
 

    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]
        

    def insert(self,x):
        self.heap
        self.heap.append(x)
        self.size += 1
        x = len(self.heap)
        p = m.floor(x/2)
        while True: 
            if p-1 == -1: 
                break
            if self.heap[p-1] <= self.heap[x-1]: 
                self.swap(x, p)
                x = p
                p = m.floor(x/2)
            else: 
                break

    def deleteMax(self):
        if self.size<=0:
            return None
        elif self.size==1:
            self.size=0
            return self.heap[0]
        else: 
            #Save the root
            popped = self.heap[0]
            #Remove Root 
            #Move the rightmost leaf
            xIndice = len(self.heap)
            self.swap(xIndice, 1)
            del self.heap[xIndice-1]
            self.size -= 1
            #Find the biggest child
            #swap node with biggest child
            pIndice = 1
            while True:
                if self.leftChild(pIndice) == None and self.rightChild(pIndice) == None:
                    return popped
                #if both children exist, continue
                if self.leftChild(pIndice) != None and self.rightChild(pIndice) != None:
                    #if either child is greater than the parent
                    if self.leftChild(pIndice) > self.heap[pIndice-1] or self.rightChild(pIndice) > self.heap[pIndice-1]:
                        #if the left child is greater than the right child
                        if self.leftChild(pIndice) > self.rightChild(pIndice):
                            leftIndice = 2*pIndice
                            self.swap(pIndice, leftIndice)
                            pIndice = leftIndice
                            continue
                        #if the right child is greater than the left child
                        elif self.leftChild(pIndice) < self.rightChild(pIndice):
                            rightIndice = 2*pIndice+1
                            self.swap(pIndice, rightIndice)
                            pIndice = rightIndice
                            continue
                        #if the left child is equal to the right child
                        elif self.leftChild(pIndice) == self.rightChild(pIndice):
                            leftIndice = 2*pIndice
                            self.swap(pIndice, leftIndice)
                            pIndice = leftIndice
                        else: 
                            continue
                    else: 
                        break
                elif self.leftChild(pIndice) != None: 
                    leftIndice = 2*pIndice
                    if self.heap[pIndice-1] < self.heap[leftIndice-1]:
                        self.swap(pIndice, leftIndice)
                        pIndice = leftIndice
                        return popped
                    return popped
                elif self.rightChild(pIndice) != None:
                    rightIndice = 2*pIndice+1
                    if self.heap[pIndice-1] < self.heap[rightIndice-1]:
                        self.swap(pIndice, rightIndice)
                        pIndice = rightIndice
                        return popped
                    return popped
                else: 
                    break
            return popped

def heapSort(numList):
    x = MaxHeapPriorityQueue()
    s = Stack()
    finalList = []
    for i in numList:
        x.insert(i)
    while x.size != 0:
        popped = x.deleteMax()
        s.push(popped)
    while s.isEmpty() == False:
        finalList.append(s.pop())

    return finalList




