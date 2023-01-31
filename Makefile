all: centos-7.tar rockylinux-8.tar
.PHONY: all

%.tar: %/Containerfile
	podman save $$(podman build --quiet $*) >$@

clean:
	rm -rf *.tar
.PHONY: clean