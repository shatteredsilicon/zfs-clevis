%global version 1.0
%global dracutmodule /usr/lib/dracut/modules.d/90zfs-clevis

Name:		   zfs-clevis
Version:	   %{version}
Release:	   1
BuildArch:	   noarch
Summary:	   A Dracut module to unlock zfs datasets with clevis during boot
Group:		   Applications/System
License:	   GPLv3
URL:		   https://github.com/shatteredsilicon/%{name}
Source0:	   https://github.com/shatteredsilicon/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:          dracut, clevis

%description
A Dracut module to unlock zfs datasets with clevis during boot

%prep
%setup -q

%build
echo "Nothing to build"

%install
%{__install} -d -m 0755 %{buildroot}/%{dracutmodule}
%{__install} -m 0744 module-setup.sh %{buildroot}/%{dracutmodule}
%{__install} -m 0744 fetch-keys.sh %{buildroot}/%{dracutmodule}
%{__install} -d -m 0755 %{buildroot}/etc/dracut.conf.d/
%{__install} -m 0644 zfs-clevis.conf %{buildroot}/etc/dracut.conf.d/

%files
%dir %{dracutmodule}
%{dracutmodule}/module-setup.sh
%{dracutmodule}/fetch-keys.sh
/etc/dracut.conf.d/zfs-clevis.conf

%changelog
* Fri Oct 13 2023 Niall Daley <niall@shatteredsilicon.net> - 1.1-1
- Enable module by default

* Thu Oct 12 2023 Niall Daley <niall@shatteredsilicon.net> - 1.0-1
- Initial pack of dracut module files. 

