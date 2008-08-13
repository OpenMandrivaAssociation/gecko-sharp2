%define oname		gecko-sharp-2.0
%define name		gecko-sharp2
%define version		0.13
%define release		%mkrel 5
%define pkgconfigdir	%_datadir/pkgconfig

%define xulrunner 1.9
Summary:	C# language binding for the gtkembedmoz widget
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://go-mono.com/sources/gecko-sharp-2.0/%{oname}-%{version}.tar.bz2
#gw from Fedora, use xulrunner
Patch:		gecko-sharp-2.0-0.12-xulrunner.patch
URL:		http://www.go-mono.com
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

