%global gnulib_ver 20140202

Summary: A pipeline manipulation library
Name: libpipeline
Version: 1.5.0
Release: 2%{?dist}
License: GPLv3+
Group: Development/Libraries
URL: http://libpipeline.nongnu.org/
Source: http://download.savannah.gnu.org/releases/libpipeline/libpipeline-%{version}.tar.gz

BuildRequires: libtool, check-devel

# FPC exception for gnulib - copylib - https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = %{gnulib_ver}

%description
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which is
often error-prone and insecure. This alleviates programmers of the need to
laboriously construct pipelines using lower-level primitives such as fork(2)
and execve(2).

%package devel
Summary: Header files and libraries for pipeline manipulation library
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
libpipeline-devel contains the header files and libraries needed
to develop programs that use libpipeline library.

%prep
%setup -q

%build
%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
rm $RPM_BUILD_ROOT/%{_libdir}/libpipeline.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README ChangeLog NEWS
%{_libdir}/libpipeline.so.*

%files devel
%{_libdir}/libpipeline.so
%{_libdir}/pkgconfig/libpipeline.pc
%{_includedir}/*.h
%{_mandir}/man3/*

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Nikola Forró <nforro@redhat.com> - 1.5.0-1
- update to 1.5.0
  resolves #1512903

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Nikola Forró <nforro@redhat.com> - 1.4.2-1
- update to 1.4.2
  resolves #1469102

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Nikola Forró <nforro@redhat.com> - 1.4.1-1
- updated to 1.4.1
  resolves #1256154

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 jchaloup <jchaloup@redhat.com> - 1.4.0-1
- updated to 1.4.0
  resolves: #1157461

* Tue Sep 23 2014 jchaloup <jchaloup@redhat.com> - 1.3.1-1
- resolves: #1145489
  updated to 1.3.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 1.3.0-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Peter Schiffer <pschiffe@redhat.com> - 1.3.0-1
- resolves: #1081491
  updated to 1.3.0

* Thu Dec 19 2013 Peter Schiffer <pschiffe@redhat.com> - 1.2.6-1
- resolves: #1044974
  updated to 1.2.6

* Wed Dec 11 2013 Peter Schiffer <pschiffe@redhat.com> - 1.2.5-1
- resolves: #1038010
  updated to 1.2.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun  7 2013 Peter Schiffer <pschiffe@redhat.com> - 1.2.4-1
- resolves: #971700
  updated to 1.2.4

* Wed Apr 24 2013 Peter Schiffer <pschiffe@redhat.com> - 1.2.3-1
- resolves: #956003
  updated to 1.2.3

* Tue Mar 19 2013 Peter Schiffer <pschiffe@redhat.com> - 1.2.2-4
- fixed memory leaks detected by valgrind

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.2-2
- resolves: #876108
  fixed size_t underflow in pipeline_readline() function

* Thu Oct 18 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.2-1
- updated to 1.2.2

* Thu Sep 06 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.1-2
- enabled test suite at build time
- cleaned .spec file

* Mon Jul 23 2012 Peter Schiffer <pschiffe@redhat.com> - 1.2.1-1
- update to 1.2.1
- fixed FTBFS caused by gnulib

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Apr 19 2011 Ivana Hutarova Varekova <varekova@redhat.com> - 1.2.0-1
- initial build
