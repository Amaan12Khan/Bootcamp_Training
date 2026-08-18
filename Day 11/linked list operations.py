class Node:
    def __init__(self, data):
        self.data = data  # The item value
        self.next = None  # Pointer to next item

# Manually linking scattered nodes
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

current = head

while current is not None:
    print(current.data)      # Print the data of the current node
    current = current.next   # Move to the next node in the line

count=0
while current is not None:
    count+=1      # Count the number of nodes in the linked list
    current = current.next 
print("Number of nodes:", count)

a=int(input("Enter the value to search for: "))
while current is not None:
    if current.data == a:
        print("Found the node with data", a)
        break   
    else:
        print("Node with data", a, "not found")
    current = current.next

#1.insert at the last position
def insert_last(head_node, data):
    new_node = Node(data)
    
    # If the list is empty, the new node becomes the head
    if head_node is None:
        return new_node
        
    current = head_node
    # Walk until you reach the actual last node
    while current.next is not None:
        current = current.next
    
    # Link the last node to the new node
    current.next = new_node
    return head_node

# --- 5. CALLING THE FUNCTION ---
# FIX: Pass the 'head' variable and the actual data number you want to add
head = insert_last(head, 40)

# Verification: Print the list one last time to see the new item
print("\nList after inserting 40 at the end:")
current = head
while current is not None:
    print(current.data)
    current = current.next

#2. Insert at a specific index
def insert_at(self, data, index):
    # 1. Handle insertion at the very beginning (Index 0)
    if index == 0:
        self.insert_first(data)
        return

    # 2. Start at the head node
    curr = self.head
    
    # 3. Move forward until we are exactly ONE step before the target index
    # FIX: Added the minus sign '-' inside range()
    for i in range(index - 1):
        if curr is None:
            print("Index out of bounds")
            return
        curr = curr.next

    # 4. Check if the target position is valid
    if curr is None:
        print("Index out of bounds")
        return

    # 5. Connect the new node
    new_node = Node(data)
    new_node.next = curr.next  # Point new node to the rest of the chain
    curr.next = new_node       # Point previous node to our new node


