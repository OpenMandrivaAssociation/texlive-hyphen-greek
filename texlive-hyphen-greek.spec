%global tl_name hyphen-greek
%global tl_revision 78069
%global tl_version 5

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Modern Greek in monotonic and polytonic
spelling in LGR and UTF-8 encodings. Patterns in UTF-8 use two code
positions for each of the vowels with acute accent (a.k.a tonos, oxia),
e.g., U+03AC, U+1F71 for alpha.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-greek:
greek loadhyph-el-polyton.tex
=polygreek
monogreek loadhyph-el-monoton.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-greek:
\addlanguage{greek}{loadhyph-el-polyton.tex}{}{1}{1}
\addlanguage{polygreek}{loadhyph-el-polyton.tex}{}{1}{1}
\addlanguage{monogreek}{loadhyph-el-monoton.tex}{}{1}{1}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-greek:
['greek'] = {
	loader = 'loadhyph-el-polyton.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = { 'polygreek' },
	patterns = 'hyph-el-polyton.pat.txt',
},
['monogreek'] = {
	loader = 'loadhyph-el-monoton.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-el-monoton.pat.txt',
},
TL_HYPHEN_EOF
