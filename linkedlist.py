class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_lists):
        self.head = None
        for i in data_lists:
            self.insert_at_end(i)

    def print(self):
        if self.head is None:
            print('Linkedlist is empty')
            return 
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_after_value(self, data_after,data_insert):
    
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_insert,itr.next)
                itr.next = node
                break
            itr = itr.next  
    def remove_data_by_value(self,data):
          if self.head.data == data:
            self.head = self.head.next
            return
          
          itr = self.head
          while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next












if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_values(["banana", "apple", "mango", "watermelon"])
    ll.insert_after_value("mango","Litchi")
    ll.remove_data_by_value("banana")
    ll.print()
