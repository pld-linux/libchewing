#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Intelligent phonetic input method library for Traditional Chinese
Summary(pl.UTF-8):	Biblioteka inteligentnej fonetycznej metody wprowadzania chińskiego tradycyjnego
Name:		libchewing
Version:	0.6.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/chewing/libchewing/releases
Source0:	https://github.com/chewing/libchewing/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	8ba443ebf263104c6b02e6dc6ab4135c
Patch0:		%{name}-info.patch
URL:		https://chewing.im/
BuildRequires:	cmake >= 3.21.0
# only for tests
#BuildRequires:	ncurses-devel >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libchewing is an intelligent phonetic input method library for
Chinese. It provides the core algorithm and logic that can be used by
various input methods. The Chewing input method is a smart bopomofo
phonetics input method that is useful for inputting Mandarin Chinese.

%description -l pl.UTF-8
libchewing to biblioteka inteligentnej fonetycznej metody wprowadzania
tekstu w języku chińskim tradycyjnym. Udostępnia główny algorytm i
logikę do używania w różnych metodach wprowadzania. Metoda Chewing to
inteligentna metoda wprowadzania fonetyki bopomofo przydatna do
wprowadzania chińskiego mandaryńskiego.

%package devel
Summary:	Header files for libchewing library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libchewing
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libchewing library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libchewing.

%package static
Summary:	Static libchewing library
Summary(pl.UTF-8):	Statyczna biblioteka libchewing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libchewing library.

%description static -l pl.UTF-8
Statyczna biblioteka libchewing.

%prep
%setup -q
%patch0 -p1

%build
%if %{with static_libs}
%cmake -B build-static \
	-DBUILD_SHARED_LIBS=OFF

%{__make} -C build-static
%endif

%cmake -B build \
	-DBUILD_INFO=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libchewing.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchewing.so.3
%{_datadir}/libchewing

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchewing.so
%{_includedir}/chewing
%{_pkgconfigdir}/chewing.pc
%{_infodir}/libchewing.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libchewing.a
%endif
