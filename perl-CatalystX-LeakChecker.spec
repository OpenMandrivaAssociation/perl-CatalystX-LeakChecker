%define upstream_name    CatalystX-LeakChecker
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Debug memory leaks in Catalyst applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CatalystX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B::Deparse)
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Devel::Cycle)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::AttributeHelpers)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::SimpleTable)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
It's easy to create memory leaks in Catalyst applications and often they're
hard to find. This module tries to help you finding them by automatically
checking for common causes of leaks.

This module is intended for debugging only. I suggest to not enable it in a
production environment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


