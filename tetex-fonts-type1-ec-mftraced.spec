Summary:	TeX EC fonts, PostScript Type1 format
Summary(pl):	Fonty TeXowe EC w formacie PostScript Type1
Name:		tetex-fonts-type1-ec-mftraced
Version:	1.0.8
Release:	1
License:	Public Domain
Group:		Applications/Publishing
Source0:	http://lilypond.org/download/fonts/ec-fonts-mftraced-%{version}.tar.gz
# Source0-md5:	f595a80eb1d0d7dfeff23939a082f4e5
BuildRequires:	mftrace
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts-jknappen
Requires:	tetex
Obsoletes:	ec-fonts-mftraced
Requires(post,postun):	%{_bindir}/texhash
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

%post
%{_bindir}/texhash >&2

%postun
%{_bindir}/texhash >&2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%{_datadir}/texmf/fonts/type1/public/ec-fonts-mftraced
%{_datadir}/texmf/fonts/tfm/public/ec-fonts-mftraced
%{_datadir}/texmf/dvips/ec-fonts-mftraced
