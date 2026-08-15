Name:           btrfs-assistant-evernight
Version:        2.2
Release:        1%{?dist}
Summary:        GUI management tool for Btrfs and Snapper

License:        GPL-3.0-or-later
URL:            https://gitlab.com/btrfs-assistant/btrfs-assistant
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist
BuildRequires:  btrfs-progs-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3

Requires:       snapper
Requires:       btrfs-progs
Requires:       polkit
Requires:       qt6-qtbase-gui
Requires:       libdnf5-plugin-actions

Recommends:     btrfsmaintenance

Conflicts:      btrfs-assistant
Provides:       btrfs-assistant = %{version}-%{release}

%description
Btrfs Assistant is a GUI management tool to make managing a Btrfs filesystem
easier. It provides an overview of Btrfs metadata, subvolume management,
scrub and balance operations, Snapper snapshot management, and Btrfs
Maintenance configuration.

This package (btrfs-assistant-evernight) is a repackaged version that conflicts
with the original btrfs-assistant package but provides the same functionality.
It includes additional translations (Japanese, Korean, French, German,
Traditional Chinese) and a dnf5 snapper actions plugin for automatic
pre/post transaction snapshots.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

# Install snapper actions for dnf5 pre/post transaction snapshots
install -D -m 644 src/snapper.actions \
    %{buildroot}%{_sysconfdir}/dnf/libdnf5-plugins/actions.d/snapper.actions

%files
%license LICENSE
%doc README.md changelog
%{_bindir}/btrfs-assistant
%{_bindir}/btrfs-assistant-launcher
%{_bindir}/btrfs-assistant-bin
%dir %{_datadir}/btrfs-assistant
%dir %{_datadir}/btrfs-assistant/translations
%{_datadir}/btrfs-assistant/translations/*.qm
%{_datadir}/applications/btrfs-assistant.desktop
%{_datadir}/metainfo/btrfs-assistant.metainfo.xml
%{_datadir}/polkit-1/actions/org.btrfs-assistant.pkexec.policy
%{_datadir}/icons/hicolor/scalable/apps/btrfs-assistant.svg
%config(noreplace) %{_sysconfdir}/btrfs-assistant.conf
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/actions.d/snapper.actions

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%changelog
* Sat Aug 15 2026 Evernight Vista Team <13278297951@sina.cn> - 2.2-1
- Repackaged as btrfs-assistant-evernight
- Added translations: Japanese, Korean, French, German, Traditional Chinese
- Added snapper.actions for dnf5 pre/post transaction snapshots
- Conflicts with btrfs-assistant, provides btrfs-assistant
- Requires snapper as runtime dependency
