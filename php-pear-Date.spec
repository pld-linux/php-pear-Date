%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - date and time zone classes
Summary(pl.UTF-8):	%{_pearname} - klasy daty i stref czasowych
Name:		php-pear-%{_pearname}
Version:	1.4.7
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6d34306e484d46c205002f8900ce6da3
Patch0:		%{name}-tz-baltic-hasdst.patch
URL:		http://pear.php.net/package/Date/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic classes for representation and manipulation of dates, times
and time zones without the need of timestamps, which is a huge
limitation for PHP programs. Includes time zone data, time zone
conversions and many date/time conversions. It does not rely on 32-bit
system date stamps, so you can display calendars and compare dates
that date pre 1970 and post 2038. This package also provides a class
to convert date strings between Gregorian and Human calendar formats.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Podstawowe klasy do pokazywania i manipulowania datami, czasem i
strefami czasowymi bez potrzeby używania timestamps, które są ogromnym
ograniczeniem programów w PHP. Zawiera konwersję stref czasowych,
czasu, daty, bazowane na Date::Calc. Nie zależy od 32-bitowych
systemowych timestampów, więc może wyświetlać kalendarz oraz
porównywać daty prze 1970 i po 2038 roku. Ten pakiet zawiera także
klasy do konwersji ciągów znakowych pomiędzy kalendarzem gregoriańskim
i ludzkim.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/Date/docs/TODO
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
