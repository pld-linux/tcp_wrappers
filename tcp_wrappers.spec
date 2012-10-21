Summary:	Security wrapper for tcp daemons
Summary(de.UTF-8):	Sicherheitspackung für tcp-Dämonen
Summary(es.UTF-8):	Programa de seguridad para daemons tcp
Summary(fr.UTF-8):	Enveloppe de sécurité pour les démons tcp
Summary(pl.UTF-8):	Wrapper bezpieczeństwa dla demonów tcp
Summary(pt_BR.UTF-8):	Programa de segurança para daemons tcp
Summary(ru.UTF-8):	Security wrapper для tcp-демонов
Summary(tr.UTF-8):	TCP süreçleri için güvenlik sarmalayıcısı
Summary(uk.UTF-8):	Security wrapper для tcp-демонів
Name:		tcp_wrappers
Version:	7.6
Release:	46
License:	distributable
Group:		Networking/Admin
Source0:	ftp://ftp.porcupine.org/pub/security/%{name}_%{version}.tar.gz
# Source0-md5:	e6fa25f71226d090f34de3f6b122fb5a
Source1:	hosts.allow
Source2:	hosts.deny
Patch0:		%{name}-usagi-ipv6.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-bug11881.patch
Patch3:		%{name}-bug17795.patch
Patch4:		%{name}-bug17847.patch
Patch5:		%{name}-fixgethostbyname.patch
Patch6:		%{name}-alarm.patch
Patch7:		%{name}-man_fixes.patch
Patch8:		%{name}-162412.patch
Patch9:		%{name}-196326.patch
Patch10:	%{name}-sig.patch
Patch11:	%{name}-strerror.patch
Patch12:	%{name}-sigchld.patch
Patch13:	%{name}-safe_finger.patch
Patch14:	%{name}-docs.patch
Patch15:	%{name}-220015.patch
Patch16:	%{name}-Makefile.patch
BuildRequires:	libtool
Requires:	libwrap = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this package you can monitor and filter incoming requests for the
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, and other
network services.

%description -l es.UTF-8
Con este paquete puedes monitorar y filtrar llamadas de SYSTAT,
FINGER, FTP, TElNET, RLOGIN, RSH, EXEC, TFTP, TALK, y otros servicios
de red.

%description -l fr.UTF-8
Avec ce paquetage, vous pouvez gérer et filtrer les requêtes entrantes
pour SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK et
autres services réseau.

%description -l pl.UTF-8
Przy pomocy tego pakietu można monitorować i filtrować nadchodzące
żądania SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK i
innych usług sieciowych.

%description -l pt_BR.UTF-8
Com este pacote você pode monitorar e filtrar chamadas de SYSTAT,
FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK, e outros serviços
de rede.

%description -l ru.UTF-8
Этот пакет позволяет отслеживать и фильтровать входящие запросы к
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK и другим
сетевым сервисам.

%description -l tr.UTF-8
Bu paket, SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK
ve diğer ağ hizmetleri için gelen istekleri izlemenizi ve isteğinize
göre süzmenizi sağlar.

%description -l uk.UTF-8
kЦей пакет дозволяє відслідковувати та фільтрувати вхідні запити до
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK та інших
мережевих сервісів.

%package -n libwrap
Summary:	Security wrapper access control library
Summary(pl.UTF-8):	Biblioteka wrappera bezpieczeństwa
Summary(ru.UTF-8):	Security wrapper для tcp-демонов. Библиотеки разработчика и хедера
Summary(uk.UTF-8):	Security wrapper для tcp-демонів. Бібліотеки програміста та хедери
Group:		Libraries
Requires(post):	fileutils
Requires:	libwrap-libs = %{version}-%{release}
Conflicts:	tcp_wrappers < 7.6-28

%description -n libwrap
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap -l pl.UTF-8
Biblioteka wrappera bezpieczeństwa zawierająca implementację kontroli
dostępu bazującą na języku reguł, opcjonalnie z komendami powłoki
wykowywanymi zależnie od ustawionej regułki.

%package -n libwrap-libs
Summary:	Security wrapper access control library
Summary(pl.UTF-8):	Biblioteka wrappera bezpieczeństwa
Group:		Libraries
Conflicts:	tcp_wrappers < 7.6-28

%description -n libwrap-libs
Security wrapper access control library which implement a rule-based
access control language with optional shell commands that are executed
when a rule fires.

%description -n libwrap-libs -l pl.UTF-8
Biblioteka wrappera bezpieczeństwa zawierająca implementację kontroli
dostępu bazującą na języku reguł, opcjonalnie z komendami powłoki
wykowywanymi zależnie od ustawionej regułki.

%package -n libwrap-devel
Summary:	Header file and documentation for security wrapper access control library
Summary(pl.UTF-8):	Plik nagłówkowy i dokumentacja do biblioteki wrappera bezpieczeństwa
Group:		Development/Libraries
Requires:	libwrap-libs = %{version}-%{release}

%description -n libwrap-devel
Header file and programmer's documentation for libwrap, security
wrapper access control library which implement a rule-based access
control language with optional shell commands that are executed when a
rule fires.

