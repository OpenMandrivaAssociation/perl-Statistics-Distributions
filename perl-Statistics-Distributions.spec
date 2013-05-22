%define upstream_name    Statistics-Distributions
%define	upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	Calc critical values & upper probabilities of common statistical distributions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIKEK/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This Perl module calculates percentage points (5 significant digits)
of the u (standard normal) distribution, the student's t distribution,
the chi-square distribution and the F distribution. It can also
calculate the upper probability (5 significant digits) of the u
(standard normal), the chi-square, the t and the F distribution.

These critical values are needed to perform statistical tests, like
the u test, the t test, the F test and the chi-squared test, and to
calculate confidence intervals.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Statistics/*.pm
%{perl_vendorlib}/auto/Statistics/Distributions/autosplit.ix
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-4mdv2012.0
+ Revision: 765654
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-3
+ Revision: 764166
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-2
+ Revision: 676911
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 404413
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.02-5mdv2009.0
+ Revision: 258385
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.02-4mdv2009.0
+ Revision: 246464
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.02-2mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2008.0
+ Revision: 86919
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.02-1mdv2007.0
- rebuild

* Mon Jul 11 2005 Oden Eriksson <oeriksson@mandriva.com> 1.02-1mdk
- initial Mandriva package

