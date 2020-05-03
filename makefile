all: clean run clean

# Running the script.
FILE=export
run:
	python3 ./src/run.py "$(FILE) $(SRC) $(OUT)"

# Remove the python caches.
clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

# For quick git commit push.
m=[AUTO]
git: clean
	git add -A
	git commit -m "$(m)"
	git push

