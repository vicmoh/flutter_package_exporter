all: clean run clean

# Running the script.
FILE=export
run:
	python3 run.py "$(FILE)"

# Remove the Python Caches.
clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

# For quirck git commit push.
m='[AUTO]'
git: clean
	git add -A
	git commit -m "$(m)"
	git push

