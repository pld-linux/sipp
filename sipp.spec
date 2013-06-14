
%bcond_with	options_is_ping # make sipp treat OPTIONS same as PING
				# changes sipp behaviour, but that is
				# what everybody use for 'pinging'

Summary:	SIPp - a performance testing tool for the SIP protocol
Name:		sipp
Version:	3.3
Release:	1
License:	GPL v2+ except two files under BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/sipp/%{name}-%{version}.tar.xz
# Source0-md5:	f0c4f472fa86de8a528cb91616323617
Patch0:		%{name}-headers.patch
Patch1:		%{name}-sprintf.patch
Patch2:		%{name}-stats_crash.patch
Patch3:		%{name}-OPTIONS_is_ping.patch
URL:		http://sipp.sourceforge.net/
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_options_is_ping:%patch3 -p1}

%build

%{__make} pcapplay_ossl \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CCLINK="%{__cxx}" \
	EXTRACFLAGS="%{rpmcflags}" \
	EXTRACPPFLAGS="%{rpmcxxflags}" \
	EXTRALFLAGS="%{rpmldflags}" \
	INCDIR="-I. -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install sipp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt MEDIA.txt README.txt pcap tools
%attr(755,root,root) %{_bindir}/*
