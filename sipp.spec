
%bcond_with	options_is_ping # make sipp treat OPTIONS same as PING
				# changes sipp behaviour, but that is
				# what everybody use for 'pinging'

Summary:	SIPp - a performance testing tool for the SIP protocol
Name:		sipp
Version:	3.5.1
Release:	2
License:	GPL v2+ except two files under BSD
Group:		Applications
Source0:	https://github.com/SIPp/sipp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c14e4c84975337ce952f03a38ddba7ec
Patch0:		%{name}-OPTIONS_is_ping.patch
URL:		http://sipp.sourceforge.net/
BuildRequires:	gsl-devel
BuildRequires:	libpcap-devel
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

%prep
%setup -q
%{?with_options_is_ping:%patch0 -p1}

%build
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
%doc CHANGES.md FAQ.md README.md THANKS
%attr(755,root,root) %{_bindir}/sipp
%{_mandir}/man1/sipp.1*
