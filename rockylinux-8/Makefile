.PHONY: all
all: Containerfile-8.6
all: Containerfile-8.7
all: Containerfile-8.8
all: Containerfile-8.9
all: Containerfile-8.10

.PHONY: clean
clean:
	rm -f Containerfile-8.*

Containerfile-8.%: Containerfile-vault
	env releasever=8.$* envsubst <Containerfile-vault >$@

Containerfile-8.10: Containerfile-fixed
	env releasever=8.10 envsubst <Containerfile-fixed >$@
