.PHONY: all
all: Containerfile-10.0
all: Containerfile-10.1

.PHONY: clean
clean:
	rm -f Containerfile-10.*

Containerfile-10.%: Containerfile-vault
	env release=10.$* envsubst '$$release' <Containerfile-vault >$@

Containerfile-10.1: Containerfile-fixed
	env release=10.1 envsubst '$$release' <Containerfile-fixed >$@
