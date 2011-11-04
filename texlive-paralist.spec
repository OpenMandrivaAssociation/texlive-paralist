# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/paralist
# catalog-date 2009-10-07 21:35:42 +0200
# catalog-license lppl
# catalog-version 2.3b
Name:		texlive-paralist
Version:	2.3b
Release:	1
Summary:	Enumerate and itemize within paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paralist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides enumerate and itemize environments that can be used
within paragraphs to format the items either as running text or
as separate paragraphs with a preceding number or symbol. Also
provides compacted versions of enumerate and itemize.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/paralist/paralist.sty
%doc %{_texmfdistdir}/doc/latex/paralist/README
%doc %{_texmfdistdir}/doc/latex/paralist/paralist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/paralist/paralist.drv
%doc %{_texmfdistdir}/source/latex/paralist/paralist.dtx
%doc %{_texmfdistdir}/source/latex/paralist/paralist.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
