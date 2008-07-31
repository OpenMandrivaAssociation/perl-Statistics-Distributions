%define real_name Statistics-Distributions
%define	name perl-%{real_name}
%define	version 1.02
%define	release %mkrel 5

Summary:	Statistics::Distributions - Perl module for calculating critical values and upper probabilities of common statistical distributions
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIKEK/%{real_name}-%{version}.tar.bz2
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
%setup -q -n %{real_name}-%{version} 

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

