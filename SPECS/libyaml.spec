%define ver  0.1.4
%define rel  1
%define jobs 2

Name:          libyaml
Version:       %{ver}
Release:       %{rel}
Summary:       yaml lib
Group:         Databases
License:       MIT license
URL:           http://pyyaml.org/wiki/LibYAML

Source0:       http://pyyaml.org/download/libyaml/yaml-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: libyaml
Obsoletes: libyaml

%description
YAML C lib. Useful for stopping Ruby from spamming countless warning messages

%prep
%setup -q -n yaml-%{version}

%build
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README
/usr/lib/libyaml.la
/usr/lib/libyaml-0.so.2
/usr/lib/pkgconfig/yaml-0.1.pc
/usr/lib/libyaml-0.so.2.0.2
/usr/lib/libyaml.a
/usr/lib/libyaml.so
/usr/include/yaml.h
