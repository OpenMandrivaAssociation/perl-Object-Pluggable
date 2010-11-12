%define upstream_name    Object-Pluggable
%define upstream_version 1.29

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Importable constants for Object::Pluggable
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Object/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Pod::Parser)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Object::Pluggable is a base class for creating plugin enabled objects. It
is a generic port of POE::Component::IRC's plugin system.

If your object dispatches events to listeners, then Object::Pluggable may
be a good fit for you.

Basic use would involve subclassing Object::Pluggable, then overriding
'_pluggable_event()' and inserting '_pluggable_process()' wherever you
dispatch events from.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


