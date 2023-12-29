.PHONY: all
all: Containerfile-9.0
all: Containerfile-9.1
all: Containerfile-9.2
all: Containerfile-9.3

.PHONY: clean
clean:
	rm -f Containerfile-9.*

Containerfile-9.%: Containerfile-vault
	env releasever=9.$* envsubst <Containerfile-vault >$@

Containerfile-9.3: Containerfile-fixed
	env releasever=9.3 envsubst <Containerfile-fixed >$@
