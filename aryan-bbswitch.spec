Name:           aryan-bbswitch
Version:        0.6
Release:        1%{?dist}
Summary:        BBSwitched packaged for idk_what_to_doooo

License:        MIT
URL:            https://github.com/johnclark456/bbswitch.git
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64


%description
bbswitch, packaged for idk_what_to_doooo

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
mkdir -p %{buildroot}/opt/modules/
install -m 755 bbswitch.ko %{buildroot}/opt/modules/
mkdir -p %{buildroot}/etc/systemd/system/
install -m 644 bbswitch.service %{buildroot}/etc/systemd/system/

%files
/opt/modules/bbswitch.ko
/etc/systemd/system/bbswitch.service

%changelog
* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net> 0.6-1
- Add bbservice.service (john.clark@cantab.net)

* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net> 0.5-1
- Created service file

* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net> 0.4-1
- Fix for kernel 5.17 (john.clark@cantab.net)

* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net>
- Fix for kernel 5.17 (john.clark@cantab.net)

* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net> 0.3-1
- new package built with tito

* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net> 0.2-1
- new package built with tito
