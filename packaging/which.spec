Name:       which
Summary:    Which, what, where?
Version:    0.1
Release:    1
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch

%description
Shows the path of a file

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir}/
install -m755 which %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}


%files
%manifest which.manifest
%{_bindir}/which
/usr/share/license/%{name}
