#
# TODO: - fix build without gnome-keyring
#	- errors when running with gnome-keyring 
#
# Conditional build
%bcond_without	gnome_keyring	# without gnome-keyring
#
Summary:	-
Summary(pl.UTF-8):	-
Name:		bareftp
Version:	0.3.3
Release:	0.1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.bareftp.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	3ef22582b0167c7ef8150d31822d406e
URL:		http://www.bareftp.org/
%{?with_gnome_keyring:BuildRequires:	dotnet-gnome-keyring-sharp-devel}
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q

%build
%configure \
	%{!?with_gnome_keyring:--without-gnomekeyring}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/bareftp
%dir %{_libdir}/bareftp
%{_libdir}/bareftp/bareFTP*.dll
%{_libdir}/bareftp/bareftp.exe
%{_mandir}/man1/bareftp.1*
%{_iconsdir}/hicolor/*/apps/*
%{_desktopdir}/bareftp.desktop
