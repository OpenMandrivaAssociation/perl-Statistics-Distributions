%define modname	Statistics-Distributions
%define	modver	1.02

Summary:	Calc critical values & upper probabilities of common statistical distributions
Name:		perl-%{modname}
Version:	%{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Statistics-Distributions
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIKEK/Statistics-Distributions-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Statistics/*.pm
%{perl_vendorlib}/auto/Statistics/Distributions/autosplit.ix
%{_mandir}/man3/*

