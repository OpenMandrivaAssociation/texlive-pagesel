%global tl_name pagesel
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Select pages of a document for output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pagesel
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagesel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagesel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pagesel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Selects single pages, ranges of pages, odd pages or even pages for
output.

