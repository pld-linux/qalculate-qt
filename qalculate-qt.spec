Summary:	Modern desktop calculator
Summary(pl.UTF-8):	Nowoczesny kalkulator
Name:		qalculate-qt
Version:	5.9.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	https://github.com/Qalculate/qalculate-qt/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	87d36c8f865c56fb1152f61863bcd661
URL:		https://qalculate.github.io/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	libqalculate-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	qt6-build
BuildRequires:	rpmbuild(macros) >= 2.000
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	libqalculate >= %{version}
Suggests:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qalculate is a modern multi-purpose desktop calculator. It is small
and simple to use but with much power. Features include arbitrary
precision, plotting, and a graphical interface (QT).

%description -l pl.UTF-8
Qalculate jest nowoczesnym, wielozadaniowym kalkulatorem. Jest mały i
prosty w użyciu, lecz posiada duże możliwości. Podstawowymi cechami
programu są nieograniczona precyzja, możliwość rysowania wykresów i
graficzny interfejs (QT).

%prep
%setup -q

%build
%qmake_qt6 PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/qalculate-qt
%dir %{_datadir}/qalculate-qt
%dir %{_datadir}/qalculate-qt/translations
%{_desktopdir}/io.github.Qalculate.qalculate-qt.desktop
%{_mandir}/man1/qalculate-qt.1.*
%{_iconsdir}/hicolor/*x*/apps/qalculate-qt.png
%{_iconsdir}/hicolor/scalable/apps/qalculate-qt.svg
%{_datadir}/metainfo/io.github.Qalculate.qalculate-qt.metainfo.xml
