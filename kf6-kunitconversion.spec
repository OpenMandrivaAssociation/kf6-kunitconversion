%define libname %mklibname KF6UnitConversion
%define devname %mklibname KF6UnitConversion -d
%define git 20230802

Name: kf6-kunitconversion
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kunitconversion/-/archive/master/kunitconversion-master.tar.bz2#/kunitconversion-%{git}.tar.bz2
Summary: Library for converting physical units
URL: https://invent.kde.org/frameworks/kunitconversion
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
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
%{_qtdir}/mkspecs/modules/qt_KUnitConversion.pri
%{_qtdir}/doc/KF6UnitConversion.*

%files -n %{libname}
%{_libdir}/libKF6UnitConversion.so*
