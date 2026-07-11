%global tl_name hyphen-greek
%global tl_revision 78069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5
Release:	%{tl_revision}.1
Summary:	Modern Greek hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/elhyphen
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-greek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-greek.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Modern Greek in monotonic and polytonic
spelling in LGR and UTF-8 encodings. Patterns in UTF-8 use two code
positions for each of the vowels with acute accent (a.k.a tonos, oxia),
e.g., U+03AC, U+1F71 for alpha.

