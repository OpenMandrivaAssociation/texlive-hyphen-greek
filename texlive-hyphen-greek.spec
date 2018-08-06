# revision 29725
# category TLCore
# catalog-ctan /language/hyphenation/elhyphen
# catalog-date 2012-05-25 14:41:32 +0200
# catalog-license other-free
# catalog-version 5
Name:		texlive-hyphen-greek
Version:	5
Release:	2
Summary:	Modern Greek hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/elhyphen
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-greek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-greek.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Modern Greek in monotonic and
polytonic spelling in LGR and UTF-8 encodings.  Patterns in
UTF-8 use two code positions for each of the vowels with acute
accent (a.k.a tonos, oxia), e.g., U+03AC, U+1F71 for alpha.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%{_texmfdistdir}/tex/generic/hyphen/grmhyph5.tex
%{_texmfdistdir}/tex/generic/hyphen/grphyph5.tex
%_texmf_language_dat_d/hyphen-greek
%_texmf_language_def_d/hyphen-greek
%_texmf_language_lua_d/hyphen-greek
%doc %{_texmfdistdir}/doc/generic/elhyphen/README
%doc %{_texmfdistdir}/doc/generic/elhyphen/anc-test.ltx
%doc %{_texmfdistdir}/doc/generic/elhyphen/anc-test.pdf
%doc %{_texmfdistdir}/doc/generic/elhyphen/ancient.pdf
%doc %{_texmfdistdir}/doc/generic/elhyphen/compound.ltx
%doc %{_texmfdistdir}/doc/generic/elhyphen/compound.pdf
%doc %{_texmfdistdir}/doc/generic/elhyphen/copyrite.txt
%doc %{_texmfdistdir}/doc/generic/elhyphen/modern.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-greek <<EOF
\%% from hyphen-greek:
monogreek loadhyph-el-monoton.tex
greek loadhyph-el-polyton.tex
=polygreek
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-greek
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-greek <<EOF
\%% from hyphen-greek:
\addlanguage{monogreek}{loadhyph-el-monoton.tex}{}{1}{1}
\addlanguage{greek}{loadhyph-el-polyton.tex}{}{1}{1}
\addlanguage{polygreek}{loadhyph-el-polyton.tex}{}{1}{1}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-greek
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-greek <<EOF
-- from hyphen-greek:
	['monogreek'] = {
		loader = 'loadhyph-el-monoton.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-el-monoton.pat.txt',
		hyphenation = '',
	},
	['greek'] = {
		loader = 'loadhyph-el-polyton.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = { 'polygreek' },
		patterns = 'hyph-el-polyton.pat.txt',
		hyphenation = '',
	},
EOF
