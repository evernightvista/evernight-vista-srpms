Name:           evernight-vista-grub-config
Version:        45.0.0
Release:        1%{?dist}
Summary:        KDE Plasma 6 GRUB2 configuration tool for Evernight Vista

License:        GPL-3.0-or-later
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       polkit
Requires:       grub2-tools
Requires:       grubby

%description
Evernight Vista GRUB Config is a KDE Plasma 6 friendly Qt/KF6 utility for
configuring GRUB2 boot menu behavior and custom kernel parameters.

The graphical interface follows the active KDE Plasma 6 application appearance
style. Saving GRUB2 settings is performed through a dedicated polkit-protected
helper, then the bootloader configuration is regenerated with grub2-mkconfig.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.evernight.vista.grubconfig.desktop


%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}-helper
%{_datadir}/applications/org.evernight.vista.grubconfig.desktop
%{_datadir}/polkit-1/actions/org.evernight.vista.grubconfig.policy


%changelog
* Wed Aug 12 2026 Evernight Vista <13278297951@sina.cn> - 45.0.0-1
- Initial RPM package.
