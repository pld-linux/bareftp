#
# Conditional build
%bcond_without	gnome_keyring	# without gnome-keyring
#
Summary:	File transfer client supporting the FTP, FTP (FTPS) and SSH (SFTP)
Summary(pl.UTF-8):	Program do transferu plkików używający FTP, FTP (FTPS) oraz SSH (SFTP)
Name:		bareftp
Version:	0.3.5
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.bareftp.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	a6e123e27c668f51d22fbc525856a89b
URL:		http://www.bareftp.org/
%{?with_gnome_keyring:BuildRequires:	dotnet-gnome-keyring-sharp-devel}
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bareFTP is a file transfer client writen in C# supporting the FTP, FTP
over SSL/TLS (FTPS) and SSH File Transfer Protocol (SFTP).

%description -l pl.UTF-8
bareFTP jest programem do transferu plików napisanym w C# wspierającym
protokoły FTP, FTP z obsługą SSL/TLS (FTPS) oraz SSH (SFTP).

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
