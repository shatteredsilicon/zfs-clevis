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
setup -q

%build
echo "Nothing to build"

%install
%{__install} -d %{dracutmodule}
%{__install} -m 0744 module-setup.sh %{dracutmodule}
%{__install} -m 0744 fetch-keys.sh %{dracutmodule}

%files
%dir %{dracutmodule}
%dir %{dracutmodule}/module-setup.sh
%dir %{dracutmodule}/fetch-keys.sh

%changelog
* Thu Oct 12 2023 Niall Daley <niall@shatteredsilicon.net> - 1.0-1
- Initial pack of dracut module files. 

