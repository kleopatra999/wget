Summary:	Command-line HTTP and FTP client
Summary(pl):	Wsadowy klient HTTP/FTP 
Name:		wget
Version:	1.5.3
Release:	7
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		wget-man.patch
Patch1:		wget-pl.po.patch
Patch2:		wget-info.patch
BuildPrereq:	autoconf >= 2.13-8
Prereq:		/sbin/install-info
URL:		http://sunsite.auc.dk/ftp/pub/infosystems/wget/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
wget is a command-line program to fetch files via HTTP or FTP.  It
supports recursive retrieval and mirroring options, and it automatically
retries several times before giving up, so it is well-suited to running
from cron jobs.

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do �ci�gania zasob�w wsadowo. 
Umo�liwia �ci�ganie zasob�w z podkatalogami, a tak�e ma opcje umo�liwiaj�ce 
wykonanie lokalnej kopii zasob�w (mirror). W razie niemo�no�ci dostania si� 
do zasob�w lub gdy po��czenie z serwerem FTP/HTTP zostanie zerwane, mo�e 
automatycznie ponawia� pr�by kopiowania. Jest tak�e dobrze przystosowany do 
tego, �eby uruchamia� go jako zadanie z cron'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr \
	--sysconfdir=/etc
make
tail -6 util/README >rmold.README

(cd doc; makeinfo --force wget.texi; touch *)

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc install
install -c util/rmold.pl $RPM_BUILD_ROOT/usr/bin/rmold

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/wget.info*,man/man1/*} \
    AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/wget.info.gz /etc/info-dir

%postun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/wget.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,MAILING-LIST,NEWS,TODO,README,rmold.README}.gz

%attr(755,root,root) /usr/bin/*

%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/wget.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/wget.mo
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/wget.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/wget.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/wget.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/wget.mo
%lang(pt) %{_datadir}/locale/pt*/LC_MESSAGES/wget.mo

%{_mandir}/man1/*
%{_infodir}/wget.info*

%verify(not md5 size mtime) %config(noreplace) /etc/wgetrc

%changelog
* Thu May 13 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.5.3-7]
- package is now FHS 2.0 compliant.

* Wed Apr 21 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.5.3-6]
- replacements in %files,
- recompiled on rpm 3,
- force making info pages (new makeinfo don't accept @xfer{} without "." or
  "," after this markup) by Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>.

* Fri Apr  2 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.5.2-5]
- removed man group from man pages,
- few typos corrected,
- cosmetic changes for common l&f.

* Thu Feb 10 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [1.5.2-4]
- added Group(pl)
- added gzipping documentation

* Mon Dec 27 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-3]
- standarized {un}registering info pages (added wget-info.patch),
- added URL,
- added gzipping man pages.

* Tue Sep 12 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.5.2-2]
- fixed pl translation.

* Mon Sep  7 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-2]
- added wget-pl.po.patch patch with polish translation 
  (Adam Kozubowicz <tapir@interdata.com.pl>,
- added wget-man.patch patch with wget man page.

* Sat Aug  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-1]
- added pl translation.

* Sun May 17 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.1-2]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot and Source,
- added %verify(not md5 size mtime) and noreplace parameter for %config,
- removed COPYING from %doc (copyright statment is in Copyright
  field),
- added %postun, %post sections with {de}instaling wget info pages,
- spec file rewrited for using Buildroot,
- added %clean section,
- added URL,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- Buildroot changed to /tmp/wget-%%{PACKAGE_VERSION}-root,
- added %%{PACKAGE_VERSION} to Source url,
- replaced "mkdir -p" with "install -d" in %install,
- base datadir changed to %{_datadir},
- added %lang macros for %{_datadir}/locale/*/LC_MESSAGES/wget.mo files,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Thu May  7 1998 ??? <root@ricketts.stannes.ox.ac.uk>
  [1.5.1-1]
- previous release in rpm package.
