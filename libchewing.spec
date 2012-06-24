Summary:	Intelligent phonetic input method library for Traditional Chinese
Summary(pl):	Biblioteka inteligentnej fonetycznej metody wprowadzania chi�skiego tradycyjnego
Name:		libchewing
Version:	0.2.7
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://chewing.csie.net/download/libchewing/%{name}-%{version}.tar.gz
# Source0-md5:	ca4a4834daf9247582de9813250e8466
URL:		http://chewing.csie.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libchewing is an intelligent phonetic input method library for
Chinese. It provides the core algorithm and logic that can be used by
various input methods. The Chewing input method is a smart bopomofo
phonetics input method that is useful for inputting Mandarin Chinese.

%description -l pl
libchewing to biblioteka inteligentnej fonetycznej metody wprowadzania
tekstu w j�zyku chi�skim tradycyjnym. Udost�pnia g��wny algorytm i
logik� do u�ywania w r�nych metodach wprowadzania. Metoda Chewing to
inteligentna metoda wprowadzania fonetyki bopomofo przydatna do
wprowadzania chi�skiego mandary�skiego.

%package devel
Summary:	Header files for libchewing library
Summary(pl):	Pliki nag��wkowe biblioteki libchewing
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libchewing library.

%description devel -l pl
Pliki nag��wkowe biblioteki libchewing.

%package static
Summary:	Static libchewing library
Summary(pl):	Statyczna biblioteka libchewing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libchewing library.

%description static -l pl
Statyczna biblioteka libchewing.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libchewing.so.*.*.*
%{_datadir}/chewing

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchewing.so
%{_libdir}/libchewing.la
%{_includedir}/chewing
%{_pkgconfigdir}/chewing.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libchewing.a
