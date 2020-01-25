#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	F77
Summary:	ExtUtils::F77 Perl module - simple interface to F77 libraries
Summary(pl.UTF-8):	Moduł Perla ExtUtils::F77 - prosty interfejs do bibliotek F77
Name:		perl-ExtUtils-F77
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c0143b5342587ed2ee5db3f6cfb9cc13
Patch0:		%{name}-gcc.patch
URL:		http://search.cpan.org/dist/ExtUtils-F77/
BuildRequires:	gcc-fortran
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gcc-fortran
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to figure out how to link C programs with Fortran
subroutines on your system. Basically one must add a list of Fortran
runtime libraries. The problem is their location and name varies with
each OS/compiler combination.

%description -l pl.UTF-8
Ten moduł próbuje odkryć, jak linkować programy w C z obecnymi w
systemie procedurami Fortranu. Zasadniczo polega to na dodaniu listy
fortranowych bibliotek uruchomieniowych. Problem tkwi w ich położeniu
i różnych nazwach w zależności od kombinacji systemu operacyjnego i
kompilatora.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/ExtUtils/F77.pm
%{_mandir}/man3/ExtUtils::F77.3pm*
