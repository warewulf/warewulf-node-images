.PHONY: all
all: Containerfile-9.0
all: Containerfile-9.1
all: Containerfile-9.2
all: Containerfile-9.3
all: Containerfile-9.5
all: Containerfile-9.4

.PHONY: clean
clean:
	rm -f Containerfile-9.*

Containerfile-9.%: Containerfile-vault
	env release=9.$* envsubst '$$release' <Containerfile-vault >$@

Containerfile-9.5: Containerfile-fixed
	env release=9.5 envsubst '$$release' <Containerfile-fixed >$@
