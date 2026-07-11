%global tl_name schola-otf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Using the OpenType fonts TeX Gyre schola
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/schola-otf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schola-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schola-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can only be used with LuaLaTeX or XeLaTeX. It does the font
setting for the OpenType font TeX Gyre Schola for text and math. The
missing typefaces like bold math and slanted text are also defined

