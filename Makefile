
all: setup redis nodejs libyaml ruby19 ruby20
	echo "Making All"

setup:
	sudo cp files/s3tools.repo /etc/yum.repos.d/
	sudo yum -y install s3cmd
	sudo yum -y install rpm-build createrepo
	sudo yum -y install redhat-rpm-config
	sudo yum groupinstall "Development Tools"a
	sudo yum install -y readline-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel byacc
	echo "cp .rpmmacros ~/"
	cp .rpmmacros ~/

redis:
	./download redis-2.6.11.tar.gz http://redis.googlecode.com/files/redis-2.6.11.tar.gz
	rpmbuild -ba SPECS/redis.spec

nodejs:
	./download node-v0.8.22.tar.gz http://nodejs.org/dist/v0.8.22/node-v0.8.22.tar.gz
	rpmbuild -ba SPECS/nodejs.spec

libyaml:
	./download yaml-0.1.4.tar.gz http://pyyaml.org/download/libyaml/yaml-0.1.4.tar.gz
	rpmbuild -ba SPECS/libyaml.spec

ruby19:
	./download ruby-1.9.3-p392.tar.gz http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p392.tar.gz
	rpmbuild -ba SPECS/ruby19.spec

ruby20:
	make libyaml
	sudo rpm -ivh RPMS/x86_64/libyaml-0.1.4-1.x86_64.rpm 
	./download ruby-2.0.0-p247.tar.gz ftp://ftp.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p247.tar.gz
	rpmbuild -ba SPECS/ruby20.spec

