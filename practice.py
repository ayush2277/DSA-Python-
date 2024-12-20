class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head  = None

    def insert_at_begg(self,data):
        node = Node (data ,self.head)
        self.head = node
    
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


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)


    def insert_values(self,data_lists):
        self.head = None
        for i in data_lists:
          self.insert_at_end(i)


    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count


    def remove_element(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid")


        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                break
            itr.next = itr.next.next
            count += 1


    def insert_at(self,index,data):
         if index<0 or index>self.get_length():
            raise Exception("Invalid")

         if index == 0:
            self.insert_at_begg(data)
            return

         count = 0
         itr = self.head
         while itr:
            if count == index - 1:
             node = Node(data, itr.next)
             itr.next = node
             break

            itr = itr.next
            count += 1

    



if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_values(["banana","apple","mango","waatermelon"])
    print(ll.get_length())
    #ll.remove_element(30)
    ll.insert_at(5,"pappaya")
    ll.print()