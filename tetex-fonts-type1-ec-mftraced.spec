Summary:	TeX EC fonts, PostScript Type1 format
Summary(pl):	Fonty TeXowe EC w formacie PostScript Type1
Name:		tetex-fonts-type1-ec-mftraced
Version:	1.0.12
Release:	1
License:	Public Domain
Group:		Applications/Publishing
Source0:	http://lilypond.org/download/fonts/ec-fonts-mftraced-%{version}.tar.gz
# Source0-md5:	4b355f668ca9cc01677e94c6eecdac40
BuildRequires:	mftrace
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts-jknappen
Requires(pre):	/usr/bin/updmap
Requires:	tetex
Obsoletes:	ec-fonts-mftraced
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are Type1 renderings of the EC variants of the standard CMR
family.

%description -l pl
Ten pakiet zawiera wyrenderowane do Type1 warianty EC standardowych
fontów z rodziny CMR.

%prep
%setup -q -n ec-fonts-mftraced-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2
updmap --enable Map ec-mftrace.map >/dev/null 2>&1

%postun
[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%{_datadir}/texmf/fonts/type1/public/ec-fonts-mftraced
%{_datadir}/texmf/fonts/tfm/public/ec-fonts-mftraced
%dir %{_datadir}/texmf/fonts/map
%dir %{_datadir}/texmf/fonts/map/dvips
%{_datadir}/texmf/fonts/map/dvips/ec-fonts-mftraced
