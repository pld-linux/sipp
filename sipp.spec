#
# Conditional build:
%bcond_with	options_is_ping # make sipp treat OPTIONS same as PING
				# changes sipp behaviour, but that is
				# what everybody use for 'pinging'

Summary:	SIPp - a performance testing tool for the SIP protocol
Summary(pl.UTF-8):	SIPp - narzędzie do testowania wydajności protokołu SIP
Name:		sipp
Version:	3.6.0
Release:	3
License:	GPL v2+ except two files under BSD
Group:		Applications/Communications
#Source0Download: https://github.com/SIPp/sipp/releases/
Source0:	https://github.com/SIPp/sipp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1fd27333d179d786d3f6a67ee451fae9
Patch0:		%{name}-OPTIONS_is_ping.patch
URL:		http://sipp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gsl-devel
BuildRequires:	help2man
BuildRequires:	libpcap-devel
BuildRequires:	libsctp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIPp is a performance testing tool for the SIP protocol. It includes a
few basic SipStone user agent scenarios (UAC and UAS) and establishes
and releases multiple calls with the INVITE and BYE methods. It can
also reads XML scenario files describing any performance testing
configuration. It features the dynamic display of statistics about
running tests (call rate, round trip delay, and message statistics),
periodic CSV statistics dumps, TCP and UDP over multiple sockets or
multiplexed with retransmission management, regular expressions and
variables in scenario files, and dynamically adjustable call rates.

SIPp can be used to test many real SIP equipements like SIP proxies,
B2BUAs, SIP media servers, SIP/x gateways, SIP PBX, ... It is also
very useful to emulate thousands of user agents calling your SIP
system.

%description -l pl.UTF-8
SIPp to narzędzie do testowania wydajności protokołu SIP. Zawiera
kilka podstawowych scenrariuszy klienta SipStone (UAC i UAS);
nawiązuje i zwalnia wiele połączeń przy użyciu metod INVITE i BYE.
Potrafi czytać także pliki scenariuszy w formacie XML, opisujące
dowolną konfigurację testowania wydajności. Ma dynamiczne wyświetlanie
statystyk działających testów (częstość połączeń, opóźnienie pakietów,
statystyki komunikatów), okresowe zrzuty statystyk w formacie CSV,
połączenia TCP i UDP na wielu gniazdach lub miltipleksowane z
zarządzaniem retransmisją, wyrażenia regularne i zmienne w plikach
scenariuszy oraz dynamicznie modyfikowaną częstość połączeń.

SIPp może być używany do testowania wielu rzeczywistych urządzeń SIP,
takich jak proxy SIP, B2BUA, serwery mediów SIP, bramki SIP/x, PBX-y
SIP... Jest także przydatny do emulowania tysięcy klientów dzwoniących
do systemu SIP.

%prep
%setup -q
%{?with_options_is_ping:%patch0 -p1}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-epoll \
	--with-openssl \
	--with-pcap \
	--with-sctp \
	--with-gsl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.md THANKS
%attr(755,root,root) %{_bindir}/sipp
%{_mandir}/man1/sipp.1*
