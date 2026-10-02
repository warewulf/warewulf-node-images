.PHONY: all
all: Containerfile-10.1
all: Containerfile-10.2
all: Containerfile-10-x86_64_v2

.PHONY: clean
clean:
	rm -f Containerfile-10.*
	rm -f Containerfile-10-x86_64_v2

Containerfile-10.%: Containerfile-vault
	env release=10.$* envsubst '$$release' <Containerfile-vault >$@

Containerfile-10.2: Containerfile-fixed
	env release=10.2 envsubst '$$release' <Containerfile-fixed >$@

Containerfile-10-x86_64_v2: Containerfile
	sed 's|^FROM docker.io/library/almalinux:10$$|FROM --platform=linux/amd64/v2 quay.io/almalinuxorg/almalinux:10|' $< >$@
