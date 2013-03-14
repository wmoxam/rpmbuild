%define _prefix         /usr/local
%define _datadir        /usr/local/share
%define _mandir         /usr/local/share/man
%define ver  2.6.11
%define rel  1

Name:          redis
Version:       %{ver}
Release:       %{rel}
Summary:       Redis Server
Group:         Applications/Internet
License:       BSD
URL:           http://nodejs.org

Source0:       http://redis.googlecode.com/files/redis-%{ver}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make
Requires(post): /sbin/chkconfig /usr/sbin/useradd
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service
Provides: redis

%description
Redis is a key-value database. It is similar to memcached but the dataset is
not volatile, and values can be strings, exactly like in memcached, but also
lists and sets with atomic operations to push/pop elements.


%prep
%setup

%{__cat} <<EOF >redis.logrotate
%{_localstatedir}/log/redis/*log {
    missingok
}
EOF

%{__cat} <<'EOF' >redis.sysv
#!/bin/sh
#
# redis        init file for starting up the redis daemon
#
# chkconfig:   - 20 80
# description: Starts and stops the redis daemon.

# Source function library.
. /etc/rc.d/init.d/functions

name="redis-server"
exec="/usr/local/sbin/$name"
pidfile="/var/run/redis/redis.pid"
REDIS_CONFIG="/etc/redis.conf"

[ -e /etc/sysconfig/redis ] && . /etc/sysconfig/redis

lockfile=/var/lock/subsys/redis

start() {
    [ -f $REDIS_CONFIG ] || exit 6
    [ -x $exec ] || exit 5
    echo -n $"Starting $name: "
    daemon --user ${REDIS_USER-redis} "$exec $REDIS_CONFIG"
    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
    return $retval
}

stop() {
    echo -n $"Stopping $name: "
    killproc -p $pidfile $name
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
    return $retval
}

restart() {
    stop
    start
}

reload() {
    false
}

rh_status() {
    status -p $pidfile $name
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}


case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
        restart
        ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart}"
        exit 2
esac
exit $?
EOF


%build
%{__make}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%{__install} -Dp -m 0755 src/redis-server %{buildroot}%{_sbindir}/redis-server
%{__install} -Dp -m 0755 src/redis-benchmark %{buildroot}%{_bindir}/redis-benchmark
%{__install} -Dp -m 0755 src/redis-cli %{buildroot}%{_bindir}/redis-cli

%{__install} -Dp -m 0755 redis.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/redis
%{__install} -Dp -m 0755 redis.sysv %{buildroot}%{_sysconfdir}/init.d/redis
%{__install} -Dp -m 0644 redis.conf %{buildroot}%{_sysconfdir}/redis.conf
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/lib/redis
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/log/redis
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/run/redis
%{__install} -p -d -m 0755 %{buildroot}%{pid_dir}

%pre
/usr/sbin/useradd -c 'Redis' -u 6379 -s /bin/false -r -d %{_localstatedir}/lib/redis redis 2> /dev/null || :

%preun
if [ $1 = 0 ]; then
    # make sure redis service is not running before uninstalling

    # when the preun section is run, we've got stdin attached.  If we
    # call stop() in the redis init script, it will pass stdin along to
    # the redis-cli script; this will cause redis-cli to read an extraneous
    # argument, and the redis-cli shutdown will fail due to the wrong number
    # of arguments.  So we do this little bit of magic to reconnect stdin
    # to the terminal
    term="/dev/$(ps -p$$ --no-heading | awk '{print $2}')"
    exec < $term

    /sbin/service redis stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del redis
fi

%post
/sbin/chkconfig --add redis

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/redis-server
%{_bindir}/redis-benchmark
%{_bindir}/redis-cli
%{_sysconfdir}/init.d/redis
%config(noreplace) %{_sysconfdir}/redis.conf
%{_sysconfdir}/logrotate.d/redis
%dir %attr(0770,redis,redis) %{_localstatedir}/lib/redis
%dir %attr(0755,redis,redis) %{_localstatedir}/log/redis
%dir %attr(0755,redis,redis) %{_localstatedir}/run/redis
