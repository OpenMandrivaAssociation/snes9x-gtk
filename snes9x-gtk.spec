Name:			snes9x-gtk
Version:		1.53
Release:		%mkrel 1

Summary:	Super NES emulator with a GTK frontend
Group:		Emulators
License:	LGPLv2+
#Licensed under both the GNU LGPL 2.1 and the "BSD-style" Snes9x license.
URL:		http://code.google.com/p/snes9x-gtk/
#changelog on the forum : http://www.snes9x.com/phpbb2/viewtopic.php?p=22874
Source0:	http://snes9x-gtk.googlecode.com/files/snes9x-%{version}-src.tar.bz2
Source1:	snes9x-gtk.png

%ifarch %ix86
BuildRequires:	nasm
%endif
BuildRequires:	zlib1-devel
BuildRequires:	libpng-devel
BuildRequires:	XFree86-devel
BuildRequires:	gtk2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	portaudio-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	alsa-lib-devel
#BuildRequires:	gtkglext-devel
BuildRequires:	SDL1.2-devel
BuildRequires:	intltool
BuildRequires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}

#Provides: snes9x-binary

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
rm -rf %{buildroot}
cd gtk
#makeinstall_std DESTDIR=%{buildroot}/%{_prefix}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 data/snes9x.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d -m 755 %{buildroot}%{_datadir}/applications
#install -m 644 gtk/snes9x.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
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
%defattr(-,root,root)
%doc docs/* gtk/doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

