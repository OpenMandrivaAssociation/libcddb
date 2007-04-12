%define name libcddb
%define version 1.3.0
%define rel 1
%define release %mkrel %rel
%define docver 1.3.0

%define major 2
%define libname %mklibname cddb %{major}

Name: %name
Version: %version
Release: %release
License: LGPL
Group: System/Libraries
URL: http://libcddb.sourceforge.net/
Source: http://prdownloads.sourceforge.net/libcddb/%name-%version.tar.bz2
Source1: http://prdownloads.sourceforge.net/libcddb/%name-doc-%docver.tar.bz2
BuildRoot: %_tmppath/%name-buildroot
Summary: CDDB access library
BuildRequires: libcdio-devel
#auto* deps
BuildRequires: gettext-devel
BuildRequires: automake1.8

%description 
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.


%package -n %{libname}
Summary: Libraries from %name
Group: System/Libraries

%description -n %{libname}
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

%package -n %{libname}-devel
Summary: Devel files from libcddb
Group: Development/C
Requires: %{libname} = %version
Provides: %name-devel = %version-%release 

%description -n %{libname}-devel
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

This is the libraries, include files and other resources you can use
to incorporate libcddb into applications.

%package -n %libname-static-devel 
Summary: Static Library for developing applications with %name
Group: Development/C
Requires: %libname-devel = %version

%description -n %libname-static-devel
This contains the static library of %name needed for building apps that
link statically to %name.

%package apps
Summary: Example applications based on %name
Group: Sound

%description apps
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

This package contains a command line client based on %name.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -a 1
mv output html
#gw fix libtool problem
aclocal-1.8
autoconf

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files apps
%defattr (- ,root,root)
%_bindir/*

%files -n %{libname}
%defattr (- ,root,root)
%_libdir/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc ChangeLog README AUTHORS NEWS TODO html
%_includedir/cddb
%_libdir/*.so
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/*.pc

%files -n %libname-static-devel
%defattr(-,root,root)
%{_libdir}/lib*.a

%clean
rm -rf ${RPM_BUILD_ROOT}


