RPM Dev env
-----------

Custom RPMs for OSs with outdated/missing packages
*glares at Amazon Linux* 

To develop packages:

    $ vagrant up
    $ git clone https://github.com/wmoxam/rpmbuild
    
    add/edit a spec in rpmbuild/SPEC

    $ rpmbuild -ba SPEC/whatever.spec

For easy hosting this looks reasonable: https://github.com/jbraeuer/yum-s3-plugin

