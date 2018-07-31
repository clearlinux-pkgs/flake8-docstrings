#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-docstrings
Version  : 1.3.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/a5/8c/93d397e26d732ff4978b0c1568bd9ef02f0ef7aac5763ec5c9b25ed252f5/flake8-docstrings-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/8c/93d397e26d732ff4978b0c1568bd9ef02f0ef7aac5763ec5c9b25ed252f5/flake8-docstrings-1.3.0.tar.gz
Summary  : Extension for flake8 which uses pydocstyle to check docstrings
Group    : Development/Tools
License  : MIT
Requires: flake8-docstrings-python3
Requires: flake8-docstrings-license
Requires: flake8-docstrings-python
Requires: flake8
Requires: flake8-polyfill
Requires: pydocstyle
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : flake8-polyfill
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pydocstyle
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
=================
        
        A simple module that adds an extension for the fantastic pydocstyle_ tool to
        flake8_.

%package license
Summary: license components for the flake8-docstrings package.
Group: Default

%description license
license components for the flake8-docstrings package.


%package python
Summary: python components for the flake8-docstrings package.
Group: Default
Requires: flake8-docstrings-python3

%description python
python components for the flake8-docstrings package.


%package python3
Summary: python3 components for the flake8-docstrings package.
Group: Default
Requires: python3-core

%description python3
python3 components for the flake8-docstrings package.


%prep
%setup -q -n flake8-docstrings-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533001940
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/flake8-docstrings
cp LICENSE %{buildroot}/usr/share/doc/flake8-docstrings/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/flake8-docstrings/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
