Summary:	Security wrapper for tcp daemons
Summary(de):	Sicherheitspackung für tcp-Dämonen 
Summary(fr):	Enveloppe de sécurité pour les démons tcp
Summary(pl):	Wrapper bezpieczeñstwa dla demonów tcp
Summary(tr):	TCP süreçleri için güvenlik sarmalayýcýsý
Name:		tcp_wrappers
Version:	7.6
Release:	11
Copyright:	Distributable
Group:		Networking/Admin
Group(pl):	Sieciowe/Administacyjne
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/tcp_wrappers/%{name}_%{version}.tar.gz
Source1:	hosts.allow
Source2:	hosts.deny
Patch0:		tcp_wrappers-config.patch
Patch1:		tcp_wrappers-inet_dir.patch
Patch2:		tcp_wrappers-doc_fix.patch
Patch3:		tcp_wrappers-debian.patch
Patch4:		tcp_wrappers_7.6_ume_IPv6.patch
Buildroot:	/tmp/%{name}-%{version}-root
Requires:	libwrap

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services.

%description -l fr
Avec ce paquetage, vous pouvez gérer et filtrer les requêtes entrantes pour
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK et autres services
réseau.

%description -l pl
Z tym pakietem mo¿esz monitorowaæ i filtrowaæ nadchodz±ce pro¶by do
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, i innych
us³ug sieciowych.

%description -l tr
Bu paket, SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK ve diðer
að hizmetleri için gelen istekleri izlemenizi ve isteðinize göre süzmenizi
saðlar.

%package -n libwrap
Summary:	Security wrapper access control library
Summary(pl):	Biblioteki wrappera bezpieczeñstwa
Group:		Libraries
Group(pl):	Biblioteki

%description -n libwrap
Security wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed when a rule
fires.

%description -l pl -n libwrap
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê kontroli
dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami pow³oki wykowywanymi
zale¿nie od ustawionej regu³ki.

%package -n libwrap-static
Summary:        Security wrapper access control library (static version)
Summary(pl):    Biblioteki wrappera bezpieczeñstwa (wersja statyczna)
Group:          Libraries
Group(pl):      Biblioteki

%description -n libwrap-static
Security wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed when a rule
fires.

%description -l pl -n libwrap-static
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê kontroli
dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami pow³oki wykowywanymi
zale¿nie od ustawionej regu³ki.

%package -n libwrap-devel
Summary:        Security wrapper access control library
Summary(pl):    Biblioteki wrappera bezpieczeñstwa
Group:          Libraries
Group(pl):      Biblioteki
Requires:	libwrap

%description -n libwrap-devel
Security wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed when a rule
fires.

%description -l pl -n libwrap-devel
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê kontroli
dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami pow³oki wykowywanymi
zale¿nie od ustawionej regu³ki.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/tcpd \
	$RPM_BUILD_ROOT{%{_mandir}/man{3,5,8},%{_libdir},%{_includedir},%{_sbindir}}

make install PREFIX=$RPM_BUILD_ROOT/usr
install hosts_access.3 $RPM_BUILD_ROOT%{_mandir}/man3
install {hosts_access,hosts_options}.5 $RPM_BUILD_ROOT%{_mandir}/man5
install {tcpd,tcpdchk,tcpdmatch}.8 $RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/tcpd

echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.allow.5
echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.deny.5

make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	BLURB CHANGES README* DISCLAIMER

%post
if [ -f /etc/hosts.allow -o -f /etc/host.deny ]; then
	mv /etc/tcpd/hosts.allow /etc/tcpd/hosts.allow.newrpm
	mv /etc/tcpd/hosts.deny  /etc/tcpd/hosts.deny.newrpm
	mv /etc/hosts.{allow,deny} /etc/tcpd
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz Banners.Makefile
%dir /etc/tcpd
%config(noreplace) %verify(not md5 mtime size) /etc/tcpd/hosts.*
%{_mandir}/man[58]/*

%attr(755,root,root) %{_sbindir}/*

%files -n libwrap-devel
%defattr(644,root,root,755)
%{_includedir}/tcpd.h
%{_mandir}/man3/*

%files -n libwrap
%defattr(644,root,root,755)
%{_libdir}/libwrap.s*

%files -n libwrap-static
%defattr(644,root,root,755)
%{_libdir}/libwrap.a
