Summary:	Text UI for DCTC
Summary(pl):	Tekstowy interfejs u¿ytkownika dla DCTC
Name:		ldcc
Version:	2.0.7
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://www.softservice.com.pl/store/ldcc/%{name}-%{version}.tgz
# Source0-md5:  1fbaa46a139880c6a91faf3dc5e678ff
Patch0:		%{name}-signal.patch
URL:		http://www.softservice.com.pl/ldcc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	librhtv-devel >= 2.0.1
Requires:	dctc
Requires:	librhtv >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDCC is a Linux console, text-based client for Direct Connect.

%description -l pl
LDCC jest konsolowym klientem sieci Direct Connect.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-tv-include=%{_includedir}/rhtvision \
	--with-tv-lib=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/ldcc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
