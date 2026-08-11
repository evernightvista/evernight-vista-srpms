Name:           nvidia-driver-manager
Version:        45.0.0
Release:        1%{?dist}
Summary:        NVIDIA driver manager for Fedora

License:        GPL-3.0-or-later
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires:       pciutils
Requires:       rpm
Requires:       mokutil
Requires:       polkit
Requires:       dnf

%description
NVIDIA Driver Manager is a Qt/KF6 graphical utility for Fedora.
It detects NVIDIA GPUs, lets users select NVIDIA driver branches,
supports Secure Boot MOK enrollment, and installs the matching CUDA
driver package.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%{_bindir}/%{name}
%{_libexecdir}/nvidia-driver-manager-helper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/org.fedoraproject.nvidia-driver-manager.policy

%changelog
* Tue Aug 11 2026 KairikiFedora <13278297951@sina.cn> - 45.0.0-1
- Rewritten NVIDIA driver manager with GPU detection, driver branch selection,
  Secure Boot MOK support, --skip detection override, and CUDA package handling.
- Install akmods-evernight automatically at runtime when needed, use one Polkit
  authentication for the whole install flow, and add zh_CN/zh_TW/ja/de/ko/fr
  translations.
