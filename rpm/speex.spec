Name:       speex
Summary:    A voice compression format (codec)
Version:    1.2.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.speex.org/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)


%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).



%package tools
Summary:    The tools package for %{name}
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}

%description tools
Speex is a patent-free compression format designed especially for
speech. This package contains tools files and user's manual for %{name}.


%package devel
Summary:    Development package for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}



%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static --enable-binaries
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -f $RPM_BUILD_ROOT%{_docdir}/speex/manual.pdf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libspeex*.so.*

%files tools
%defattr(-,root,root,-)
%{_bindir}/speexenc
%{_bindir}/speexdec
%doc %{_mandir}/man1/speexenc.1*
%doc %{_mandir}/man1/speexdec.1*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS TODO
%doc doc/manual.pdf
%dir %{_includedir}/speex
%{_includedir}/speex/*.h
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex*.pc
%{_libdir}/libspeex*.so
