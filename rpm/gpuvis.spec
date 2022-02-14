%global commit 02b534e7d918501a55147effcf5535638a6f5a0f
%global shortcommit %(c=%{commit}; echo ${c:0:7})	
%global commit_date 20220213

Name:		gpuvis
Version:        0.1
Release:        1%{?dist}
Summary:        GPU Trace Visualizer

License:        MIT
URL:            https://github.com/mikesart/gpuvis
Source0:	https://github.com/mikesart/gpuvis/archive/%{name}-%{commit}.tar.gz
Source1:	com.github.%{name}.Gpuvis.desktop
Source2:	com.github.%{name}.Gpuvis.metainfo.xml
Source3:	com.github.%{name}.Gpuvis.svg

BuildRequires:  g++ gcc
BuildRequires:	rapidjson-devel
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  meson SDL2-devel freetype-devel gtk3-devel libstdc++-devel pkg-config


%description
Gpuvis is a Linux GPU profiler similar to GPUView on Windows. 
It is designed to work with trace-cmd captures and help track 
down Linux gpu and application performance issues.

%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install

#enable desktop application
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications/		\
%{SOURCE1}
mkdir -p %{buildroot}%{_metainfodir} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 755 %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.github.%{name}.Gpuvis.svg

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/com.github.%{name}.Gpuvis.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.%{name}.Gpuvis.svg
%doc README.md


%changelog
* Mon Feb 14 2022 Dorinda Bassey <dbassey@redhat.com> - 0.1-1
- Add Icon
- Fetch upstream

* Thu Jan 27 2022 Dorinda Bassey <dbassey@redhat.com> - 0.1-1
- Add patch to handle RapidJSON dependency in meson build

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
