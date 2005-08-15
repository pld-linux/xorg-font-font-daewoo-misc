# $Rev: 3206 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-daewoo-misc
Summary(pl):	font-daewoo-misc
Name:		xorg-font-font-daewoo-misc
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-daewoo-misc-%{version}.tar.bz2
# Source0-md5:	5980c9f827a3484044c18d1f526d1bd4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-daewoo-misc-%{version}-root-%(id -u -n)

%description
font-daewoo-misc

%description -l pl
font-daewoo-misc


%prep
%setup -q -n font-daewoo-misc-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/misc/*
