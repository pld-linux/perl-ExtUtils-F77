%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-F77 perl module
Summary(pl):	Modu³ perla ExtUtils-F77
Name:		perl-ExtUtils-F77
Version:	1.12
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-F77-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-F77 - Simple interface to F77 libs.

%description -l pl
ExtUtils-F77 - prosty interfejs do bibliotek F77.

%prep
%setup -q -n ExtUtils-F77-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/ExtUtils/F77
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz

%{perl_sitelib}/ExtUtils/F77.pm
%{perl_sitearch}/auto/ExtUtils/F77

%{_mandir}/man3/*
