#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-docstrings
Version  : 1.0.2
Release  : 7
URL      : http://pypi.debian.net/flake8-docstrings/flake8-docstrings-1.0.2.tar.gz
Source0  : http://pypi.debian.net/flake8-docstrings/flake8-docstrings-1.0.2.tar.gz
Summary  : Extension for flake8 which uses pydocstyle to check docstrings
Group    : Development/Tools
License  : MIT
Requires: flake8-docstrings-python
BuildRequires : flake8
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
flake8-docstrings
=================
A simple module that adds an extension for the fantastic pydocstyle_ tool to
flake8_.

%package python
Summary: python components for the flake8-docstrings package.
Group: Default

%description python
python components for the flake8-docstrings package.


%prep
%setup -q -n flake8-docstrings-1.0.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
