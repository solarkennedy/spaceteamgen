.PHONY: test fetch run

test:
	py.test -v

fetch:
	./fetch_strings.sh

run:
	@./spaceteamgen.py
