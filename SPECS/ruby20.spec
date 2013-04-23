%define _prefix  	/usr/local
%define _datadir        /usr/local/share
%define _mandir		/usr/local/share/man
%define _libdir		/usr/local/lib
%define _includedir	/usr/local/include
%define rubyver         2.0.0
%define rubyminorver    p0

Name:           PresslyRuby20
Version:        %{rubyver}%{rubyminorver}
Release:        1%{?dist}
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/

Source0:        http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-%{rubyver}-%{rubyminorver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libyaml readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make

Provides: presslyruby20
Obsoletes: presslyruby20

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -q -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --prefix /usr/local \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}

