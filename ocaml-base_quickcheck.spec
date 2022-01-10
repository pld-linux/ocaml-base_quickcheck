#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Randomized testing framework, designed for compatibility with Base
Summary(pl.UTF-8):	Szkielet testów losowych, zaprojektowany jako zgodny z Base
Name:		ocaml-base_quickcheck
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/base_quickcheck/tags
Source0:	https://github.com/janestreet/base_quickcheck/archive/v%{version}/base_quickcheck-%{version}.tar.gz
# Source0-md5:	d04738d4499e256b752bc40fcdb9730d
URL:		https://github.com/janestreet/base_quickcheck
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_base-devel >= 0.14
BuildRequires:	ocaml-ppx_base-devel < 0.15
BuildRequires:	ocaml-ppx_fields_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_fields_conv-devel < 0.15
BuildRequires:	ocaml-ppx_let-devel >= 0.14
BuildRequires:	ocaml-ppx_let-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_message-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_message-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_value-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_value-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.22.0
BuildRequires:	ocaml-splittable_random-devel >= 0.14
BuildRequires:	ocaml-splittable_random-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Base_quickcheck provides randomized testing in the style of Haskell's
Quickcheck library, with support for built-in types as well as types
provided by Base.

This package contains files needed to run bytecode executables using
base_quickcheck library.

%description -l pl.UTF-8
Base_quickcheck pozwala na testowanie z elementami losowości w stylu
biblioteki Quickcheck z Haskella, z obsługą typów wbudowanych, a także
typów dostarczanych przez Base.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki base_quickcheck.

%package devel
Summary:	Randomized testing framework, designed for compatibility with Base - development part
Summary(pl.UTF-8):	Szkielet testów losowych, zaprojektowany jako zgodny z Base - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_base-devel >= 0.14
Requires:	ocaml-ppx_fields_conv-devel >= 0.14
Requires:	ocaml-ppx_let-devel >= 0.14
Requires:	ocaml-ppx_sexp_message-devel >= 0.14
Requires:	ocaml-ppx_sexp_value-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.22.0
Requires:	ocaml-splittable_random-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
base_quickcheck library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki base_quickcheck.

%prep
%setup -q -n base_quickcheck-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/base_quickcheck/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/base_quickcheck/*/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/base_quickcheck/*/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/base_quickcheck

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/base_quickcheck
%{_libdir}/ocaml/base_quickcheck/META
%{_libdir}/ocaml/base_quickcheck/*.cma
%dir %{_libdir}/ocaml/base_quickcheck/ppx_quickcheck
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cma
%dir %{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/base_quickcheck/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/base_quickcheck/*.cmi
%{_libdir}/ocaml/base_quickcheck/*.cmt
%{_libdir}/ocaml/base_quickcheck/*.cmti
%{_libdir}/ocaml/base_quickcheck/*.mli
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cmi
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cmt
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cmti
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.mli
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cmi
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cmt
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cmti
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/base_quickcheck/base_quickcheck.a
%{_libdir}/ocaml/base_quickcheck/*.cmx
%{_libdir}/ocaml/base_quickcheck/*.cmxa
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/ppx_quickcheck.a
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cmx
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/*.cmxa
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/ppx_quickcheck_expander.a
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cmx
%{_libdir}/ocaml/base_quickcheck/ppx_quickcheck/expander/*.cmxa
%endif
%{_libdir}/ocaml/base_quickcheck/dune-package
%{_libdir}/ocaml/base_quickcheck/opam
%{_examplesdir}/%{name}-%{version}
