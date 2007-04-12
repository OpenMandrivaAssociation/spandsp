%define	major 0
%define libname	%mklibname spandsp %{major}

Summary:	Steve's SpanDSP library for telephony spans
Name:		spandsp
Version:	0.0.3
Release:	%mkrel 1.pre27.1
License:	GPL
Group:		System/Libraries
URL:		http://www.soft-switch.org/
Source0:	http://www.soft-switch.org/downloads/spandsp/spandsp-0.0.3pre27.tgz
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	tiff-devel >= 3.6.1-3mdk
BuildRequires:	fltk-devel
BuildRequires:	fftw2-devel
BuildRequires:	audiofile-devel
BuildRequires:	libxml2-devel
BuildRequires:	jpeg-devel
BuildRequires:	file
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
spandsp is a library for DSP in telephony spans. It can perform
many of the common DSP functions, such as the generation and
detection of DTMF and supervisory tones.

%package -n	%{libname}
Summary:	Steve's SpanDSP library for telephony spans
Group:          System/Libraries

%description -n	%{libname}
spandsp is a library for DSP in telephony spans. It can perform
many of the common DSP functions, such as the generation and
detection of DTMF and supervisory tones.

%package -n	%{libname}-devel
Summary:	Header files and libraries needed for development with SpanDSP
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Obsoletes:	%{name}-devel lib%{name}-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
This package includes the header files and libraries needed for
developing programs using SpanDSP.

%prep

%setup -q -n %{name}-0.0.3

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
#export WANT_AUTOCONF_2_5=1
#libtoolize --copy --force && aclocal-1.7 && autoconf && automake-1.7

%configure2_5x

%make

# make test does not work yet
#%%make -C tests \
#    LIBS="-laudiofile -lfftw -lxml2 -ltiff -lfl -lpthread"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS ChangeLog DueDiligence NEWS README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_includedir}/spandsp
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/%{name}/global-tones.xml
%{_datadir}/%{name}/tones.dtd


