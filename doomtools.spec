name:    doomtools
Version: 2026.06.28
Release: 7%{?dist}
Summary: Doom modding utility suite
License: MIT
URL:     https://mtrop.github.io/DoomTools/

Source0: https://github.com/MTrop/DoomTools/releases/download/2026.06.28-RELEASE/doomtools-bash-2026.06.28.184036227.tar.gz
Source1: doomtools-rpm-sources.tar.gz

BuildRequires: javapackages-filesystem
BuildRequires: bash-completion-devel
BuildRequires: ImageMagick
Requires: java

BuildArch: noarch

%description
DoomTools is a set of command-line utilities for building projects or for other things related to Doom Engine games.

# its just java and shell scripts
%global debug_package %{nil}

%prep
%setup -q -c -n doomtools
tar -xzf %{SOURCE1} -C .

%build
# no build needed

%install

# so that license only gets installed to licenses directory
mv docs/LICENSE.txt docs/licenses/LICENSE.txt

# java jar
install -Dm644 jar/*.jar %{buildroot}/%{_javadir}/doomtools/doomtools.jar

# shell wrappers
install -d %{buildroot}/%{_bindir}

SHELL_TEMPLATE="template.sh"

for f in *; do
    [ -f "$f" ] || continue
    mainclass=$(grep -E '^MAINCLASS=' "$f" | cut -d= -f2-)
    [ -n "$mainclass" ] || continue

    sed -e "s|@MAINCLASS@|$mainclass|g" "$SHELL_TEMPLATE" > %{buildroot}/%{_bindir}/"$f"
    chmod 755 %{buildroot}/%{_bindir}/"$f"
done

# desktop + icon
install -Dm644 doomtools.desktop %{buildroot}/%{_datadir}/applications/doomtools.desktop
sed -i -e "s|@BINDIR@|%{_bindir}|g" %{buildroot}/%{_datadir}/applications/doomtools.desktop
install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
magick docs/doomtools-logo.ico[0] %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/doomtools.png

# bash completions
install -m644 completion/bash/* %{buildroot}/%{bash_completions_dir}/

%files
%{_bindir}/*
%{_javadir}/doomtools/doomtools.jar
%{_datadir}/applications/doomtools.desktop
%{_datadir}/icons/hicolor/128x128/apps/doomtools.png
%{bash_completions_dir}/*
%license docs/licenses/LICENSE.txt
%doc docs/*.md docs/*.txt docs/changelogs

%changelog
* Fri Jul 06 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-7
- Add Bash completion script for 'doomfetch'

* Fri Jul 03 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-6
- Add Bash completion script for 'doomtools'

* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-5
- No changes

* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-4
- Make sure changelogs stay in a subdirectory of docs

* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-3
- Add a workaround for "--docs" not working with standard doc paths

* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-2
- Remove "GUI" from the name of all desktop actions

* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 2026.06.28-1
- Initial COPR package
