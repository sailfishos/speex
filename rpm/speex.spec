Name:       speex
Summary:    A voice compression format (codec)
Version:    1.2.1
Release:    1
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
Requires:   %{name} = %{version}-%{release}

%description tools
Speex is a patent-free compression format designed especially for
speech. This package contains tools files and user's manual for %{name}.


%package devel
Summary:    Development package for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}



%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static --enable-binaries --enable-fixed-point
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -f $RPM_BUILD_ROOT%{_docdir}/speex/manual.pdf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libspeex.so.*

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
%{_includedir}/speex/speex.h
%{_includedir}/speex/speex_callbacks.h
%{_includedir}/speex/speex_types.h
%{_includedir}/speex/speex_stereo.h
%{_includedir}/speex/speex_bits.h
%{_includedir}/speex/speex_header.h
%{_includedir}/speex/speex_config_types.h
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex.pc
%{_libdir}/libspeex.so
