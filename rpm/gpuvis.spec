%global rapidjson_version 1.1.0
%global rapidjson_release 16

Name:		gpuvis
Version:        0.1
Release:        1%{?dist}
Summary:        GPU Trace Visualizer

License:        MIT
URL:            https://github.com/mikesart/gpuvis
Source0:	https://github.com/mikesart/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.metainfo.xml

BuildRequires:  g++ gcc
BuildRequires:	rapidjson-devel >= %{rapidjson_version}-%{rapidjson_release}
BuildRequires:  desktop-file-utils libappstream-glib rapidjson
BuildRequires:  meson SDL2-devel freetype-devel gtk3-devel libstdc++-static libstdc++-devel glibc-static pkg-config


%description
Gpuvis is a Linux GPU profiler similar to GPUView on Windows. 
It is designed to work with trace-cmd captures and help track 
down Linux gpu and application performance issues.

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

#enable desktop application
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications/		\
%{SOURCE1}
mkdir -p %{buildroot}%{_metainfodir}
install -m 755 %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%doc README.md


%changelog
* Mon Jan 24 2022 Dorinda Bassey <dbassey@redhat.com> - 0.1-1
- v0 -> v0.1.

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
