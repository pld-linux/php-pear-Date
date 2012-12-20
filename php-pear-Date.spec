%define		status	alpha
%define		pearname Date
%define		subver	a3
%define		rel		2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - date and time zone classes
Summary(pl.UTF-8):	%{pearname} - klasy daty i stref czasowych
Name:		php-pear-%{pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}%{subver}.tgz
# Source0-md5:	47fc4f78fa8bb10eb9fea545f6ea8831
URL:		http://pear.php.net/package/Date/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 4.2
Requires:	php-pear
Suggests:	php-pear-Numbers_Words
Obsoletes:	php-pear-Date-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define	_noautoreq_pear Numbers/Words.php

%description
Generic classes for representation and manipulation of dates, times
and time zones without the need of timestamps, which is a huge
limitation for PHP programs. Includes time zone data, time zone
conversions and many date/time conversions. It does not rely on 32-bit
system date stamps, so you can display calendars and compare dates
that date pre 1970 and post 2038. This package also provides a class
to convert date strings between Gregorian and Human calendar formats.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Podstawowe klasy do pokazywania i manipulowania datami, czasem i
strefami czasowymi bez potrzeby używania timestamps, które są ogromnym
ograniczeniem programów w PHP. Zawiera konwersję stref czasowych,
czasu, daty, bazowane na Date::Calc. Nie zależy od 32-bitowych
systemowych timestampów, więc może wyświetlać kalendarz oraz
porównywać daty prze 1970 i po 2038 roku. Ten pakiet zawiera także
klasy do konwersji ciągów znakowych pomiędzy kalendarzem gregoriańskim
i ludzkim.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Date/README .

mv .%{php_pear_dir}/buildPackageXML.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%doc docs/Date/docs/TODO
%dir %{php_pear_dir}/Date
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/Date/*.php
