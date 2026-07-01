name:    doomtools
Version: 2026.06.28
Release: 2%{?dist}
Summary: Doom modding utility suite
License: MIT
URL:     https://mtrop.github.io/DoomTools/

Source0: https://github.com/MTrop/DoomTools/releases/download/2026.06.28-RELEASE/doomtools-bash-2026.06.28.184036227.tar.gz
Source1: doomtools.desktop
Source2: template.sh

BuildRequires: javapackages-filesystem
BuildRequires: ImageMagick
Requires: java

BuildArch: noarch

%description
DoomTools is a set of command-line utilities for building projects or for other things related to Doom Engine games.

# its just java and shell scripts
%global debug_package %{nil}

%prep
%setup -q -c -n doomtools

%install

# so that license only gets installed to licenses directory
mv docs/LICENSE.txt docs/licenses/LICENSE.txt

# java jar
install -Dm644 jar/*.jar %{buildroot}/%{_javadir}/doomtools/doomtools.jar

# shell wrappers
install -d %{buildroot}/%{_bindir}

SHELL_TEMPLATE="%{SOURCE2}"

for f in *; do
    [ -f "$f" ] || continue
    mainclass=$(grep -E '^MAINCLASS=' "$f" | cut -d= -f2-)
    [ -n "$mainclass" ] || continue

    sed -e "s|@MAINCLASS@|$mainclass|g" "$SHELL_TEMPLATE" > %{buildroot}/%{_bindir}/"$f"
    chmod 755 %{buildroot}/%{_bindir}/"$f"
done

# desktop + icon
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/doomtools.desktop
install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
magick docs/doomtools-logo.ico[0] %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/doomtools.png

%files
%{_bindir}/*
%{_javadir}/doomtools/doomtools.jar
%{_datadir}/applications/doomtools.desktop
%{_datadir}/icons/hicolor/128x128/apps/doomtools.png
%license docs/licenses/LICENSE.txt
%doc docs/*.md docs/*.txt docs/changelogs/*

%changelog
* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-2
- Remove "GUI" from the name of all desktop actions

* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-1
- Initial COPR package
