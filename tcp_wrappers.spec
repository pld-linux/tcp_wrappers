Summary:	Security wrapper for tcp daemons
Summary(de):	Sicherheitspackung fЭr tcp-DДmonen
Summary(es):	Programa de seguridad para daemons tcp
Summary(fr):	Enveloppe de sИcuritИ pour les dИmons tcp
Summary(pl):	Wrapper bezpieczeЯstwa dla demonСw tcp
Summary(pt_BR):	Programa de seguranГa para daemons tcp
Summary(ru):	Security wrapper для tcp-демонов
Summary(tr):	TCP sЭreГleri iГin gЭvenlik sarmalayЩcЩsЩ
Summary(uk):	Security wrapper для tcp-демон╕в
Name:		tcp_wrappers
Version:	7.6
Release:	31
License:	distributable
Group:		Networking/Admin
Source0:	ftp://ftp.porcupine.org/pub/security/%{name}_%{version}.tar.gz
# Source0-md5: e6fa25f71226d090f34de3f6b122fb5a
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
Patch8:		%{name}-weak-severity.patch
BuildRequires:	libtool
Requires:	libwrap = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services.

%description -l es
Con este paquete puedes monitorar y filtrar llamadas de SYSTAT,
FINGER, FTP, TElNET, RLOGIN, RSH, EXEC, TFTP, TALK, y otros servicios
de red.

%description -l fr
Avec ce paquetage, vous pouvez gИrer et filtrer les requЙtes entrantes
pour SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK et
autres services rИseau.

%description -l pl
Przy pomocy tego pakietu mo©na monitorowaФ i filtrowaФ nadchodz╠ce
©╠dania SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK i
innych usЁug sieciowych.

%description -l pt_BR
Com este pacote vocЙ pode monitorar e filtrar chamadas de SYSTAT,
FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, e outros serviГos
de rede.

%description -l ru
Этот пакет позволяет отслеживать и фильтровать входящие запросы к
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK и другим
сетевым сервисам.

%description -l tr
Bu paket, SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK
ve diПer aП hizmetleri iГin gelen istekleri izlemenizi ve isteПinize
gЖre sЭzmenizi saПlar.

%description -l uk
kЦей пакет дозволя╓ в╕дсл╕дковувати та ф╕льтрувати вх╕дн╕ запити до
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK та ╕нших
мережевих серв╕с╕в.

%package -n libwrap
Summary:	Security wrapper access control library
Summary(pl):	Biblioteka wrappera bezpieczeЯstwa
Summary(ru):	Security wrapper для tcp-демонов. Библиотеки разработчика и хедера
Summary(uk):	Security wrapper для tcp-демон╕в. Б╕бл╕отеки програм╕ста та хедери
Group:		Libraries
Requires(post):	/sbin/ldconfig
Requires(post):	fileutils
Conflicts:	tcp_wrappers < 7.6-28

%description -n libwrap
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap -l pl
Biblioteka wrappera bezpieczeЯstwa zawieraj╠ca implementacjЙ kontroli
dostЙpu bazuj╠c╠ na jЙzyku reguЁ, opcjonalnie z komendami powЁoki
wykowywanymi zale©nie od ustawionej reguЁki.

%package -n libwrap-devel
Summary:	Header file and documentation for security wrapper access control library
Summary(pl):	Plik nagЁСwkowy i dokumentacja do biblioteki wrappera bezpieczeЯstwa
Group:		Development/Libraries
Requires:	libwrap = %{version}-%{release}

%description -n libwrap-devel
Header file and programmer's documentation for libwrap, security
wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap-devel -l pl
Plik nagЁСwkowy i dokumentacja programisty do libwrap - biblioteki
wrappera bezpieczeЯstwa zawieraj╠cej implementacjЙ kontroli dostЙpu
bazuj╠c╠ na jЙzyku reguЁ, opcjonalnie z komendami powЁoki wykowywanymi
zale©nie od ustawionej reguЁki.

%description -n libwrap-devel -l ru
Этот пакет позволяет отслеживать и фильтровать входящие запросы к
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK и другим
сетевым сервисам.

Это библиотеки разработчика и хедера, необходимые для разработки
программ, использующих библиотеки tcp-wrapper'а.

%description -n libwrap-devel -l uk
Цей пакет дозволя╓ в╕дсл╕дковувати та ф╕льтрувати вх╕дн╕ запити до
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK та ╕нших
мережевих серв╕с╕в.

Це б╕бл╕отеки програм╕ста та хедери, необх╕дн╕ для розробки програм,
як╕ використовують б╕бл╕отеки tcp-wrapper'а.

%package -n libwrap-static
Summary:	Security wrapper access control library (static version)
Summary(pl):	Biblioteki wrappera bezpieczeЯstwa (wersja statyczna)
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolvimento com tcp_wrappers
Summary(ru):	Security wrapper для tcp-демонов. Статические библиотеки
Summary(uk):	Security wrapper для tcp-демон╕в. Статичн╕ б╕бл╕отеки
Group:		Development/Libraries
Requires:	libwrap-devel = %{version}-%{release}

%description -n libwrap-static
Static version of libwrap, security wrapper access control library
which implement a rule-based access control language with optional
shell commands that are executed when a rule fires.

%description -n libwrap-static -l pl
Statyczna wersja libwrap - biblioteki wrappera bezpieczeЯstwa
zawieraj╠cej implementacjЙ kontroli dostЙpu bazuj╠c╠ na jЙzyku reguЁ,
opcjonalnie z komendami powЁoki wykowywanymi zale©nie od ustawionej
reguЁki.

%description -n libwrap-static -l pt_BR
Bibliotecas e arquivos de inclusao para desenvolvimento com
tcp_wrappers.

%description -n libwrap-static -l ru
Этот пакет позволяет отслеживать и фильтровать входящие запросы к
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK и другим
сетевым сервисам.

Это статические библиотеки, необходимые для разработки программ,
использующих библиотеки tcp-wrapper'а.

%description -n libwrap-static -l uk
Цей пакет дозволя╓ в╕дсл╕дковувати та ф╕льтрувати вх╕дн╕ запити до
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK та ╕нших
мережевих серв╕с╕в.

Це статичн╕ б╕бл╕отеки, необх╕дн╕ для розробки програм, як╕
використовують б╕бл╕отеки tcp-wrapper'а.

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
%patch8 -p1

%build
%{__make} linux \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

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

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libwrap
/sbin/ldconfig
if [ -f /etc/hosts.allow -o -f /etc/host.deny ]; then
	if [ ! -L /etc/hosts.allow ]; then
		mv -f /etc/tcpd/hosts.allow /etc/tcpd/hosts.allow.newrpm
		mv -f /etc/hosts.allow /etc/tcpd
	fi
	if [ ! -L /etc/tcpd/hosts.deny ]; then
		mv -f /etc/tcpd/hosts.deny  /etc/tcpd/hosts.deny.newrpm
		mv -f /etc/hosts.deny /etc/tcpd
	fi
fi

%postun -n libwrap -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%{_mandir}/man8/*
%attr(755,root,root) %{_sbindir}/*

%files -n libwrap
%defattr(644,root,root,755)
%dir %{_sysconfdir}/tcpd
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
