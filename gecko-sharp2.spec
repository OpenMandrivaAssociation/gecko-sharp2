%define oname    gecko-sharp-2.0
%define name    gecko-sharp2
%define version 0.12
%define release %mkrel 1
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif

Summary:       Gecko-sharp is a C# language binding for the gtkembedmoz widget
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source:        http://go-mono.com/sources/gecko-sharp-2.0/%oname-%version.tar.bz2
URL:           http://www.go-mono.com
License:       LGPL/MPL
Group:         System/Libraries
Provides:      gtkmozembed-sharp == %{version}
Requires:      gtk-sharp2
Requires:      libmozilla-firefox
BuildRequires: gtk2-devel
BuildRequires: gtk-sharp2
BuildRequires: mono-devel
BuildRequires: mono-tools
BuildArch: noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-buildroot
%define _requires_exceptions ^lib.*

%description 
Gecko-sharp is a C# language binding for the gtkembedmoz widget. You
can use it to embed mozilla into C# programs.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
Gecko-sharp is a C# language binding for the gtkembedmoz widget. You
can use it to embed mozilla into C# programs.

This package contains the API documentation for the %name in
Monodoc format.

%prep
%setup -q -n %oname-%version

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
make

%install
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
%doc ChangeLog COPYING README sample
%{_prefix}/lib/mono/gac/*
%{_prefix}/lib/mono/gecko-sharp-2.0
%{pkgconfigdir}/*

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/gecko-sharp-docs*


