Name:           aryan-bbswitch
Version:        0.2
Release:        1%{?dist}
Summary:        BBSwitched packaged for idk_what_to_doooo

License:        MIT
URL:            https://github.com/johnclark456/bbswitch.git
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64


%description
bbswitch, packaged for idk_what_to_doooo

%prep
# we have no source, so nothing here

%build
make

%install
mkdir -p %{buildroot}/opt/modules/
install -m 755 bbswitch.ko %{buildroot}/opt/modules/

%files
/opt/modules/bbswitch.ko

%changelog
* Tue May 24 2022 Johnathon Clark <john.clark@cantab.net> 0.2-1
- new package built with tito

# let's skip this for now