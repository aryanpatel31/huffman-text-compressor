.PHONY: test demo clean

test:
	python huffman_test.py

demo:
	python huffman.py

clean:
	rm -f compression_analysis.png
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
