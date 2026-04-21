
import heapq

class Node:
    """Represents a node in the Huffman tree"""
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char        # The character (None if internal node)
        self.freq = freq        # Frequency of character
        self.left = left        # Left child (0)
        self.right = right      # Right child (1)

    def __lt__(self, other):
        """Less than operator for heap comparison"""
        return self.freq < other.freq
    
def build_frequency_table(text):
    """Count the frequency of each character in the text"""
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
        
    return frequency


def build_huffman_tree(frequency):
    """Build the Huffman tree from chraracter frequencies"""

    #if only one unique character (edge case)
    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        return Node(char = char, freq = frequency[char])
    
    #creating a min-heap with all characters
    heap = []
    for char, freq in frequency.items():
        node = Node(char = char, freq = freq)
        heapq.heappush(heap, node)

    #building tree by combining smallest nodes
    while len(heap) > 1:
        left = heapq.heappop(heap) #smallest
        right = heapq.heappop(heap) #2nd smallest

        #creating parent node (internal node, so no char)
        parent = Node(freq= left.freq + right.freq, left = left, right = right)
        heapq.heappush(heap, parent) #parent back on heap
        
    return heap[0] 


def generate_codes(node, code="", codes=None):
        """Generate binary codes for each character by traversing the tree"""
        
        if codes is None:
            codes = {}

        #Base case: leaf node (has a char)
        if node.char is not None:
            codes[node.char] = code if code else "0" #handling single char edge case
            return codes
        
        #recursive case : traverse left (add "0") and traverse right (add "1")
        if node.left:
            generate_codes(node.left, code + "0", codes)
        if node.right:
            generate_codes(node.right, code + "1", codes)

        return codes

def encode(text, codes):
    """Encode the text using the Huffman codes"""
    encoded = ""
    
    for char in text:
        encoded += codes[char]

    return encoded

def decode(encoded_text, node):
    """Decode the binary string back to original text using the Huffman tree"""
    decoded = ""
    current = node

    for bit in encoded_text:
        
        if bit == "0":
            current = current.left
        else:
            current = current.right
        
        #reached leaf node (char)
        if current.char is not None:
            decoded += current.char
            current = node #reseting to root for next char

    return decoded

def calculate_compression_ratio(original_text, encoded_text):
    """Calculate how much we compressed the text"""
    original_size = len(original_text) * 8 #each char is 8 bits
    compressed_size = len(encoded_text) #each bit in encoding

    ratio = (1 - compressed_size / original_size) * 100

    return ratio, original_size, compressed_size

def analyze_compression():
    """Analyze compression across different file types"""
    results = []
    
    files_to_compress = [
        ("data/small.txt", "text"),
        ("data/large.txt", "text"),
        ("data/script.py", "code"),
        ("data/notes.md", "markdown"),
        ("data/sample.jpg", "image")
    ]
    
    for filepath, file_type in files_to_compress:
        if file_type == "image":
            # For images, read as binary
            with open(filepath, 'rb') as f:
                data = f.read()
            text = data.decode('latin1')  # Convert bytes to string
        else:
            # For text files, read normally
            with open(filepath, 'r') as f:
                text = f.read()
        
        # Now compress all the same way
        frequency = build_frequency_table(text)
        tree = build_huffman_tree(frequency)
        codes = generate_codes(tree)
        encoded = encode(text, codes)
        
        ratio, original_size, compressed_size = calculate_compression_ratio(text, encoded)
        
        result = {
            'filename': filepath.split('/')[-1],
            'type': file_type,
            'original_size': original_size,
            'compressed_size': compressed_size,
            'ratio': ratio
        }
        
        results.append(result)
    
    return results

def print_compression_analysis(results):
    """Print analysis results"""
    print("\n" + "=" * 80)
    print("COMPRESSION ANALYSIS ACROSS FILE TYPES")
    print("=" * 80)
    print(f"{'Filename':<20} {'Type':<10} {'Original (bits)':<20} {'Compressed (bits)':<20} {'Ratio %':<10}")
    print("-" * 80)
    
    for result in results:
        print(f"{result['filename']:<20} {result['type']:<10} {result['original_size']:<20} {result['compressed_size']:<20} {result['ratio']:<10.2f}")
    
    print("=" * 80)


if __name__ == "__main__":
    # Run compression analysis
    results = analyze_compression()
    print_compression_analysis(results)