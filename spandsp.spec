%define major 0

%define libnamedevold %{mklibname spandsp 0}-devel
%define libname %mklibname spandsp %{major}
%define libnamedev %mklibname spandsp -d
%define libnamestaticdev %mklibname spandsp -d -s

Name:           spandsp
Version:        0.0.4
Release:        %mkrel 0.pre7.2
Summary:        Steve's SpanDSP library for telephony spans
License:        GPL
Group:          System/Libraries
URL:            http://www.soft-switch.org/
Source0:        http://www.soft-switch.org/downloads/spandsp/spandsp-0.0.4pre7.tgz
BuildRequires:  audiofile-devel
BuildRequires:  fftw2-devel
BuildRequires:  file
BuildRequires:  fltk-devel
BuildRequires:  jpeg-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  tiff-devel

%description
spandsp is a library for DSP in telephony spans. It can perform
many of the common DSP functions, such as the generation and
detection of DTMF and supervisory tones.

%package -n %{libname}
Summary:        Steve's SpanDSP library for telephony spans
Group:          System/Libraries

%description -n %{libname}
spandsp is a library for DSP in telephony spans. It can perform
many of the common DSP functions, such as the generation and
detection of DTMF and supervisory tones.

%package -n %{libnamedev}
Summary:        Header files and libraries needed for development with SpanDSP
Group:          Development/C
Obsoletes:      %{libnamedevold} < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libnamedev}
This package includes the header files and libraries needed for
developing programs using SpanDSP.

%package -n %{libnamestaticdev}
Summary:        Static libraries needed for development with SpanDSP
Group:          Development/C
Provides:       %{name}-static-devel = %{version}-%{release}
Requires:       %{libnamedev} = %{version}-%{release}

%description -n %{libnamestaticdev}
This package includes the static libraries needed for
developing programs using SpanDSP.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING DueDiligence INSTALL NEWS README
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/spandsp
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_datadir}/%{name}/global-tones.xml
%{_datadir}/%{name}/tones.dtd

%files -n %{libnamestaticdev}
%defattr(-,root,root)
%{_libdir}/*.a
