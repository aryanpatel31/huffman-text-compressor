# Huffman Text Compressor

### Project Overview

This project implements Huffman encoding, a data compression algorithm that reduces file sizes by assigning variable length binary codes to characters based on their frequency. The project analyzes compression effectiveness across different file types:
- text
- markdown
- code
- images

The project also visualizes compression ratio and time by file.


### Relevant Data Structure Concepts and their Application

The project uses Binary Trees (for the Huffman tree structure), Min-Heaps (priority queue for building the tree), and Hash Maps/Dictionaries (for frequency tables and code mappings).

###### Application Details

The huffman tree is built using a min-heap priority queue that stores nodes sorted by character frequency. We repeatedly pop the two smallest nodes and combine them until one tree remains. The tree is then traversed recursively to generate optimal binary codes. Hash maps store character frequencies and their corresponding codes for O(1) lookup during encoding.

### Project Workflow

The end to end workflow: (1) Read input file, (2) Count character frequencies using a hash map, (3) Build a Huffman tree using a min-heap, (4) Generate binary codes by traversing the tree, (5) Encode the text by replacing characters with their codes, (6) Calculate compression ratio, (7) Decompress by traversing the tree with the binary string.

The expected input is any text file, markdown file, .jpg file, or .py file.

The expected output is an analysis of the compression including:
- the type of the file
- the number of bits in original file
- the number of bits in compressed version
- the ratio %
- a visualization of compression ratio and time by file


### Performance

The time complexity is O(n*log(k)) where n is the text length and k is the number of unique characters. Building a frequency table is O(n), building the tree is O(k\*log(k)), encoding is O(n), and decoding is O(n). Observed runtime on Alice in Wonderland Chapter 1 took ~0.0009 seconds with 45.1% compression ratio. Larger files compress faster relative to their size due to better character distribution as well. The .jpg file compresses poorly because images contain mostly random pixel values with little character repetition.

### Challenges

The main challenge was handling the edge case of single-character files. I actually did not catch this edge case until I wrote the unit test. When only one unique character exists, the Huffman tree is just a leaf node with no children, causing the decoder to crash. This situation was fixed by checking if the root node itself is a leaf and directly repeating the character. 

Another challenge I faced was handling file I/O for different file types. Text files (.txt, .md, .py) was normal in that they could be read in as regular strings, but the image (.jpg) file was new to me. I decided to read it in binary and then decoded using latin1 (maps each byte to and character) encoding. This was addressed using conditional logic. 

### Improvements

If redoing this project, I would: (1) add better support for binary files beyond text by doing more research into how images are actually compressed, (2) Implement RLE (run-length encoding) as a comparison baseline, (3) add a GUI for user-friendly file selection and compression visualization to make this more user friendly. 

I encountered run-length encoding in some research I was doing about what / where compression is used most often for.

### Learning 

Through this project, I better understood how greedy algorithms optimize solutions, how priority queues enable efficient data structure operations, the importance of handling edge cases in recursive algorithms, how to visualize algorithm performance with matplotlib, and the real world trade off between compression ratio and speed (primarily through research into compression).

Additionally, this was my first time actually writing unit tests so this I was able to learn the process of brainstorming some unit tests and edge cases. I believe this thought process will help me when I am programming so that I see edge cases earlier in the development process.

### Real-World Relevance

Huffman coding is used in file compression tools (zip, gzip), image formats (jpeg, png), and network transmission to reduce bandwidth. Companies use similar compression algorithms for cloud storage and data archiving, and transmitting large datasets. The analysis of different file types' compressibility is relevant for storage optimization and understanding which data compresses well. This type of analysis can save significant money for companies operating on a large scale.


### Use of AI tools

I used Claude for debugging the single character edge case in the decoder, helping me brainstorm/design meaningful unit tests that cover edge cases, and learning the matplotlib library. I also used Claude to refine my docstrings for functions definitions.