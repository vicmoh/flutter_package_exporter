m='[AUTO]'
git:
	git add -A
	git commit -m "$(m)"
	git push

FILE='./'
run:
	python3 export.py $(FILE)
