#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Random
Summary:	String::Random - Perl module to generate random strings based on a pattern
Summary(pl):	String::Random - modu³ Perla do generowania losowych ³añcuchów na podstawie wzoru
Name:		perl-String-Random
Version:	0.198
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5556b44648a80b0bcb0114eecc5d4082
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Random is used to generate random strings.  It was written to
make generating random passwords and such a little easier.

%description -l pl
Modu³ String::Random s³u¿y do generowania losowych ³añcuchów. Zosta³
napisany, aby uczyniæ znacznie ³atwiejszym generowanie losowych hase³.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
