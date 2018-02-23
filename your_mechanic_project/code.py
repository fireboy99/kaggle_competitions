class Time(object):
 
    def __init__(self, time_slot, connected, prev, next):
        self.time_slot = time_slot
        self.connected = connected
        self.prev = prev
        self.next = next
        
        
        
class TimeTable(object):
 
    head = None
    tail = None
 
    def add(self, time_slot, connected):
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
                while(current_node is not None):
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
                current_node.connected = False
            current_node = current_node.next
 
    def show(self):
        current_node = self.head
        final_print_str = "["
        while current_node is not None:
            if(current_node.connected == True):
                if(current_node.prev is None):
                    final_print_str += "["
                    final_print_str += str(current_node.time_slot)
                    final_print_str += ", "
                elif(current_node.prev.connected == False):
                    final_print_str += "["
                    final_print_str += str(current_node.time_slot)
                    final_print_str += ", "
                elif(current_node.next == None):
                    final_print_str += str(current_node.time_slot)
                    final_print_str += "], "
            elif((current_node.connected == False) and (current_node.prev.connected == True)):
                final_print_str += str(current_node.time_slot)
                final_print_str += "], "
            current_node = current_node.next
        final_print_str = final_print_str[0:-2] + "]"
        print final_print_str


#lines = ["add, 1, 5","remove, 2, 3", "add, 6, 8", "remove, 4, 7", "add, 2, 7"]
#
#print lines

table = TimeTable()
print "Printing the TimeTable:"
with open("file.csv") as f:
    for line in f:
        cmd = line.replace(" ","")
        cmd = cmd.split(",")
        if(cmd[0] == 'add'):
            for val in range(int(cmd[1]), int(cmd[2])):
                table.add(val,True)
            table.add(val+1,False)
            table.show()
        elif(cmd[0] == 'remove'):
            for val in range(int(cmd[1]), int(cmd[2])):
                table.remove(val)
            table.show()
