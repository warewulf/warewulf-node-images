.PHONY: all
all: Containerfile-9.5
all: Containerfile-9.6

.PHONY: clean
clean:
	rm -f Containerfile-9.*

Containerfile-9.%: Containerfile-vault
	env release=9.$* envsubst '$$release' <Containerfile-vault >$@

Containerfile-9.6: Containerfile-fixed
	env release=9.6 envsubst '$$release' <Containerfile-fixed >$@
