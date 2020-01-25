#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Wifi
%define	pnam	WpaCtrl
Summary:	Wifi::WpaCtrl - wpa_supplicant/hostapd control interface library
Summary(pl.UTF-8):	Wifi::WpaCtrl - interfejs do sterowania wpa_supplicantem/hostapd
Name:		perl-Wifi-WpaCtrl
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FL/FLORA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fd6b4d8d3e7c5b785c425c56d15a6015
URL:		http://search.cpan.org/dist/Wifi-WpaCtrl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a wrapper around wpa_ctrl.[ch] supplied by
wpa_supplicant. It may be used to communicate with
wpa_supplicant/hostapd in various ways.

%description -l pl.UTF-8
Ten moduł obudowuje wpa_ctrl.[ch] dostarczane z wpa_supplicantem. Może
być używany do komunikacji z wpa_supplicantem/hostapd na różne
sposoby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorarch}/Wifi/WpaCtrl.pm
%dir %{perl_vendorarch}/auto/Wifi/WpaCtrl
%attr(755,root,root) %{perl_vendorarch}/auto/Wifi/WpaCtrl/WpaCtrl.so
%{_mandir}/man3/Wifi::WpaCtrl.3pm*
