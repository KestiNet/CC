import heapq
#https://www.geeksforgeeks.org/huffman-coding-in-python/

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.frequency < other.frequency
    
def huffman_tree(char, frequency):
    priority_queue = [Node(char, f) for char, f in zip(char, frequency)]
    heapq.heapify(priority_queue)

    while len(priority_queue) >1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]






with open('134-0.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

char_freq = {}

def huffman_tree(char, frequency):


for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1


for char, frequency in char_freq.items():
    print(f"'{char}': '{frequency}'")