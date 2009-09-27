%define name libcddb
%define version 1.3.2
%define rel 3
%define release %mkrel %rel
%define docver 1.3.0

%define major 2
%define libname %mklibname cddb %{major}
%define develname %mklibname cddb -d
%define staticdevelname %mklibname cddb -d -s

%define bootstrap 0
%{?_with_bootstrap: %global bootstrap 1}

Name: %name
Version: %version
Release: %release
License: LGPLv2+
Group: System/Libraries
URL: http://libcddb.sourceforge.net/
Source: http://prdownloads.sourceforge.net/libcddb/%name-%version.tar.bz2
Source1: http://prdownloads.sourceforge.net/libcddb/%name-doc-%docver.tar.bz2
BuildRoot: %_tmppath/%name-buildroot
Summary: CDDB access library
%if !%{bootstrap}
BuildRequires: libcdio-devel
%endif
#auto* deps
#BuildRequires: gettext-devel
#BuildRequires: automake1.8

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

%package -n %{develname}
Summary: Devel files from libcddb
Group: Development/C
Requires: %{libname} = %version
Provides: %{name}-devel = %version-%release
Obsoletes: %{_lib}cddb2-devel

%description -n %{develname}
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

This is the libraries, include files and other resources you can use
to incorporate libcddb into applications.

%package -n %{staticdevelname}
Summary: Static Library for developing applications with %name
Group: Development/C
Requires: %{develname} = %version
Provides: %{name}-static-devel = %version-%release
Obsoletes: %{_lib}cddb2-static-devel

%description -n %{staticdevelname}
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
rm -rf %{buildroot}
%setup -q -a 1
mv output html

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files apps
%defattr (- ,root,root)
%_bindir/*

%files -n %{libname}
%defattr (- ,root,root)
%_libdir/*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc ChangeLog README AUTHORS NEWS TODO html
%_includedir/cddb
%_libdir/*.so
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/*.pc

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/lib*.a



