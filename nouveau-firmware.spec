Name:            nouveau-firmware
Version:         340.32
Release:         10%{?dist}
Summary:         Firmware files used by the nouveau Linux kernel driver

License:         Redistributable, no modification permitted
URL:             https://nouveau.freedesktop.org/wiki/VideoAcceleration/
Source0:         https://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source1:         https://raw.github.com/imirkin/re-vp2/master/extract_firmware.py
Source2:         https://raw.github.com/imirkin/re-vp2/master/README

BuildRequires:   python2-devel

BuildArch:       noarch

%description
This package includes firmware files required for the nouveau kernel driver
to activate Video acceleration on certain NVIDIA devices.


%prep
%setup -q -c -T
sh %{SOURCE0} --extract-only
cp NVIDIA-Linux*/LICENSE .
cp %{SOURCE2} .


%build
%{__python2} %{SOURCE1}


%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/nouveau
find -maxdepth 1 ! -type d \( -name "nv*" -o -name "vuc*" \)  | xargs mv -t %{buildroot}%{_prefix}/lib/firmware/nouveau


%files
%doc README
%license LICENSE
%dir %{_prefix}/lib/firmware/nouveau
%{_prefix}/lib/firmware/nouveau/*


%changelog
* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 340.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 340.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 340.32-2
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Mon May 25 2015 Nicolas Chauvet <kwizart@gmail.com> - 340.32-1
- Update to 340.32

* Fri Oct 25 2013 Stefan Becker <chemobejk@gmail.com> - 325.08-1
- Initial RPM Release
