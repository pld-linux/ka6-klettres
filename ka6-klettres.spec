#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.02.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		klettres
Summary:	klettres
Name:		ka6-%{kaname}
Version:	24.02.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9a91523376367f1382b32986aac4e8a0
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KLettres aims to help to learn the alphabet and then to read some
syllables in different languages. It is meant to help learning the
very first sounds of a new language, for children or for adults.

%description -l pl.UTF-8
Celem KLettres jest pomoc w nauce alfabetu i czytania różnych
sylab w różnych językach. Program ma pomagać uczyć się pierwszych
dźwięków nowego języka, przeznaczony jest zarówno dla dzieci
jak i dorosłych.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/org.kde.klettres.desktop
%{_datadir}/config.kcfg/klettres.kcfg
%{_iconsdir}/hicolor/*x*/apps/klettres.png
%{_datadir}/klettres
%{_datadir}/metainfo/org.kde.klettres.appdata.xml
%{_datadir}/qlogging-categories6/klettres.categories
%{_datadir}/knsrcfiles/klettres.knsrc
