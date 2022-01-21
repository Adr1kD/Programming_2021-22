class Node:
    def __init__(self, info, next_=None):
        self.info= info
        self.next= next_
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def push_front(self, new_info):
        new_element = Node(new_info)

        new_element.next= self.head
        self.head = new_element

        if self.tail is None:
            self.tail = new_element

    def push_back(self, new_info):
        new_element = Node(new_info)
        if self.tail is not None:
            self.tail.next = new_element
            self.tail = new_element
        else:
            self.tail = new_element

        if self.head is None:
            self.head = new_element

    def leng(self):
        crr = self.head
        i=0
        while crr is not None:
            i=i+1
            crr=crr.next
        return i

    def pop_back(self):
        p=self.head
        i=self.leng()
        while i!=2:
            p=p.next
            last_elem=p
            i=i-1
        self.tail=last_elem
        self.tail.next=None

        
    def pop_front(self):
        first_element=self.head
        self.head=self.head.next
        first_element.next=None

    def get_front(self):
        return self.head.info

    def get_back(self):
        return self.tail.info

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def get_info(self, c):
        p=self.head
        i=0
        c=c-1
        while i!=c:
            i+=1
            p= p.next
        return p.info

    def get(self, c):
        p=self.head
        i=0
        c=c-1
        while i!=c:
            i+=1
            p= p.next
        return p
        
    def insert(self, new_info, pos):
        if pos==1:
            self.push_front(new_info)
        else:
            new_element = Node(new_info)
            new_element.next= self.get(pos)
            self.get(pos-1).next= new_element

    def delete(self, pos):
        if pos==1:
            self.pop_front()
        else:
            self.get(pos-1).next=self.get(pos+1)
            #garbrage collecter
       
    def print(self):
        p=self.head
        while p is not None:
            print(p.info, "->", end="")
            p= p.next
        
