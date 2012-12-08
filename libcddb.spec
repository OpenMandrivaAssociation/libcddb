%define docver 1.3.0

%define major 2
%define libname %mklibname cddb %{major}
%define develname %mklibname cddb -d
%define staticdevelname %mklibname cddb -d -s

%define bootstrap 0
%{?_with_bootstrap: %global bootstrap 1}

Summary:	CDDB access library
Name:		libcddb
Version:	1.3.2
Release:	7
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libcddb.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libcddb/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/libcddb/%{name}-doc-%{docver}.tar.bz2
%if !%{bootstrap}
BuildRequires:	pkgconfig(libcdio)
%endif
#auto* deps
#BuildRequires:	gettext-devel
#BuildRequires:	automake1.8

%description 
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

%package -n %{libname}
Summary:	Libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

%package -n %{develname}
Summary:	Devel files from libcddb
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}cddb2-devel < 1.3.2-5

%description -n %{develname}
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

This is the libraries, include files and other resources you can use
to incorporate libcddb into applications.

%package -n %{staticdevelname}
Summary:	Static Library for developing applications with %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}cddb2-static-devel < 1.3.2-5

%description -n %{staticdevelname}
This contains the static library of %{name} needed for building apps that
link statically to %{name}.

%package apps
Summary:	Example applications based on %{name}
Group:		Sound

%description apps
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org).  It
tries to be as cross-platform as possible.  The initial libary will
have a C API.

This package contains a command line client based on %{name}.

%prep
%setup -q -a 1
mv output html

%build
%configure2_5x
%make

%install
%makeinstall_std

%files apps
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog README AUTHORS NEWS TODO html
%{_includedir}/cddb
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{staticdevelname}
%{_libdir}/lib*.a

%changelog
* Thu Oct 27 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.2-5mdv2012.0
+ Revision: 707546
- rebuild for new libcdio

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-4
+ Revision: 660227
- mass rebuild

* Sun Sep 27 2009 Olivier Blin <blino@mandriva.org> 1.3.2-3mdv2010.0
+ Revision: 449858
- add boostrap flag for build dep loop libcddb <-> libcdio
  (from Arnaud Patard)

* Wed Aug 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.3.2-2mdv2010.0
+ Revision: 421575
- apply libraries policy

* Sun May 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 371267
- new version

* Sun Mar 01 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.1-1mdv2009.1
+ Revision: 346284
- new version
- update license
- fix build

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1.3.0-1mdv2009.0
+ Revision: 217188
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Sep 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.2-1mdv2007.0
- New version 1.2.2

* Fri Mar 24 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.1-4mdk
- rebuild for new libcdio

* Wed Jan 11 2006 Götz Waschk <waschk@mandriva.org> 1.2.1-3mdk
- fix buildrequires

* Thu Jan 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.1-2mdk
- Rebuild

* Sat Aug 06 2005 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdk
- doc version is still 1.2.0
- New release 1.2.1

* Tue Jul 26 2005 Götz Waschk <waschk@mandriva.org> 1.2.0-1mdk
- New release 1.2.0

* Fri Jul 22 2005 Götz Waschk <waschk@mandriva.org> 1.1.0-3mdk
- update the docs

* Thu Jul 14 2005 Götz Waschk <waschk@mandriva.org> 1.1.0-2mdk
- rebuild

* Mon Jul 11 2005 Götz Waschk <waschk@mandriva.org> 1.1.0-1mdk
- major 2
- New release 1.1.0

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 1.0.2-1mdk
- New release 1.0.2

* Sun Apr 24 2005 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdk
- fix deps
- mkrel
- New release 1.0.1

* Tue Apr 19 2005 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdk
- fix buildrequires

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0.0-1mdk
- fix build
- New release 1.0.0

* Fri Feb 04 2005 Götz Waschk <waschk@linux-mandrake.com> 0.9.6-2mdk
- rebuild

* Tue Nov 09 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.9.6-1mdk
- New release 0.9.6

* Fri Jul 23 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.5-1mdk
- add docs
- add source URL
- New release 0.9.5

