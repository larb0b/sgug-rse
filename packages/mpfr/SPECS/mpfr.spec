Summary: A C library for multiple-precision floating-point computations
Name: mpfr
Version: 4.0.1
Release: 5%{?dist}
URL: http://www.mpfr.org/
# GFDL (mpfr.texi, mpfr.info and fdl.texi)
License: LGPLv3+ and GPLv3+ and GFDL
BuildRequires: autoconf libtool gmp-devel gcc
Requires: gmp >= 4.2.3

Source0: http://www.mpfr.org/%{name}-%{version}/%{name}-%{version}.tar.xz

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=11783&view=revision
# http://www.mpfr.org/mpfr-3.1.6/patch01
#Patch0: rev11783.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=11982&view=revision
# http://www.mpfr.org/mpfr-3.1.6/patch02
#Patch1: rev11982.patch

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

%package devel
Summary: Development files for the MPFR library
Requires: %{name}%{?_isa} = %{version}-%{release}
# https://fedoraproject.org/wiki/Packaging:Scriptlets#Texinfo
%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%global info_scriptlet 1
Requires(post): info
Requires(preun): info
%endif
Requires: gmp-devel

%description devel
Header files and documentation for using the MPFR 
multiple-precision floating-point library in applications.

If you want to develop applications which will use the MPFR library,
you'll need to install the mpfr-devel package. You'll also need to
install the mpfr package.

%prep
%autosetup -p1

%build
%configure --disable-assert --disable-static
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libmpfr.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/AUTHORS
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/BUGS
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/FAQ.html
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/NEWS
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/TODO

#these go into licenses, not doc
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/COPYING  $RPM_BUILD_ROOT%{_pkgdocdir}/COPYING.LESSER

%check
make %{?_smp_mflags} check

#%ldconfig_scriptlets

%files
%license COPYING COPYING.LESSER
%doc NEWS README AUTHORS BUGS TODO doc/FAQ.html
%{_libdir}/libmpfr.so.*

%files devel
%{_pkgdocdir}/examples
%{_libdir}/libmpfr.so
%{_includedir}/*.h
%{_infodir}/mpfr.info*
%{_libdir}/pkgconfig/mpfr.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.6-3
- update scriptlets (#1644106)
- use %%make_build %%make_install

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 25 2018 James Paul Turner <jamesturner246@fedoraproject.org> - 3.1.6-1
- Update to MPFR version 3.1.6
- Use autosetup specfile macro for applying patches (patches 1 and 2 applied)
- Removed iconv calls, as they were breaking .info files, which are now unicode
  resolves #1299649
- Other minor cleanups
- BuildRequire gcc per https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar  4 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.5-3
- Examples should be in devel
- Minor cleanups

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 3.1.5-2
- Add missing %%license macro

* Tue Sep 27 2016 Frantisek Kluknavsky <fkluknav@redhat.com> - 3.1.5-1
- rebase

* Tue Mar 08 2016 Frantisek Kluknavsky <fkluknav@redhat.com> - 3.1.4-1
- Rebase

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Dan Horák <dan[at]danny.cz> - 3.1.3-3
- drop support for F<20

* Fri Oct 23 2015 David Sommerseth <davids@redhat.com> - 3.1.3-2
- Fixed missing packaging of doc files

* Tue Jun 23 2015 Frantisek Kluknavsky <fkluknav@redhat.com> - 3.1.3-1
- rebase to 3.1.3
- limboverflow.patch already in tarball, dropped

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Frantisek Kluknavsky <fkluknav@redhat.com> - 3.1.2-8
- added limboverflow.patch, rhbz#1171701, rhbz#1171710, there was one less limb allocated in strtofr

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.2-4
- Install docs into unversioned docdir (Fix FTBFS RHBZ#992296).
- Append --disable-static to %%configure.
- Fix broken %%changelog date.
- Remove stray cd ..

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 Karsten Hopp <karsten@redhat.com> 3.1.2-2
- bump release and rebuild to fix dependencies on PPC

* Fri Mar 22 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 3.1.2-1
- Rebase to 3.1.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 26 2012 Peter Schiffer <pschiffe@redhat.com> - 3.1.1-1
- resolves: #837563
  update to 3.1.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Peter Schiffer <pschiffe@redhat.com> - 3.1.0-1
- resolves: #743237
  update to 3.1.0
- removed compatibility symlinks and provides

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.0.0-4.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 3.0.0-4.1
- rebuild with new gmp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  7 2010 Dan Horák <dan[at]danny.cz> 3.0.0-3
- update the compat Provides for non-x86 arches

* Wed Dec  1 2010 Ivana Hutarova Varekova <varekova@redhat.com> 3.0.0-2
- fix -devel description (see 603021#c3)

* Tue Nov 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> 3.0.0-1
- update to 3.0.0
- created links and provides to .1

* Fri Dec 18 2009 Ivana Hutarova Varekova <varekova@redhat.com> 2.4.2-1
- update to 2.4.2

* Fri Nov 13 2009 Ivana Varekova <varekova@redhat.com> 2.4.1-5
- fix 537328 - mpfr-devel should "Requires: gmp-devel"

* Wed Aug 12 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.4.1-4
- Use lzma compressed upstream tarball.

* Mon Aug 10 2009 Ivana Varekova <varekova redhat com> 2.4.1-3
- fix installation with --excludedocs option (#515958)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 11 2009 Ivana Varekova <varekova@redhat.com> - 2.4.1-1
- update to 2.4.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Ivana Varekova <varekova@redhat.com> - 2.4.0-1
- update to 2.4.0

* Wed Oct 15 2008 Ivana Varekova <varekova@redhat.com> - 2.3.2-1
- update to 2.3.2

* Mon Jul 21 2008 Ivana Varekova <varekova@redhat.com> - 2.3.1-1
- update to 2.3.1

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.0-3
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Ivana Varekova <varekova@redhat.com> 2.3.0-2
- rebuilt

* Thu Sep 20 2007 Ivana Varekova <varekova@redhat.com> 2.3.0-1
- update to 2.3.0
- fix license flag

* Mon Aug 20 2007 Ivana Varekova <varekova@redhat.com> 2.2.1-2
- spec file cleanup (#253440)

* Tue Jan 16 2007 Ivana Varekova <varekova@redhat.com> 2.2.1-1
- started

