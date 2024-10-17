%define oname		gecko-sharp-2.0
%define name		gecko-sharp2
%define version		0.13
%define release		%mkrel 7
%define pkgconfigdir	%_datadir/pkgconfig

%define xulrunner 1.9
Summary:	C# language binding for the gtkembedmoz widget
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://go-mono.com/sources/gecko-sharp-2.0/%{oname}-%{version}.tar.bz2
#gw from Fedora, use xulrunner
Patch:		gecko-sharp-2.0-0.12-xulrunner.patch
URL:		https://www.go-mono.com
License:	LGPLv2+ and MPLv1.1
Group:		System/Libraries
Provides:	gtkmozembed-sharp == %{version}
Requires:	gtk-sharp2
Requires:	libxulrunner >= %xulrunner
BuildRequires:	xulrunner-devel >= %xulrunner
BuildRequires:	gtk2-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	mono-devel
BuildRequires:	mono-tools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
%define _requires_exceptions ^lib\\|lib.*glib2.0_0

%description 
Gecko-sharp is a C# language binding for the gtkembedmoz widget. You
can use it to embed mozilla into C# programs.

%package doc
Summary:	Development documentation for %name
Group:		Development/Other
Requires(post):		mono-tools >= 1.1.9
Requires(postun):	mono-tools >= 1.1.9

%description doc
Gecko-sharp is a C# language binding for the gtkembedmoz widget. You
can use it to embed mozilla into C# programs.

This package contains the API documentation for %name in
Monodoc format.

%prep
%setup -q -n %oname-%version
%patch -p1

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%pkgconfigdir

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc ChangeLog README sample
%{_prefix}/lib/mono/gac/*
%{_prefix}/lib/mono/gecko-sharp-2.0
%{pkgconfigdir}/*

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/gecko-sharp-docs*



%changelog
* Wed Oct 12 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-7mdv2012.0
+ Revision: 704467
- rebuild

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 0.13-6mdv2011.0
+ Revision: 584903
- rebuild

* Wed Aug 13 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-5mdv2011.0
+ Revision: 271468
- fix xulrunner dep

* Wed Jul 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-4mdv2009.0
+ Revision: 255984
- fix xulrunner dep

* Wed Jul 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-3mdv2009.0
+ Revision: 254950
- build with xulrunner

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-2mdv2009.0
+ Revision: 193993
- fix requires exception

* Tue Apr 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.13-1mdv2009.0
+ Revision: 192402
- new version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.12-5mdv2008.1
+ Revision: 170857
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-3mdv2008.0
+ Revision: 94389
- fix pkgconfig dir

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.12-2mdv2008.0
+ Revision: 91236
- correct buildrequires
- rebuild for 2008
- new license policy
- spec clean

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - filter out new automatic mono deps


* Wed Feb 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-1mdv2007.0
+ Revision: 117018
- new version
- disable parallel build

* Sat Nov 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.11-5mdv2007.1
+ Revision: 76571
- Import gecko-sharp2

* Fri Sep 22 2006 Götz Waschk <waschk@mandriva.org> 0.11-5mdv2007.0
- split monodoc docs to separate package

* Thu Aug 31 2006 Götz Waschk <waschk@mandriva.org> 0.11-4mdv2007.0
- fix deps

* Wed Jul 19 2006 Götz Waschk <waschk@mandriva.org> 0.11-3mdv2007.0
- fix postun script

* Thu Sep 29 2005 Götz Waschk <waschk@mandriva.org> 0.11-2mdk
- regenerate monodoc index on postun

* Sun Sep 11 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.11-1mdk
- New release 0.11

* Fri Aug 26 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.10-4mdk
- rebuild for new gtk-sharp2

* Sat Jul 02 2005 Götz Waschk <waschk@mandriva.org> 0.10-3mdk
- fix deps

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 0.10-2mdk
- add monodoc calls in the post scripts

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 0.10-1mdk
- fix buildrequires
- update file list
- drop the patch
- new source URL
- New release 0.10

* Fri Apr 29 2005 Götz Waschk <waschk@mandriva.org> 0.7-4mdk
- fix pkgconfig location

* Fri Apr 01 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-3mdk
- fix buildrequires

* Thu Mar 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-2mdk
- fix buildrequires

* Thu Mar 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- rename from gecko-sharp to coexist with version for gtk-sharp 1.0.x
- New release 0.7

* Thu Mar 24 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-5mdk 
- Rebuild with firefox 1.0.2

* Sat Feb 26 2005 Götz Waschk <waschk@linux-mandrake.com> 0.6-4mdk
- depend on firefox instead of mozilla

* Wed Jan 05 2005 Götz Waschk <waschk@linux-mandrake.com> 0.6-3mdk
- rebuild

* Sun Nov 21 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6-2mdk
- rebuild for new mozilla

* Sun Oct 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6-1mdk
- noarch package
- New release 0.6

* Thu Jul 29 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-2mdk
- rebuild for new rpm

* Thu Jun 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- update file list
- fix autoconf macro
- fix description
- enable parallel build
- new version

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 0.4-2mdk
- buildrequires (slbd)

* Fri Jun 04 2004 Sandino "Tigrux" Flores <tigrux@ximian.com> 0.4-1mdk
- First rpm for mandrake

