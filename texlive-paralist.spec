%global tl_name paralist
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	Enumerate and itemize within paragraphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/paralist
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paralist.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides enumerate and itemize environments that can be used within
paragraphs to format the items either as running text or as separate
paragraphs with a preceding number or symbol. Also provides compacted
versions of enumerate and itemize.

