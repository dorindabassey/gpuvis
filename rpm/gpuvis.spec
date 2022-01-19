%global commit 9439b5b1e8016f628b9c2f8e7bffb52a0dea193c
%global shortcommit %(c=%{commit}; echo ${c:0:7})	
%global commitdate 20220119
%global rapidjson_version 1.1.0
%global rapidjson_release 16

Name:		gpuvis
Version:        0
Release:        1.%{commitdate}.git%{shortcommit}%{?dist}
Summary:        GPU Trace Visualizer

License:        MIT
URL:            https://github.com/mikesart/gpuvis
Source0:	https://github.com/mikesart/gpuvis/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:	https://github.com/Tencent/rapidjson/archive/1c2c8e085a8b2561dff17bedb689d2eb0609b689.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.metainfo.xml

BuildRequires:  g++ gcc
BuildRequires:	rapidjson-devel >= %{rapidjson_version}-%{rapidjson_release}
BuildRequires:  desktop-file-utils libappstream-glib rapidjson
BuildRequires:  meson SDL2-devel freetype-devel gtk3-devel libstdc++-static libstdc++-devel glibc-static pkg-config


%description
Gpuvis is a Linux GPU profiler similar to GPUView on Windows. 
It is designed to work with trace-cmd captures and help track 
down Linux gpu and application performance issues.

%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install

#enable desktop application
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications/		\
%{SOURCE2}
mkdir -p %{buildroot}%{_metainfodir}
install -m 755 %{SOURCE3} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%doc README.md


%changelog
* Wed Jan 19 2022 Dorinda Bassey <dbassey@redhat.com> - 0-1
- fix Makefile Upstream, remove ppc64le support
- Use meson build
- Update Sources

* Wed Jan 19 2022 Dorinda Bassey <dbassey@redhat.com> - 0-1
- Add support for ppc64le in Makefile

* Tue Jan 18 2022 Dorinda Bassey <dbassey@redhat.com> - 0-1
- Install the Desktop file
- Exclude ppc64le because -march=native option in makefile not supported on powerpc
- Fix Version

* Thu Jan 13 2022 Dorinda Bassey <dbassey@redhat.com> - 0-1
- Initial Packaged Version
- Created Install path
