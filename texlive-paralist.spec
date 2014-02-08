# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/paralist
# catalog-date 2009-10-07 21:35:42 +0200
# catalog-license lppl
# catalog-version 2.3b
Name:		texlive-paralist
Version:	2.3b
Release:	3
Summary:	Enumerate and itemize within paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paralist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides enumerate and itemize environments that can be used
within paragraphs to format the items either as running text or
as separate paragraphs with a preceding number or symbol. Also
provides compacted versions of enumerate and itemize.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3b-2
+ Revision: 754642
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3b-1
+ Revision: 719190
- texlive-paralist
- texlive-paralist
- texlive-paralist
- texlive-paralist

