%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - date and time zone classes
Summary(pl):	%{_pearname} - klasy daty i stref czasowych
Name:		php-pear-%{_pearname}
Version:	1.4.3
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e1ac9ae6469584e6f887b6fd020b3ae1
Patch0:		%{name}-tz-baltic-hasdst.patch
URL:		http://pear.php.net/package/Date/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Podstawowe klasy do pokazywania i manipulowania datami, czasem i
strefami czasowymi bez potrzeby u¿ywania timestamps, które s± ogromnym
ograniczeniem programów w PHP. Zawiera konwersjê stref czasowych,
czasu, daty, bazowane na Date::Calc. Nie zale¿y od 32-bitowych
systemowych timestampów, wiêc mo¿e wy¶wietlaæ kalendarz oraz
porównywaæ daty prze 1970 i po 2038 roku. Ten pakiet zawiera tak¿e
klasy do konwersji ci±gów znakowych pomiêdzy kalendarzem gregoriañskim
i ludzkim.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
%doc docs/%{_pearname}/TODO
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
