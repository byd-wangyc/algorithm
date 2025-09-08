class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linklist:
    def __init__(self):
        self.head = None
        self.size = 0

    def addtail(self,val):
        new_code = node(val)
        if self.head == None:
            self.head = new_code
        else:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
            cur.next = new_code  # pyright: ignore[reportAttributeAccessIssue]
        self.size +=1

    def print_linklist(self):
        cur = self.head
        while cur!=None:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")
    
    def delete(self,index):
        if index<0 or index>=self.size:
            return
        else:
            if index ==0:
                self.head = self.head.next # pyright: ignore[reportOptionalMemberAccess]
            else:
                cur = self.head
                for _ in range(index-1):
                    cur = cur.next # pyright: ignore[reportOptionalMemberAccess]
                cur.next = cur.next.next # pyright: ignore[reportAttributeAccessIssue, reportOptionalMemberAccess]
        self.size-=1

linklist1 = linklist()
linklist1.addtail(1)
linklist1.addtail(2)
linklist1.addtail(3)
linklist1.print_linklist()
linklist1.delete(1)
linklist1.print_linklist()
print(linklist1.size)


    