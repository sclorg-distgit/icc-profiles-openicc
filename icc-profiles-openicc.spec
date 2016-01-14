%global pkg_name icc-profiles-openicc
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.3.1
Release:        5.8%{?dist}
Summary:        The OpenICC profiles

License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/OpenICC-Profiles/%{pkg_name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  %{?scl_prefix}color-filesystem
Requires:       %{?scl_prefix}color-filesystem


%description
The OpenICC profiles are provided to serve color managed
applications and services.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%configure --enable-verbose
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/{icons,pixmaps,mime}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%doc default_profiles/base/LICENSE-ZLIB
%doc default_profiles/base/LICENSE-ZLIB-LSTAR
%dir %{_icccolordir}/OpenICC
%{_icccolordir}/OpenICC/compatibleWithAdobeRGB1998.icc
%{_icccolordir}/OpenICC/sRGB.icc
%{_icccolordir}/OpenICC/ProPhoto-RGB.icc
%dir %{_icccolordir}/Oyranos
%{_icccolordir}/Oyranos/Gray-CIE_L.icc
%{_icccolordir}/Oyranos/Gray_linear.icc
%{_icccolordir}/Oyranos/ITULab.icc
%dir %{_icccolordir}/basICColor
%{_icccolordir}/basICColor/LStar-RGB.icc
%dir %{_icccolordir}/lcms
%{_icccolordir}/lcms/LCMSLABI.ICM
%{_icccolordir}/lcms/LCMSXYZI.ICM
%{_icccolordir}/lcms/Lab.icc
%{_icccolordir}/lcms/XYZ.icc
%dir %{_colordir}/target
%dir %{_colordir}/target/NPES
%{_colordir}/target/NPES/TR002.ti3
%{_colordir}/target/NPES/TR003.ti3
%{_colordir}/target/NPES/TR005.ti3
%{_colordir}/target/NPES/TR006.ti3
%dir %{_colordir}/target/fogra
%{_colordir}/target/fogra/FOGRA28L.ti3
%{_colordir}/target/fogra/FOGRA29L.ti3
%{_colordir}/target/fogra/FOGRA30L.ti3
%{_colordir}/target/fogra/FOGRA39L.ti3
%{_colordir}/target/fogra/FOGRA40L.ti3


%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.3.1-5.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.3.1-5.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5.5
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5.4
- Skip installation of icons, pixmaps and MIME data

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5.3
- Mass rebuild 2014-02-18

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3.1-5
- Mass rebuild 2013-12-27

* Thu Jul 25 2013 Michal Srb <msrb@redhat.com> - 1.3.1-4
- Fix license tag

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jan 21 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1.1
- Drop wrong obsoletes

* Sat Aug 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Rename to icc-profiles-openicc
- Add scriptlet for icons directory
- Use absolute path for update-mime-database
- Drop README
- Add directory ownership

* Thu Jul 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Tue Jan 25 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jan 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.1-1
- Spec file rewrite

* Mon Dec 27 2010 - Kai-Uwe Behrmann <ku.b at gmx.de>
- split out a directory package from the mime types

* Fri Aug 28 2010 - Kai-Uwe Behrmann <ku.b at gmx.de>
- new package naming scheme for Oyranos independent installations
