Summary:	Net-SNMP extension for monitoring ISC DHCP server.
Name:		dhcpd-snmp
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.net-track.ch/opensource/dhcpd-snmp/%{name}-%{version}.tar.gz
# Source0-md5:	f2ea2aa9cbae4c3585d972bdecae9201
URL:		http://www.net-track.ch/opensource/dhcpd-snmp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.228
Requires:	net-snmp
Requires:	perl(Time::Local)
Requires:	dhcpd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dhcpd-snmp is an extension for the Net-SNMP agent and the ISC DHCP
server. It allows you to monitor and track the address usage of your
dynamic IP address pools through SNMP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
