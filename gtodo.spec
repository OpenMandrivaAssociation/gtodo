%define	name	gtodo
%define	version	0.16.0
%define	release	%mkrel 0.rc2.1
%define	Summary	TODO List manager for Gnome 2

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Office
URL:		http://gtodo.qballcow.nl/
Source0:	%{name}-%{version}-rc2.tar.bz2
Source11:	gtodo16.png
Source12:	gtodo32.png
Source13:	gtodo48.png
Patch0:		gtodo-0.16.0-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gettext libxml2-devel gtk+2-devel libGConf2-devel
BuildRequires:	perl-XML-Parser gnome-vfs2-devel libxslt-devel
BuildRequires:	desktop-file-utils

%description
Gtodo is a Gtk+-2.0 Todo list manager written for use with gnome 2.
It tries to follow the hig and gnome policy as good as possible.

%prep
%setup -q 
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name}

desktop-file-install	--vendor="" \
			--remove-category="Application" \
			--add-category="X-MandrivaLinux-Office-TasksManagement" \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas %{name}
%endif

%preun
%preun_uninstall_gconf_schemas %{name}

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/mime-info/*


