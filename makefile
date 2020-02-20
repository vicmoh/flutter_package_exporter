# Running the script.
FILE=export
run:
	python3 run.py "$(FILE)"


# For quirck git commit push.
m='[AUTO]'
git:
	git add -A
	git commit -m "$(m)"
	git push

