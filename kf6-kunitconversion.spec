%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6UnitConversion
%define devname %mklibname KF6UnitConversion -d
#define git 20240217

Name: kf6-kunitconversion
Version: 6.20.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kunitconversion/-/archive/master/kunitconversion-master.tar.bz2#/kunitconversion-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kunitconversion-%{version}.tar.xz
%endif
Summary: Library for converting physical units
URL: https://invent.kde.org/frameworks/kunitconversion
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: python%{pyver}dist(build)
BuildRequires: pkgconfig(python3)
BuildRequires: cmake(Shiboken6)
BuildRequires: cmake(PySide6)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6I18n)
Requires: %{libname} = %{EVRD}

%description
Library for converting physical units

%package -n %{libname}
Summary: Library for converting physical units
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library for converting physical units

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for converting physical units

%package -n python-kunitconversion
Summary: Python bindings to KUnitConversion
Group: Development/Python
Requires: %{libname} = %{EVRD}

%description -n python-kunitconversion
Python bindings to KUnitConversion

%prep
%autosetup -p1 -n kunitconversion-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kunitconversion.*

%files -n %{devname}
%{_includedir}/KF6/KUnitConversion
%{_libdir}/cmake/KF6UnitConversion

%files -n %{libname}
%{_libdir}/libKF6UnitConversion.so*

%files -n python-kunitconversion
%{_libdir}/python*/site-packages/KUnitConversion.cpython-*.so
