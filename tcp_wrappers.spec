Summary:	Security wrapper for tcp daemons
Summary(de):	Sicherheitspackung für tcp-Dämonen
Summary(fr):	Enveloppe de sécurité pour les démons tcp
Summary(pl):	Wrapper bezpieczeñstwa dla demonów tcp
Summary(tr):	TCP süreçleri için güvenlik sarmalayýcýsý
Name:		tcp_wrappers
Version:	7.6
Release:	27
License:	distributable
Group:		Networking/Admin
Source0:	ftp://ftp.porcupine.org/pub/security/%{name}_%{version}.tar.gz
Source1:	hosts.allow
Source2:	hosts.deny
Patch0:		http://www.imasy.or.jp/~ume/ipv6/%{name}_7.6-ipv6-1.9.diff.gz
Patch1:		%{name}-fix.patch
Patch2:		%{name}-bug11881.patch
Patch3:		%{name}-bug17795.patch
Patch4:		%{name}-bug17847.patch
Patch5:		%{name}-fixgethostbyname.patch
Patch6:		%{name}-alarm.patch
Patch7:		%{name}-man_fixes.patch
BuildRequires:	libtool
Requires:	libwrap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services.

%description -l fr
Avec ce paquetage, vous pouvez gérer et filtrer les requêtes entrantes
pour SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK et
autres services réseau.

%description -l pl
Z tym pakietem mo¿esz monitorowaæ i filtrowaæ nadchodz±ce pro¶by do
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, i innych
us³ug sieciowych.

%description -l tr
Bu paket, SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK
ve diðer að hizmetleri için gelen istekleri izlemenizi ve isteðinize
göre süzmenizi saðlar.

%package -n libwrap
Summary:	Security wrapper access control library
Summary(pl):	Biblioteki wrappera bezpieczeñstwa
Group:		Libraries
Requires(post):	/sbin/ldconfig

%description -n libwrap
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap -l pl
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê
kontroli dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami
pow³oki wykowywanymi zale¿nie od ustawionej regu³ki.

%package -n libwrap-devel
Summary:	Security wrapper access control library
Summary(pl):	Biblioteki wrappera bezpieczeñstwa
Group:		Libraries
Requires:	libwrap = %{version}-%{release}

%description -n libwrap-devel
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap-devel -l pl
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê
kontroli dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami
pow³oki wykowywanymi zale¿nie od ustawionej regu³ki.

%package -n libwrap-static
Summary:	Security wrapper access control library (static version)
Summary(pl):	Biblioteki wrappera bezpieczeñstwa (wersja statyczna)
Group:		Libraries
Requires:	libwrap-devel = %{version}-%{release}

%description -n libwrap-static
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap-static -l pl
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê
kontroli dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami
pow³oki wykowywanymi zale¿nie od ustawionej regu³ki.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__make} linux CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/tcpd \
	$RPM_BUILD_ROOT{%{_mandir}/man{3,5,8},%{_libdir},%{_includedir},%{_sbindir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install	hosts_access.3			$RPM_BUILD_ROOT%{_mandir}/man3
install {hosts_access,hosts_options}.5	$RPM_BUILD_ROOT%{_mandir}/man5
install {tcpd,tcpdchk,tcpdmatch}.8	$RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/tcpd

echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.allow.5
echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.deny.5

%post -n libwrap
/sbin/ldconfig
if [ -f /etc/hosts.allow -o -f /etc/host.deny ]; then
	mv -f /etc/tcpd/hosts.allow /etc/tcpd/hosts.allow.newrpm
	mv -f /etc/tcpd/hosts.deny  /etc/tcpd/hosts.deny.newrpm
	mv -f /etc/hosts.{allow,deny} /etc/tcpd
fi

%postun -n libwrap -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%dir %{_sysconfdir}/tcpd
%{_mandir}/man8/*
%attr(755,root,root) %{_sbindir}/*

%files -n libwrap
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tcpd/hosts.*
%attr(755,root,root) %{_libdir}/libwrap.so.*.*
%{_mandir}/man5/*

%files -n libwrap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwrap.so
%{_libdir}/libwrap.la
%{_includedir}/tcpd.h
%{_mandir}/man3/*

%files -n libwrap-static
%defattr(644,root,root,755)
%{_libdir}/libwrap.a
