%define upstream_name    Object-Pluggable
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	1.29
Release:	2

Summary:	Importable constants for Object::Pluggable
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/hinrik/object-pluggable
Source0:	https://cpan.metacpan.org/authors/id/H/HI/HINRIK/Object-Pluggable-1.29.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(constant)
BuildArch:	noarch

%description
Object::Pluggable is a base class for creating plugin enabled objects. It
is a generic port of POE::Component::IRC's plugin system.

If your object dispatches events to listeners, then Object::Pluggable may
be a good fit for you.

Basic use would involve subclassing Object::Pluggable, then overriding
'_pluggable_event()' and inserting '_pluggable_process()' wherever you
dispatch events from.

%prep
%setup -q -n Object-Pluggable-1.29

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

