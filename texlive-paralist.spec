Name:		texlive-paralist
Version:	43021
Release:	1
Summary:	Enumerate and itemize within paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/paralist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
