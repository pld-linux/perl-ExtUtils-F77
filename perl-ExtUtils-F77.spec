%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	F77
Summary:	ExtUtils::F77 perl module
Summary(pl):	Modu³ perla ExtUtils::F77
Name:		perl-ExtUtils-F77
Version:	1.14
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
Requires:	gcc-g77
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::F77 - Simple interface to F77 libs.

%description -l pl
ExtUtils::F77 - prosty interfejs do bibliotek F77.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_sitelib}/ExtUtils/F77.pm
%{_mandir}/man3/*
