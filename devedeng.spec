Name:           devedeng
Version:        4.14.0
Release:        2%{?dist}
Summary:        A program to create video DVDs and CDs (VCD, sVCD or CVD)

License:        GPLv3+
URL:            http://www.rastersoft.com/programas/devede.html
Source0:        https://gitlab.com/rastersoft/devedeng/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Provides:       devede = %{version}-%{release}
Obsoletes:      devede < 4.0

BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
#Requires:       mplayer
#Requires:       mpv
Requires:       vlc
Requires:       ffmpeg
Requires:       dvdauthor
Requires:       vcdimager
Requires:       genisoimage
Requires:       brasero
#Requires:       k3b
Requires:       ImageMagick
Requires:       python3-urllib3 
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       dejavu-sans-fonts
Requires:       hicolor-icon-theme


%description
DevedeNG is a program to create video DVDs and CDs (VCD, sVCD or CVD), 
suitable for home players, from any number of video files, in any of the 
formats supported by FFMpeg.  

The suffix NG is because it is a rewrite from scratch of the old Devede, to 
work with Python3 and Gtk3, and with a new internal architecture that allows 
to expand it and easily add new features.


%prep
%autosetup -n %{name}-%{version}


%build
%py3_build

# Remove shebang from Python libraries
for lib in build/lib/devedeng/*.py; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done



%install
%py3_install 

# Fix desktop file 
desktop-file-install \
  --delete-original \
  --add-category X-OutputGeneration \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*.desktop

# Move icon into %%{_datadir}/icons/hicolor/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/pixmaps/%{name}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Add docs
install -m 644 HISTORY.md %{buildroot}%{_pkgdocdir}
install -m 644 README.md %{buildroot}%{_pkgdocdir}

%find_lang %{name}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%{_bindir}/devede_ng.py
%{_bindir}/copy_files_verbose.py
%{_datadir}/%{name}
%{python3_sitelib}/%{name}*.egg-info
%{python3_sitelib}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%exclude %{_mandir}/man1/devede.1*
%doc %{_docdir}/%{name}
%license COPYING


%changelog

* Wed Feb 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.14.0-2
- Updated to 4.14.0

* Tue Jan 29 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.13.0-2
- Updated to 4.13.0

* Fri Jul 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.12.0-2
- Rebuilt for Python 3.7

* Wed Jun 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.12.0-1
- Updated to 4.12.0
- Changed sources to gitlab

* Thu May 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 4.11.0-1
- Updated to 4.11.0

* Mon Apr 09 2018 David Vásquez <davidva AT tutanota DOT com> - 4.9.0-1
- Updated to 4.9.0

* Sun Jan 21 2018 David Vásquez <davidva AT tutanota DOT com> - 4.8.12-1
- Updated to 4.8.12

* Wed Dec 06 2017 David Vásquez <davidva AT tutanota DOT com> - 4.8.11-1
- Updated to 4.8.11

* Tue Nov 28 2017 David Vásquez <davidva AT tutanota DOT com> - 4.8.10-1
- Updated to 4.8.10

* Tue Sep 05 2017 David Vásquez <davidva AT tutanota DOT com> - 4.8.9-1
- Updated to 4.8.9

* Wed Feb 08 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.8-1
- Updated to new upstream release

* Thu Feb 02 2017 Andrea Musuruane <musuruan@gmail.com> 4.8.7-1
- Updated to new upstream release

* Sat Dec 17 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.6-1
- Updated to new upstream release

* Sat Nov 26 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.5-1
- Updated to new upstream release

* Sat Nov 05 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.4-1
- Updated to new upstream release

* Sat Oct 29 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.3-1
- Updated to new upstream release

* Sun Sep 25 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.2-1
- Updated to new upstream release

* Tue Sep 06 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.1-1
- Updated to new upstream release

* Sun Aug 14 2016 Andrea Musuruane <musuruan@gmail.com> 4.8.0-1
- Updated to new upstream release

* Thu Aug 04 2016 Andrea Musuruane <musuruan@gmail.com> 4.7.1-1
- Updated to new upstream release

* Mon Apr 25 2016 Andrea Musuruane <musuruan@gmail.com> 4.7.0-1
- Updated to new upstream release

* Thu Mar 17 2016 Andrea Musuruane <musuruan@gmail.com> 4.6.1-1
- First release 

