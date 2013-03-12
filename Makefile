
all: setup nodejs ruby
	echo "Making All"

setup:
	sudo yum -y install rpm-build
	sudo yum -y install redhat-rpm-config
	sudo yum groupinstall "Development Tools"
	echo "cp .rpmmacros ~/"
	cp .rpmmacros ~/

node_downloaded := $(wildcard */node-v0.8.22.tar.gz)

nodejs:
	./download node-v0.8.22.tar.gz http://nodejs.org/dist/v0.8.22/node-v0.8.22.tar.gz
	rpmbuild -ba SPECS/nodejs.spec

ruby:
	sudo yum install -y readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc
	./download ruby-1.9.3-p392.tar.gz http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p392.tar.gz
	rpmbuild -ba SPECS/ruby.spec
