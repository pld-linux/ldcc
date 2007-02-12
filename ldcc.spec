Summary:	Text UI for DCTC
Summary(pl.UTF-8):   Tekstowy interfejs użytkownika dla DCTC
Name:		ldcc
%define		subver	beta
Version:	2.1.0
Release:	0.%{subver}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.softservice.com.pl/store/ldcc/%{name}-%{version}-%{subver}.tgz
# Source0-md5:	2942aa7a107c94d85bd356bc1d554446
Patch0:		%{name}-signal.patch
URL:		http://www.softservice.com.pl/ldcc/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	librhtv-devel >= 2.0.1
Requires:	dctc >= 0.85.9
Requires:	librhtv >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDCC is a Linux console, text-based client for Direct Connect.

%description -l pl.UTF-8
LDCC jest konsolowym klientem sieci Direct Connect.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p1

%build
%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__automake}
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