%description -n libwrap-devel -l pl.UTF-8
Plik nagłówkowy i dokumentacja programisty do libwrap - biblioteki
wrappera bezpieczeństwa zawierającej implementację kontroli dostępu
bazującą na języku reguł, opcjonalnie z komendami powłoki wykowywanymi
zależnie od ustawionej regułki.

%description -n libwrap-devel -l ru.UTF-8
Этот пакет позволяет отслеживать и фильтровать входящие запросы к
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK и другим
сетевым сервисам.

Это библиотеки разработчика и хедера, необходимые для разработки
программ, использующих библиотеки tcp-wrapper'а.

%description -n libwrap-devel -l uk.UTF-8
Цей пакет дозволяє відслідковувати та фільтрувати вхідні запити до
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK та інших
мережевих сервісів.

Це бібліотеки програміста та хедери, необхідні для розробки програм,
які використовують бібліотеки tcp-wrapper'а.

%package -n libwrap-static
Summary:	Security wrapper access control library (static version)
Summary(pl.UTF-8):	Biblioteki wrappera bezpieczeństwa (wersja statyczna)
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento com tcp_wrappers
Summary(ru.UTF-8):	Security wrapper для tcp-демонов. Статические библиотеки
Summary(uk.UTF-8):	Security wrapper для tcp-демонів. Статичні бібліотеки
Group:		Development/Libraries
Requires:	libwrap-devel = %{version}-%{release}

%description -n libwrap-static
Static version of libwrap, security wrapper access control library
which implement a rule-based access control language with optional
shell commands that are executed when a rule fires.

%description -n libwrap-static -l pl.UTF-8
Statyczna wersja libwrap - biblioteki wrappera bezpieczeństwa
zawierającej implementację kontroli dostępu bazującą na języku reguł,
opcjonalnie z komendami powłoki wykowywanymi zależnie od ustawionej
regułki.

%description -n libwrap-static -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusao para desenvolvimento com
tcp_wrappers.

%description -n libwrap-static -l ru.UTF-8
Этот пакет позволяет отслеживать и фильтровать входящие запросы к
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK и другим
сетевым сервисам.

Это статические библиотеки, необходимые для разработки программ,
использующих библиотеки tcp-wrapper'а.

%description -n libwrap-static -l uk.UTF-8
Цей пакет дозволяє відслідковувати та фільтрувати вхідні запити до
SYSTAT, FINGER, FTP, TELNET, RLOGIN, RSH, EXEC, TFTP, TALK та інших
мережевих сервісів.

Це статичні бібліотеки, необхідні для розробки програм, які
використовують бібліотеки tcp-wrapper'а.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
%{__make} linux \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/tcpd \
	$RPM_BUILD_ROOT{%{_mandir}/man{3,5,8},%{_libdir}} \
	$RPM_BUILD_ROOT{/%{_lib},%{_includedir},%{_sbindir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

mv $RPM_BUILD_ROOT%{_libdir}/libwrap.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo libwrap.so.*.*.*) \
        $RPM_BUILD_ROOT%{_libdir}/libwrap.so

cp -p hosts_access.3			$RPM_BUILD_ROOT%{_mandir}/man3
cp -p {hosts_access,hosts_options}.5	$RPM_BUILD_ROOT%{_mandir}/man5
cp -p {tcpd,tcpdchk,tcpdmatch}.8	$RPM_BUILD_ROOT%{_mandir}/man8

cp -p %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/tcpd

echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.allow.5
echo ".so hosts_access.5" > $RPM_BUILD_ROOT%{_mandir}/man5/hosts.deny.5

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libwrap
if [ -f /etc/hosts.allow -o -f /etc/host.deny ]; then
	if [ ! -L /etc/hosts.allow ]; then
		mv -f /etc/tcpd/hosts.allow{,.rpmnew}
		mv -f /etc/hosts.allow /etc/tcpd
	fi
	if [ ! -L /etc/tcpd/hosts.deny ]; then
		mv -f /etc/tcpd/hosts.deny{,.rpmnew}
		mv -f /etc/hosts.deny /etc/tcpd
	fi
fi

%post	-n libwrap-libs -p /sbin/ldconfig
%postun	-n libwrap-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%attr(755,root,root) %{_sbindir}/safe_finger
%attr(755,root,root) %{_sbindir}/tcpd
%attr(755,root,root) %{_sbindir}/tcpdchk
%attr(755,root,root) %{_sbindir}/tcpdmatch
%attr(755,root,root) %{_sbindir}/try-from
%{_mandir}/man8/tcpd.8*
%{_mandir}/man8/tcpdchk.8*
%{_mandir}/man8/tcpdmatch.8*

%files -n libwrap
%defattr(644,root,root,755)
%dir %{_sysconfdir}/tcpd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tcpd/hosts.allow
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tcpd/hosts.deny
%{_mandir}/man5/hosts.allow.5*
%{_mandir}/man5/hosts.deny.5*
%{_mandir}/man5/hosts_access.5*
%{_mandir}/man5/hosts_options.5*

%files -n libwrap-libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libwrap.so.*.*
%attr(755,root,root) %ghost /%{_lib}/libwrap.so.0

%files -n libwrap-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwrap.so
%{_libdir}/libwrap.la
%{_includedir}/tcpd.h
%{_mandir}/man3/*

%files -n libwrap-static
%defattr(644,root,root,755)
%{_libdir}/libwrap.a
