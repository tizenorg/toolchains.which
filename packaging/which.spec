Name:       which
Summary:    Which, what, where?
Version:    0.1
Release:    1
License:    SMAIL GENERAL PUBLIC LICENSE
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/which.manifest 
BuildArch:  noarch

%description
Shows the path of a file

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
mkdir -p %{buildroot}/%{_bindir}/
install -m755 which %{buildroot}/%{_bindir}/

# Tizen SDK license
mkdir -p %{buildroot}/usr/share/license
cp debianutils.copyright %{buildroot}/usr/share/license/%{name}

%files
%manifest which.manifest
%{_bindir}/which
/usr/share/license/%{name}
