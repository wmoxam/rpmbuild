
all: setup redis nodejs ruby
	echo "Making All"

setup:
	sudo cp files/s3tools.repo /etc/yum.repos.d/
	sudo yum -y install s3tools
	sudo yum -y install rpm-build
	sudo yum -y install redhat-rpm-config
	sudo yum groupinstall "Development Tools"a
	sudo yum install -y readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc
	echo "cp .rpmmacros ~/"
	cp .rpmmacros ~/
	echo "cp .wgetrc ~/"
	cp .wgetrc ~/

redis:
	./download redis-2.6.11.tar.gz http://redis.googlecode.com/files/redis-2.6.11.tar.gz
	rpmbuild -ba SPECS/redis.spec

nodejs:
	./download node-v0.8.22.tar.gz http://nodejs.org/dist/v0.8.22/node-v0.8.22.tar.gz
	rpmbuild -ba SPECS/nodejs.spec

ruby:
	./download ruby-1.9.3-p392.tar.gz http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p392.tar.gz
	rpmbuild -ba SPECS/ruby.spec
