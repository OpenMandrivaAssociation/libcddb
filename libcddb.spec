%define docver	1.3.0
%define major	2
%define libname	%mklibname cddb %{major}
%define devname	%mklibname cddb -d
%define _disable_rebuild_configure 1
%define _disable_lto 1

%bcond_with	bootstrap

Summary:	CDDB access library
Name:		libcddb
Version:	1.3.2
Release:	20
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libcddb.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libcddb/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/libcddb/%{name}-doc-%{docver}.tar.bz2
%if !%{with bootstrap}
BuildRequires:	pkgconfig(libcdio)
%endif

%description 
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

%package apps
Summary:	Example applications based on %{name}
Group:		Sound

%description apps
This package contains a command line client based on %{name}.

%package -n %{libname}
Summary:	Libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

%package -n %{devname}
Summary:	Devel files from libcddb
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}cddb2-devel < 1.3.2-5
Obsoletes:	%{_lib}cddb-static-devel < 1.3.2-8

%description -n %{devname}
This is the libraries, include files and other resources you can use
to incorporate libcddb into applications.

%prep
%setup -q -a 1
mv output html

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files apps
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libcddb.so.%{major}*

%files -n %{devname}
%doc ChangeLog README AUTHORS NEWS TODO html
%{_includedir}/cddb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

