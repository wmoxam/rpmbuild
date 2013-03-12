
all: setup nodejs ruby
	echo "Making All"

setup:
	sudo yum -y install rpm-build
	sudo yum -y install redhat-rpm-config
	sudo yum groupinstall "Development Tools"
	echo "cp .rpmmacros ~/"
	cp .rpmmacros ~/

nodejs:
	wget http://nodejs.org/dist/v0.8.22/node-v0.8.22.tar.gz
	mv node-v0.8.22.tar.gz SOURCES/.
	rpmbuild -ba SPEC/nodejs.spec

ruby:
	sudo yum install -y readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc
	wget http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p392.tar.gz
	mv ruby-1.9.3-p392.tar.gz SOURCES/.
	rpmbuild -ba SPECS/ruby.spec
