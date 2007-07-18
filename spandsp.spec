%define major 0
%define libname %mklibname spandsp %{major}
%define libnamedev %mklibname spandsp -d

Summary:        Steve's SpanDSP library for telephony spans
Name:           spandsp
Version:        0.0.4
Release:        %mkrel 0.pre3.1
License:        GPL
Group:          System/Libraries
URL:            http://www.soft-switch.org/
Source0:        http://www.soft-switch.org/downloads/spandsp/spandsp-0.0.4pre3.tgz
BuildRequires:  autoconf2.5
BuildRequires:  automake1.7
BuildRequires:  audiofile-devel
BuildRequires:  fftw2-devel
BuildRequires:  file
BuildRequires:  fltk-devel
BuildRequires:  jpeg-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  tiff-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
Obsoletes:      %{name}-devel < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{libnamedev}
This package includes the header files and libraries needed for
developing programs using SpanDSP.

%prep
%setup -q
# strip away annoying ^M
#find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
#find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}

%check
# make test does not work yet
%if 0
%{make} -C tests \
    LIBS="-laudiofile -lfftw -lxml2 -ltiff -lfl -lpthread"
%endif

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
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/%{name}/global-tones.xml
%{_datadir}/%{name}/tones.dtd
