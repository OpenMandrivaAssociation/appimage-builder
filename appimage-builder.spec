Name:           appimage-builder
Version:        0.8.1
Release:        1
Summary:        Recipe based AppImage creation tool
Group:          System/Configuration/Packaging
License:        MIT
URL:            https://github.com/AppImageCrafters/appimage-builder
Source0:        https://github.com/AppImageCrafters/appimage-builder/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Requires:       python
Requires:       python3dist(setuptools)

%description
It's a tool for packing applications along with all of its dependencies using the system package manager to obtain binaries and resolve dependencies. 
It creates a self-sufficient and portable bundle using the AppImage format.

Features:

Real GNU/Linux packaging (no more distro packaging)
Simple recipes
Simple workflow
Backward and forward compatibility
One binary, many target systems.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
#python setup.py build
%py_build

%install
#python setup.py install --root=%{buildroot}
%py_install
%files
