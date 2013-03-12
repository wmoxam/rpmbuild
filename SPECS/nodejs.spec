%define ver  0.8.22
%define rel  1
%define jobs 2

Name:          nodejs
Version:       %{ver}
Release:       %{rel}
Summary:       Node.js programs
Group:         Applications/Internet
License:       Copyright Joyent, Inc. and other Node contributors.
URL:           http://nodejs.org

Source0:       http://nodejs.org/dist/node-v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python >= 2.6, openssl-devel, gcc-c++

Provides: nodejs
Obsoletes: nodejs

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model. This allows Node.js to get excellent performance based on
the architectures of many Internet applications.

%prep
%setup -q -n node-v%{version}

%build
export JOBS=%{jobs}
python ./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README.md

/usr/bin/node
/usr/bin/npm
/usr/bin/node-waf
/usr/include/node
/usr/share/man/man1/node.1.gz
/usr/lib/node
/usr/lib/node_modules
/usr/lib/dtrace/node.d
