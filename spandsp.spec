%define major 3

%define libnamedevold %{mklibname spandsp 0}-devel
%define oldlibname %mklibname spandsp 2
%define libname %mklibname spandsp
%define libnamedev %mklibname spandsp -d
%define libnamestaticdev %mklibname spandsp -d -s

%define date 20230428

Summary:        Steve's SpanDSP library for telephony spans
Name:           spandsp
Version:        3.0.0
Release:        0.%{date}1
License:        GPL
Group:          System/Libraries
URL:            https://github.com/freeswitch/spandsp
Source0:        https://github.com/freeswitch/spandsp/archive/refs/heads/master.tar.gz#/%{name}-%{date}.tar.gz
BuildRequires:  pkgconfig(audiofile)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  file
BuildRequires:  fltk-devel
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  libtool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libtiff-4)

%description
spandsp is a library for DSP in telephony spans. It can perform many of the
common DSP functions, such as the generation and detection of DTMF and
supervisory tones.

%package -n %{libname}
Summary:        Steve's SpanDSP library for telephony spans
Group:          System/Libraries
%rename %{oldlibname}

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
%autosetup -p1 -n %{name}-master
./autogen.sh
%configure --enable-static

%build
%make_build

%install
%make_install

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
