import unittest
from huffman import build_frequency_table, build_huffman_tree, generate_codes, encode, decode, calculate_compression_ratio

class TestHuffmanCompression(unittest.TestCase):
    
    def test_encode_decode_roundtrip(self):
        """Test that encoding then decoding returns original text"""
        text = "hello world this is a test"
        
        # compressing
        frequency = build_frequency_table(text)
        tree = build_huffman_tree(frequency)
        codes = generate_codes(tree)
        encoded = encode(text, codes)
        
        # decompressing
        decoded = decode(encoded, tree)
        
        # verify original text is recovered
        self.assertEqual(text, decoded)
    
    def test_single_character_file(self):
        """Test encoding/decoding with single unique character"""
        text = "aaaaa"
        
        frequency = build_frequency_table(text)
        tree = build_huffman_tree(frequency)
        codes = generate_codes(tree)
        encoded = encode(text, codes)
        decoded = decode(encoded, tree)
    
        self.assertEqual(text, decoded)
    
    def test_compression_ratio_bounds(self):
        """Test that compression ratio is between 0-100%"""
        text = "the quick brown fox jumps over the lazy dog" * 10
        
        frequency = build_frequency_table(text)
        tree = build_huffman_tree(frequency)
        codes = generate_codes(tree)
        encoded = encode(text, codes)
        
        ratio, original_size, compressed_size = calculate_compression_ratio(text, encoded)
        
        # ratio should be between 0 and 100
        self.assertGreaterEqual(ratio, 0)
        self.assertLessEqual(ratio, 100)
        
        # compressed should be smaller than original
        self.assertLess(compressed_size, original_size)

    def test_empty_string(self):
        """Test encoding/decoding with empty string"""
        text = ""
            
        frequency = build_frequency_table(text)
            
        # empty string should result in empty frequency table
        self.assertEqual(len(frequency), 0)

    def test_codes_are_unique(self):
        """Test that all generated codes are unique"""
        text = "the quick brown fox jumps over the lazy dog"
            
        frequency = build_frequency_table(text)
        tree = build_huffman_tree(frequency)
        codes = generate_codes(tree)
            
        # all codes should be unique
        code_values = list(codes.values())
        self.assertEqual(len(code_values), len(set(code_values)))  # No duplicates


if __name__ == '__main__':
    unittest.main()
