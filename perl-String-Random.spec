#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	String
%define		pnam	Random
Summary:	String::Random - Perl module to generate random strings based on a pattern
Summary(pl.UTF-8):	String::Random - moduł Perla do generowania losowych łańcuchów na podstawie wzoru
Name:		perl-String-Random
Version:	0.30
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d54ea58b992d9a2a1966051a4816693f
URL:		http://search.cpan.org/dist/String-Random/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Random is used to generate random strings.  It was written to
make generating random passwords and such a little easier.

%description -l pl.UTF-8
Moduł String::Random służy do generowania losowych łańcuchów. Został
napisany, aby uczynić znacznie łatwiejszym generowanie losowych haseł.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
