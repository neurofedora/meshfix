%global rev r60

Name:           meshfix
Version:        1.2
Release:        1.%{rev}%{?dist}
Summary:        Repairing and modification of triangle meshes

License:        GPLv2+ and Public Domain
URL:            https://code.google.com/p/meshfix/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 60 http://meshfix.googlecode.com/svn/trunk/ meshfix-r60
#  tar -cvf meshfix-r60.tar.xz meshfix-r60
Source0:        %{name}-%{rev}.tar.xz
Patch0:         meshfix-build-fix.patch
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  gcc-c++
# contrib/JMeshLib/
# it's 1.1 version, but somehow modified without any comments
Provides:       bundled(jmeshlib) = 1.1
# contrib/jrs_predicates/jrs_predicates.[ch]
Provides:       bundled(jrs_predicates)
BuildRequires:  OpenNL-devel
BuildRequires:  /usr/bin/chrpath

%description
%{summary}.

%prep
%autosetup -n %{name}-%{rev} -S git
rm -rf build/
mkdir -p build/

%build
pushd build/
  %cmake ../
  %make_build
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 build/%{name} %{buildroot}%{_bindir}
chrpath -d %{buildroot}%{_bindir}/%{name}

%check
pushd test
  sed -i -e 's|\.\./meshfix|%{buildroot}%{_bindir}/%{name}|' *.sh
  find -name '*.sh' -exec {} ';'
popd

%files
%license gpl.txt
%doc readme.txt
%{_bindir}/%{name}

%changelog
* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.2-1.r60
- Initial package
