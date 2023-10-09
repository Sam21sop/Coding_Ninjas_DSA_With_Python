import heapq
from collections import  defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


    def __lt__(self, other):
        return self.freq < other.freq
    

def build_hufman_tree(freq_dict):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node

        heapq.heappush(priority_queue, merged_node)
    return priority_queue[0]


def generate_huffman_code(root):
    codes = {}
    def traverse(node, code):
        if node:
            if node.char:
                codes[node.char] = code
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    
    traverse(root, '')
    return codes


def huffman_encoding(data):
    freq_dict = dict(Counter(data))
    root = build_hufman_tree(freq_dict)
    huffman_codes = generate_huffman_code(root)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, root


def huffman_decoding(encoded_data, root):
    decoded_data = []
    current_node = root
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data.append(current_node.char)
            current_node = root
    return ''.join(decoded_data)


def main():
    data = 'this is an example of huffman coding'
    print(f"Original Data: {data}")
    encoded_data, huffman_tree = huffman_encoding(data)
    print(f'Encoded Data: {encoded_data}')
    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(f'Decoded Data: {decoded_data}')
    
    
if __name__ == "__main__":
    main() 