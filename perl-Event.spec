#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Event
Version  : 1.28
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Event-1.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Event-1.28.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libe/libevent-perl/libevent-perl_1.26-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Event-license = %{version}-%{release}
Requires: perl-Event-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Event - A Generic Perl Event Loop
This extension aims to provide an simple and optimized event loop for
a broad class of applications.

%package dev
Summary: dev components for the perl-Event package.
Group: Development
Provides: perl-Event-devel = %{version}-%{release}
Requires: perl-Event = %{version}-%{release}

%description dev
dev components for the perl-Event package.


%package license
Summary: license components for the perl-Event package.
Group: Default

%description license
license components for the perl-Event package.


%package perl
Summary: perl components for the perl-Event package.
Group: Default
Requires: perl-Event = %{version}-%{release}

%description perl
perl components for the perl-Event package.


%prep
%setup -q -n Event-1.28
cd %{_builddir}
tar xf %{_sourcedir}/libevent-perl_1.26-1.debian.tar.xz
cd %{_builddir}/Event-1.28
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Event-1.28/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Event
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Event/8f95a1dcbae8ac3fea4de9884269e7a201eba950
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Event.3
/usr/share/man/man3/Event::MakeMaker.3
/usr/share/man/man3/Event::generic.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Event/8f95a1dcbae8ac3fea4de9884269e7a201eba950

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/EventAPI.h
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/MakeMaker.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/Watcher.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/generic.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/generic.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/group.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/idle.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/io.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/signal.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/timer.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/type.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/typemap
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Event/var.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Event/Event.so
