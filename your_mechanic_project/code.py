class Time(object):
 
    def __init__(self, time_slot, connected, prev, next):
        self.time_slot = time_slot
        self.connected = connected
        self.prev = prev
        self.next = next
        
        
        
class TimeTable(object):
 
    head = None
    tail = None
 
    def add(self, time_slot,connected):
        new_node = Time(time_slot, connected, None, None)
        # If no elements are present then initialize the system
        if self.head is None:
            self.head = self.tail = new_node
        # If elements are present 3 cases are possible.
        else:
            current_node = self.head
            if(time_slot < self.head.time_slot):
                #Connecting the new node to self head, ie putting it before the head
                new_node.next = self.head
                #Prev willl be none
                new_node.prev = None
                
                #Self heads prev will be connected
                self.head.prev = new_node

                #Initializing self head to new node
                self.head = new_node
            else:
                #We need to insert the new node at an appropriate position or
                #at the end
                current_node = self.head
                while(current_node.next is not None):
                    if(time_slot > current_node.time_slot):
                        current_node = current_node.next
                    elif(time_slot == current_node.time_slot):
                        current_node.connected = True
                        return
                    else:
                        #Connecting the new node to self head, ie putting it before the head
                        new_node.next = current_node
                        #Prev willl be none
                        new_node.prev = current_node.prev 
                        return
                new_node.prev = self.tail
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
 
    def remove(self, time_slot):
        current_node = self.head
 
        while current_node is not None:
            if current_node.time_slot == time_slot:
                # if it's not the first element
                #if current_node.prev is not None:
                current_node.connected = False
#                 else:
#                     # otherwise we have no prev (it's None), head is the next one, and prev becomes None
#                     self.head = current_node.next
#                     current_node.next.prev = None
            current_node = current_node.next
 
    def show(self):
        current_node = self.head
        print "[",
        while current_node is not None:
            if(current_node.connected == True):
                if(current_node.prev is None):
                    print "[",
                    print  current_node.time_slot,
                    print ",",
                elif(current_node.prev.connected == False):
                    print "[",
                    print  current_node.time_slot,
                    print ",",
                elif(current_node.next == None):
                    print  current_node.time_slot,
                    print "]",
            elif((current_node.connected == False) and (current_node.prev.connected == True)):
                print  current_node.time_slot,
                print "]",
            current_node = current_node.next
        print "]"


# In[80]:


lines = ["add, 1, 5","remove, 2, 3", "add, 6, 8", "remove, 4, 7", "add, 2, 7"]


# In[81]:


print lines


# In[83]:


table = TimeTable()
print "Printing the TimeTable:"
for line in lines:
    cmd = line.replace(" ","")
    cmd = cmd.split(",")
    if(cmd[0] == 'add'):
        for val in range(int(cmd[1]), int(cmd[2])):
            table.add(val,True)
            #print val
        table.add(val+1,False)
        table.show()
    elif(cmd[0] == 'remove'):
        for val in range(int(cmd[1]), int(cmd[2])):
            table.remove(val)
        table.show()
