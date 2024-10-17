Name:		texlive-pagesel
Version:	56105
Release:	2
Summary:	Select pages of a document for output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pagesel
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagesel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagesel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagesel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Selects single pages, ranges of pages, odd pages or even pages
for output. The package is part of the oberdiek bundle.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pagesel
%{_texmfdistdir}/tex/latex/pagesel
%doc %{_texmfdistdir}/doc/latex/pagesel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
