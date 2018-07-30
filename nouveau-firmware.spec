Name:            nouveau-firmware
Version:         340.32
Release:         1%{?dist}
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
* Mon May 25 2015 Nicolas Chauvet <kwizart@gmail.com> - 340.32-1
- Update to 340.32

* Fri Oct 25 2013 Stefan Becker <chemobejk@gmail.com> - 325.08-1
- Initial RPM Release
