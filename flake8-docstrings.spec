#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-docstrings
Version  : 1.6.0
Release  : 42
URL      : https://files.pythonhosted.org/packages/c1/a6/b8a953fb256ee383fed9094f7270ab75cd637c23749c211f0e6b3552a31e/flake8-docstrings-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c1/a6/b8a953fb256ee383fed9094f7270ab75cd637c23749c211f0e6b3552a31e/flake8-docstrings-1.6.0.tar.gz
Summary  : Extension for flake8 which uses pydocstyle to check docstrings
Group    : Development/Tools
License  : MIT
Requires: flake8-docstrings-license = %{version}-%{release}
Requires: flake8-docstrings-python = %{version}-%{release}
Requires: flake8-docstrings-python3 = %{version}-%{release}
Requires: flake8
Requires: pydocstyle
BuildRequires : buildreq-distutils3
BuildRequires : flake8
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
Requires: flake8-docstrings-python3 = %{version}-%{release}

%description python
python components for the flake8-docstrings package.


%package python3
Summary: python3 components for the flake8-docstrings package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_docstrings)
Requires: pypi(flake8)
Requires: pypi(pydocstyle)

%description python3
python3 components for the flake8-docstrings package.


%prep
%setup -q -n flake8-docstrings-1.6.0
cd %{_builddir}/flake8-docstrings-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616163407
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flake8-docstrings
cp %{_builddir}/flake8-docstrings-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/flake8-docstrings/a2c9ace5fabfdb17da21cef10ebcd4c2a2736dc5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flake8-docstrings/a2c9ace5fabfdb17da21cef10ebcd4c2a2736dc5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
