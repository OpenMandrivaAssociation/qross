%define	major	0.1
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname %{oname} -d
%define	oname Qross


Name:           qross
Version:        0.3.1
Release:        2
License:        LGPLv2+
Summary:        A Qt-only fork of Kross
Url:            https://github.com/0xd34df00d/Qross
Group:          System/Libraries
# WARNING: don't forget to remove at least
# src/bindings/csharp directory from upstream sources,
# really only src/bindings/python works now, see more at
Source0:        %{oname}-%{version}.tar.xz

BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  pkgconfig(QtCore)
Requires:  %{libname} = %{EVRD}


%description
Qross is a Qt-only fork of Kross
the KDE scripting framework.
The Qross scripting framework is 
not a scripting language itself. 
It merely serves to plug into C++/Qt 
applications the support for 
other, already existing scripting 
languages, like JavaScript or
Python.


%files  
%doc docs/CHANGES
%{_bindir}/%{name}


%package -n %{libname}
Summary:        A Qt-only fork of Kross
Group:          System/Libraries

%description   -n %{libname}
Qross is a Qt-only fork of Kross
the KDE scripting framework.
The Qross scripting framework is 
not a scripting language itself. 
It merely serves to plug into C++/Qt 
applications the support for 
other, already existing scripting 
languages, like JavaScript or
Python.

%files   -n %{libname}
%doc docs/CHANGES
%{_libdir}/*%{name}*.so.*
%{_libdir}/qt4/plugins/script/*%{name}*.so.*
#-------------------------------------

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       cmake
Requires:       %{libname} = %{EVRD}
Requires:       pkgconfig(QtCore)
Provides:       Qross-devel = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%files -n %{devname}
%doc docs/CHANGES
%{_includedir}/%{name}
%{_libdir}/*%{name}*.so
%{_libdir}/qt4/plugins/script/*%{name}*.so
%dir %{_datadir}/leechcraft
%dir %{_datadir}/leechcraft/cmake
%{_datadir}/*/*/FindQrosscore.cmake
#-------------------------------------

%prep
%setup -qn %{oname}-%{version}/src/%{name}


%build
mkdir build && cd build

cmake .. \
%ifarch x86_64
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

%make VERBOSE=1


%install
cd build
%make_install

%fdupes -s %{buildroot}%{_datadir}






