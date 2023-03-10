#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sparsezoo
Version  : 1.3.1
Release  : 2
URL      : https://github.com/neuralmagic/sparsezoo/archive/refs/tags/v1.3.1.tar.gz
Source0  : https://github.com/neuralmagic/sparsezoo/archive/refs/tags/v1.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: sparsezoo-bin = %{version}-%{release}
Requires: sparsezoo-license = %{version}-%{release}
Requires: sparsezoo-python = %{version}-%{release}
Requires: sparsezoo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

%package bin
Summary: bin components for the sparsezoo package.
Group: Binaries
Requires: sparsezoo-license = %{version}-%{release}

%description bin
bin components for the sparsezoo package.


%package license
Summary: license components for the sparsezoo package.
Group: Default

%description license
license components for the sparsezoo package.


%package python
Summary: python components for the sparsezoo package.
Group: Default
Requires: sparsezoo-python3 = %{version}-%{release}

%description python
python components for the sparsezoo package.


%package python3
Summary: python3 components for the sparsezoo package.
Group: Default
Requires: python3-core
Provides: pypi(sparsezoo)

%description python3
python3 components for the sparsezoo package.


%prep
%setup -q -n sparsezoo-1.3.1
cd %{_builddir}/sparsezoo-1.3.1
pushd ..
cp -a sparsezoo-1.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674058704
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . click
pypi-dep-fix.py . numpy
pypi-dep-fix.py . protobuf
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . click
pypi-dep-fix.py . numpy
pypi-dep-fix.py . protobuf
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sparsezoo
cp %{_builddir}/sparsezoo-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/sparsezoo/0dece4cd82f7d1f382592ee79318ac0126c1aee7 || :
cp %{_builddir}/sparsezoo-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/sparsezoo/321caeefde174c62217e56cf8953ae8005911dc3 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} click
pypi-dep-fix.py %{buildroot} numpy
pypi-dep-fix.py %{buildroot} protobuf
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sparsezoo
/usr/bin/sparsezoo.download

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sparsezoo/0dece4cd82f7d1f382592ee79318ac0126c1aee7
/usr/share/package-licenses/sparsezoo/321caeefde174c62217e56cf8953ae8005911dc3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
