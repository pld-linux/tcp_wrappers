Summary:     Security wrapper for tcp daemons
Summary(de): Sicherheitspackung für tcp-Dämonen 
Summary(fr): Enveloppe de sécurité pour les démons tcp
Summary(pl): Wrapper bezpieczeñstwa dla demonów tcp
Summary(tr): TCP süreçleri için güvenlik sarmalayýcýsý
Name:        tcp_wrappers
Version:     7.6
Release:     7
Copyright:   Distributable
Group:       Networking/Admin
Source:      ftp://coast.cs.purdue.edu/pub/tools/unix/tcp_wrappers/%{name}_%{version}.tar.gz
Source1:     hosts.allow
Source2:     hosts.deny
Patch:       tcpw-config.patch
Patch1:      tcpw7.2-setenv.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
Summary:     Security wrapper access control library
Summary(pl): Biblioteki wrappera bezpieczeñstwa
Group:       Libraries

%description -n libwrap
Security wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed when a rule
fires.

%description -l pl -n libwrap
Biblioteki wrappera bezpieczeñstwa, które zawieraj± implementacjê kontroli
dostêpu bazuj±c± na jêzyku regu³, opcjonalnie z komendami pow³oki wykowywanymi
zale¿nie od ustawionej regu³ki.

%prep
%setup -q -n %{name}_%{version}
%patch -p1 -b .config
%patch1 -p1 -b .setenv

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/tcpd,usr/{man/man{3,5,8},lib,include,sbin}}

install hosts_access.3 $RPM_BUILD_ROOT/usr/man/man3
install {hosts_access,hosts_options}.5 $RPM_BUILD_ROOT/usr/man/man5
install {tcpd,tcpdchk,tcpdmatch}.8 $RPM_BUILD_ROOT/usr/man/man8

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/tcpd

echo ".so hosts_access.5" > $RPM_BUILD_ROOT/usr/man/man5/hosts.allow.5
echo ".so hosts_access.5" > $RPM_BUILD_ROOT/usr/man/man5/hosts.deny.5

install libwrap.a $RPM_BUILD_ROOT/usr/lib
install tcpd.h $RPM_BUILD_ROOT/usr/include
install -s safe_finger tcpd tcpdchk tcpdmatch try-from $RPM_BUILD_ROOT/usr/sbin

%post
if [ -f /etc/hosts.allow -o -f /etc/host.deny ]; then
	mv /etc/tcpd/hosts.allow /etc/tcpd/hosts.allow.newrpm
	mv /etc/tcpd/hosts.deny  /etc/tcpd/hosts.deny.newrpm
	mv /etc/hosts.{allow,deny} /etc/tcpd
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%attr(700, root, root) %dir /etc/tcpd
%config %verify(not md5 mtime size) /etc/tcpd/hosts.*
%attr(644, root,  man) /usr/man/man[58]/*
%attr(755, root, root) /usr/sbin/*

%files -n libwrap
%defattr(644, root, root)
/usr/include/tcpd.h
/usr/lib/libwrap.a
%attr(644, root,  man) /usr/man/man3/*

%changelog
* Sun Nov  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [7.6-7]
- in tcpw-config.patch added modifications informs that hosts.{allow,deny}
  files now placed in /etc/tcpd,
- changed permission on /etc/tcpd to 700.

* Sat Sep 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [7.6-6]
- added pl translation.

* Thu Aug 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
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

* Thu Jun 25 1998 Alan Cox <alan@redhat.com>
- Erp where did the Dec 05 patch escape to

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- don't build setenv.o module -- it just breaks things

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- upgrade to 7.6

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Upgraded to version 7.5
- Uses a build root
