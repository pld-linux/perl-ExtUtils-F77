%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-F77 perl module
Summary(pl):	Modu³ perla ExtUtils-F77
Name:		perl-ExtUtils-F77
Version:	1.13
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-F77-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Requires:	gcc-g77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-F77 - Simple interface to F77 libs.

%description -l pl
ExtUtils-F77 - prosty interfejs do bibliotek F77.

%prep
%setup -q -n ExtUtils-F77-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/ExtUtils/F77.pm
%{_mandir}/man3/*
