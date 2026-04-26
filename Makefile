.PHONY: test demo clean

test:
	python huffman_test.py

demo:
	python huffman.py

clean:
	#removing visualization
	rm -f compression_analysis.png
	# removing Python cache folders
	find . -type d -name __pycache__ -exec rm -rf {} +
	#removing compiled Python files
	find . -type f -name "*.pyc" -delete
