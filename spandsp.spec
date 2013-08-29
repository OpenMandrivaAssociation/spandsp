%define major 2

%define libnamedevold %{mklibname spandsp 0}-devel
%define libname %mklibname spandsp %{major}
%define libnamedev %mklibname spandsp -d
%define libnamestaticdev %mklibname spandsp -d -s

Summary:        Steve's SpanDSP library for telephony spans
Name:           spandsp
Version:        0.0.6
Release:        %mkrel 0.pre21
License:        GPL
Group:          System/Libraries
URL:            http://www.soft-switch.org/
Source0:        http://www.soft-switch.org/downloads/spandsp/spandsp-%{version}pre21.tgz
BuildRequires:  audiofile-devel
BuildRequires:  fftw3-devel
BuildRequires:  file
BuildRequires:  fltk-devel
BuildRequires:  jpeg-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  tiff-devel

%description
spandsp is a library for DSP in telephony spans. It can perform many of the
common DSP functions, such as the generation and detection of DTMF and
supervisory tones.

%package -n %{libname}
Summary:        Steve's SpanDSP library for telephony spans
Group:          System/Libraries

%description -n %{libname}
spandsp is a library for DSP in telephony spans. It can perform many of the
common DSP functions, such as the generation and detection of DTMF and
supervisory tones.

%package -n %{libnamedev}
Summary:        Header files and libraries needed for development with SpanDSP
Group:          Development/C
Obsoletes:      %{libnamedevold} < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libnamedev}
This package includes the header files and libraries needed for developing
programs using SpanDSP.

%package -n %{libnamestaticdev}
Summary:        Static libraries needed for development with SpanDSP
Group:          Development/C
Provides:       %{name}-static-devel = %{version}-%{release}
Requires:       %{libnamedev} = %{version}-%{release}

%description -n %{libnamestaticdev}
This package includes the static libraries needed for developing programs
using SpanDSP.

%prep

%setup -q

%build
%configure2_5x --enable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING DueDiligence INSTALL NEWS README
%{_libdir}/lib*.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/spandsp
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{libnamestaticdev}
%{_libdir}/*.a


%changelog
* Thu Nov 03 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.0.6-0.pre18mdv2011.0
+ Revision: 713253
- added new files removed old
- pkgconfig fix in spec and version bump

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.0.5-0.pre4.2mdv2010.0
+ Revision: 434015
- rebuild

* Tue Jul 22 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-0.pre4.1mdv2009.0
+ Revision: 240865
- 0.0.5pre4

* Wed Jun 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.4-0.pre7.3mdv2009.0
+ Revision: 225610
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.0.4-0.pre7.2mdv2008.1
+ Revision: 140850
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 David Walluck <walluck@mandriva.org> 0.0.4-0.pre7.2mdv2008.0
+ Revision: 79130
- 0.0.4pre7

* Sat Jul 21 2007 Stefan van der Eijk <stefan@mandriva.org> 0.0.4-0.pre3.2mdv2008.0
+ Revision: 54337
- fix new dev stuff breakage

* Wed Jul 18 2007 David Walluck <walluck@mandriva.org> 0.0.4-0.pre3.1mdv2008.0
+ Revision: 53318
- 0.0.4pre3

