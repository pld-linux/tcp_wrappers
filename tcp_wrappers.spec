Summary:	Security wrapper for tcp daemons
Summary(de):	Sicherheitspackung f�r tcp-D�monen 
Summary(fr):	Enveloppe de s�curit� pour les d�mons tcp
Summary(pl):	Wrapper bezpiecze�stwa dla demon�w tcp
Summary(tr):	TCP s�re�leri i�in g�venlik sarmalay�c�s�
Name:		tcp_wrappers
Version:	7.6
Release:	9
Copyright:	Distributable
Group:		Networking/Admin
Group(pl):	Sieciowe/Administacyjne
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/tcp_wrappers/%{name}_%{version}.tar.gz
Source1:	hosts.allow
Source2:	hosts.deny
Patch0:		tcp_wrappers-config.patch
Patch1:		tcp_wrappers-inet_dir.patch
Patch2:		tcp_wrappers-doc_fix.patch
Patch3:		tcp_wrappers-ipv6.patch
Patch4:		tcp_wrappers-setenv.patch
Requires:	inetd
Buildroot:	/tmp/%{name}-%{version}-root

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services.

%description -l fr
Avec ce paquetage, vous pouvez g�rer et filtrer les requ�tes entrantes pour
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK et autres services
r�seau.

%description -l pl
Z tym pakietem mo�esz monitorowa� i filtrowa� nadchodz�ce pro�by do
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, i innych
us�ug sieciowych.

%description -l tr
Bu paket, SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK ve di�er
a� hizmetleri i�in gelen istekleri izlemenizi ve iste�inize g�re s�zmenizi
sa�lar.

%package -n libwrap
Summary:	Security wrapper access control library
Summary(pl):	Biblioteki wrappera bezpiecze�stwa
Group:		Libraries
Group(pl):	Biblioteki

%description -n libwrap
Security wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed when a rule
fires.

%description -l pl -n libwrap
Biblioteki wrappera bezpiecze�stwa, kt�re zawieraj� implementacj� kontroli
dost�pu bazuj�c� na j�zyku regu�, opcjonalnie z komendami pow�oki wykowywanymi
zale�nie od ustawionej regu�ki.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make linux RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DINET6"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/tcpd \
	$RPM_BUILD_ROOT{%{_mandir}/man{3,5,8},%{_libdir},%{_includedir},%{_sbindir}}

install hosts_access.3 $RPM_BUILD_ROOT%{_mandir}/man3
install {hosts_access,hosts_options}.5 $RPM_BUILD_ROOT%{_mandir}/man5
install {tcpd,tcpdchk,tcpdmatch}.8 $RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/tcpd

echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.allow.5
echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.deny.5

install libwrap.a $RPM_BUILD_ROOT%{_libdir}
install tcpd.h $RPM_BUILD_ROOT%{_includedir}
install -s safe_finger tcpd tcpdchk tcpdmatch try-from $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	BLURB CHANGES README* DISCLAIMER

%post
if [ -f /etc/hosts.allow -o -f /etc/host.deny ]; then
	mv /etc/tcpd/hosts.allow /etc/tcpd/hosts.allow.newrpm
	mv /etc/tcpd/hosts.deny  /etc/tcpd/hosts.deny.newrpm
	mv /etc/hosts.{allow,deny} /etc/tcpd
fi

if [ -f /var/lock/subsys/inetd ]; then
	/etc/rc.d/init.d/inetd restart &>/dev/null
fi     

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz Banners.Makefile
%attr(750,root,bin) %dir /etc/tcpd
%attr(640,root,bin) %config %verify(not md5 mtime size) /etc/tcpd/hosts.*
%{_mandir}/man[58]/*

%attr(755,root,root) %{_sbindir}/*

%files -n libwrap
%defattr(644,root,root,755)
%{_includedir}/tcpd.h
%{_libdir}/libwrap.a
%{_mandir}/man3/*

%changelog
* Thu Apr 15 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [7.6-8]
- added gzipping %doc,
- Fix: set <uid>.<gid> to root.bin on /etc/tcpd.

* Wed Nov 18 1998  Wojtek �lusarczyk <wojtek@SHADOW.EU.ORG>
- added some patches prepared by Maciej W. R�ycki <macro@amg.gda.pl>.

* Sun Nov  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [7.6-7]
- in tcpw-config.patch added modifications informs that hosts.{allow,deny}
  files now placed in /etc/tcpd,
- changed permission on /etc/tcpd to 750

* Sat Sep 26 1998 Arkadiusz Mi�kiewicz <misiek@misiek.eu.org>
  [7.6-6]
- added pl translation.

* Thu Aug 18 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [7.6-5]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source and %setup,
- added libwrap subpackage,
- fiew simplification in %install,
- hosts.{allow,deny} moved to this package to separated directoty /etc/tcpd
  for this files and banners from setup (also added %verify rules for
  this files),
- hosts.allow(5) and hosts.deny(5) man pages are now maked as nroff include
  to hosts_access(5) instead making sym link to hosts_access.5 (this allow
  compress man pages in future),
- added %post section with moving previouse hosts.{allow,deny} to /etc/tcpd,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).
