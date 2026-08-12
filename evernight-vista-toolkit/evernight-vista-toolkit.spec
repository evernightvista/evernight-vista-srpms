Name:           evernight-vista-toolkit
Version:        45.0.0
Release:        1%{?dist}
Summary:        Evernight Vista system utility toolkit

License:        GPL-3.0-or-later
URL:            https://evernight-vista.local/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kwidgetsaddons-devel

Requires:       dnf5
Requires:       polkit
Requires:       rpm
Obsoletes:      evernight-vista-tools

%description
Evernight Vista Toolkit is a Qt6 and KDE Frameworks 6 application for managing
optional Evernight Vista components and system-wide environment variables.

It provides polkit-protected helpers for Wine, Steam, MIDI playback support and
additional fonts.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/evernight-vista-toolkit
%{_datadir}/applications/evernight-vista-toolkit.desktop
%{_datadir}/applications/terminal-as-root.desktop
%{_datadir}/applications/file-manager-as-root.desktop
%{_datadir}/kio/servicemenus/open-root.desktop
%{_datadir}/metainfo/org.evernight.vista.toolkit.metainfo.xml
%{_datadir}/polkit-1/actions/org.evernight.vista.toolkit.policy
%dir %{_libexecdir}/evernight-vista-toolkit
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-wine
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-steam
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-midi
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-extra-fonts
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-remove-wine
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-remove-steam
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-remove-midi
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-remove-extra-fonts
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-apply-environment
%{_libexecdir}/evernight-vista-toolkit/evernight-vista-toolkit-restore-environment

%changelog
* Wed Aug 12 2026 Evernight Vista <13278297951@sina.cn> - 45.0.0-1
- Initial package with Qt6/KF6 UI, polkit helpers and environment variable editor.
