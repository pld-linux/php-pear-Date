%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_status		stable

%define		_pearname	%{_class}
Summary:	%{_pearname} - Date and Time Zone Classes
Summary(pl):	%{_pearname} - Klasy daty i stref czasowych
Name:		php-pear-%{_pearname}
Version:	1.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	b3d837c131df195c58cc21d344bef1b7
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic classes for representation and manipulation of dates, times
and time zones without the need of timestamps, which is a huge
limitation for php programs. Includes time zone data, time zone
conversions and many date/time conversions. It does not rely on 32-bit
system date stamps, so you can display calendars and compare dates
that date pre 1970 and post 2038. This package also provides a class
to convert date strings between Gregorian and Human calendar formats.

This class has in PEAR status: %{_status}.

%description -l pl
Podstawowe klasy do pokazywania i manipulowania datami, czasem i
strefami czasowymi bez potrzeby u¿ywania timestamps, które s± ogromnym
ograniczeniem programów php. Zawiera konwersjê stref czasowych, czasu,
daty, bazowane na Date::Calc. Nie zale¿y od 32-bitowych systemowych
timestampów, wiêc mo¿e wy¶wietlaæ kalendarz oraz porównywaæ daty prze
1970 i po 2038 roku. Ten pakiet zawiera tak¿e klasy do konwersji
ci±gów znakowych pomiêdzy kalendarzem gregoriañskim i ludzkim.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
