Name:		snes9x-gtk
Version:	1.53
Release:	3

Summary:	Super NES emulator with a GTK frontend
Group:		Emulators
License:	LGPLv2+
#Licensed under both the GNU LGPL 2.1 and the "BSD-style" Snes9x license.
URL:		http://code.google.com/p/snes9x-gtk/
#changelog on the forum : http://www.snes9x.com/phpbb2/viewtopic.php?p=22874
Source0:	http://snes9x-gtk.googlecode.com/files/snes9x-%{version}-src.tar.bz2
Source1:	snes9x-gtk.png

%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	intltool
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(zlib)

%description
Snes9X GTK is a Super Nintendo Entertainment System (SNES) emulator.

It basically allows you to play most games designed for the SNES
and Super Famicom Nintendo game systems on your PC or Workstation.

%prep
%setup -q -n snes9x-%{version}-src
cd gtk
./autogen.sh
%configure --with-netplay

%build
%make -C gtk

%install
cd gtk
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 data/snes9x.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -d -m 755 %{buildroot}%{_datadir}/applications
cat<<EOF>%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Snes9x GTK
Comment=Super NES Emulator
Type=Application
Categories=Game;Emulator;X-MandrivaLinux-MoreApplications-Emulators;
MimeType=application/x-snes-rom;
FilePattern=smc;fig;sfc;SMC;FIG;SFC;
Exec=snes9x-gtk %F
TryExec=snes9x-gtk
Icon=snes9x-gtk
EOF

%files 
%doc docs/* gtk/doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jul 29 2011 Andrey Bondrov <abondrov@mandriva.org> 1.53-1mdv2012.0
+ Revision: 692217
- Fix BuildRequires
- imported package snes9x-gtk


* Wed Jul 20 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.53-1mdv2011.0
- New version 1.53

* Sat Feb 20 2010 Guillaume Bedot <littletux@zarb.org> 1.52-1plf2010.1
- New release "1.52.79"
- Dropped now useless patch
- Special thanks to Zombie for waking me up (+ fix changelog for .74)

* Sun Oct 11 2009 Guillaume Bedot <littletux@zarb.org> 1.51.78-1plf2010.0
- New release "1.51.78"

* Sun Sep  6 2009 Guillaume Bedot <littletux@zarb.org> 1.51.76-1plf2010.0
- New release "1.51.76"
- fixes exec stack, adds more doc, doc encoding

* Fri Sep  4 2009 Guillaume Bedot <littletux@zarb.org> 1.51.75-1plf2010.0
- New release "1.51.75"

* Fri Aug 14 2009 Zombie Ryushu <ryushu@zarb.org> 1.51.74-1plf2010.0
- New release "1.51.74"

* Mon Jun  1 2009 Guillaume Bedot <littletux@zarb.org> 1.51.73-1plf2010.0
- New release "1.51.73"

* Mon May 18 2009 Guillaume Bedot <littletux@zarb.org> 1.51.71-1plf2010.0
- New release "1.51.71"

* Sat Apr 18 2009 Guillaume Bedot <littletux@zarb.org> 1.51.70-1plf2009.1
- New release "1.51.70"
- Dropped outdated patches

* Fri Jan 30 2009 Guillaume Bedot <littletux@zarb.org> 1.51.62-1plf2009.1
- New release "1.51.62"

* Tue Jan  6 2009 Guillaume Bedot <littletux@zarb.org> 1.51.61-1plf2009.1
- New release "1.51.61"

* Mon Nov 10 2008 Guillaume Bedot <littletux@zarb.org> 1.51.56-1plf2009.1
- New release "1.51.56"

* Tue Oct 21 2008 Guillaume Bedot <littletux@zarb.org> 1.51.54-1plf2009.1
- New release "1.51.54"

* Fri Aug 15 2008 Guillaume Bedot <littletux@zarb.org> 1.51.52-1plf2009.0
- New release "1.51.52"

* Sat Jul 12 2008 Guillaume Bedot <littletux@zarb.org> 1.51.42-1plf2009.0
- New release "1.51.42"
- fixed buildrequires, buildroot

* Thu Jun 26 2008 Guillaume Bedot <littletux@zarb.org> 1.51.37-1plf2009.0
- New release "1.51.37"

* Thu May 29 2008 Guillaume Bedot <littletux@zarb.org> 1.51.29-1plf2009.0
- First package of snes9x-gtk for PLF
