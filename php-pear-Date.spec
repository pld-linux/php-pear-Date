%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_pearname	%{_class}
Summary:	%{_class} - Date and Time Zone Classes
Summary(pl):	%{_class} - Klasy daty i stref czasowych
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic classes for representation and manipulation of dates, times
and time zones. Includes time zone data, time zone conversions and
many date/time conversions based on Date::Calc.

%description -l pl
Podstawowe klasy do pokazywania i manipulowania datami, czasem i
strefami czasowymi. Zawiera konwersjê stref czasowych, czasu, daty,
bazowane na Date::Calc.

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
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
