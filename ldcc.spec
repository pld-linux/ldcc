Summary:	Text UI for DCTC
Summary(pl):	Textowe UI dla DCTC
Name:		ldcc
Version:	2.0.7
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.softservice.com.pl/store/ldcc/%{name}-%{version}.tgz
# Source0-md5:  1fbaa46a139880c6a91faf3dc5e678ff
URL:		http://www.softservice.com.pl/ldcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	librhtv-devel >= 2.0.1
Requires:	dctc
Requires:	librhtv >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDCC is a linux console, text-based client for direct connect

%description -l pl
LDCC jest konsolowym klientem sieci direct connect

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-tv-include=%{_includedir}/rhtvision

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}/
install src/ldcc $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
