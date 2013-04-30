RPM Dev env
-----------

Custom RPMs for OSs with outdated/missing packages
*glares at Amazon Linux* 

To develop packages:

    $ vagrant up
    $ git clone https://github.com/wmoxam/rpmbuild
    $ cd rpmbuild && make setup

    add/edit a spec in rpmbuild/SPEC
    add build deps, etc to Makefile
    
    $ make 'name_of_package'


Hosting

    $ s3cmd --configure
    $ make upload name_of_package

