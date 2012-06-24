Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(es):	Cliente en l�nea de comando para bajar archivos WWW/FTP con recursi�n opcional
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP
Summary(pt_BR):	Cliente na linha de comando para baixar arquivos WWW/FTP com recurs�o opcional
Summary(ru):	������� ��� ��������� ������ �� ���������� HTTP � FTP
Summary(uk):	���̦�� ��� ��������� ���̦� �� ���������� HTTP �� FTP
Summary(zh_CN):	[ͨѶ]����ǿ������س���,֧�ֶϵ�����
Name:		wget
Version:	1.8.2
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.gnu.org/pub/gnu/wget/%{name}-%{version}.tar.gz
# Source0-md5:	a2473d7a53ebaf0a1bdb06f17059e8f1
Source2:	%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	bad85be11d26aeab8158cdfcf7e7483e
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac.patch
# based on http://www14.u-page.so-net.ne.jp/db3/h-yamamo/ipv6/patches/%{name}-1.8.1-v6-20219.patch.gz
Patch2:		%{name}-ipv6.patch
Patch3:		%{name}-ht.patch
Patch4:		%{name}-filename.patch
Patch5:		%{name}-terminate_filename.patch
URL:		http://sunsite.dk/wget/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel < 0.11
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	texinfo
BuildRequires:	perl-devel
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%description -l es
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

%description -l fr
GNU Wget est un utilitaire pour r�cup�rer des fichiers qui peut
utiliser indiff�remment les protocoles HTTP ou FTP. Parmi les
caract�ristiques de Wget, citons la capacit� � r�cup�rer des fichiers
en arri�re-plan alors que vous n'�tes pas connect�, la r�cup�ration
r�cursive de r�pertoires, la capacit� de r�cup�rer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
r�cup�rer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particuli�rement configurable.

%description -l ja
GNU wget �� HTTP �� FTP �ץ�ȥ���Τɤ��餫����Ѥ��뤳�Ȥ��Ǥ���
�ե�������������桼�ƥ���ƥ��Ǥ���wget �ϥ������Ȥ��Ƥ���
�֤˥Хå����饦��ɤ�Ư����ħ���äƤ��뤳�ȡ��ǥ��쥯�ȥ�κƵ�Ū
�������ե�����͡���Υ磻��ɥ����ɥޥå��󥰡��ե�����Υ����ॹ����פ�
��¸����ӡ��٤��԰������³�� FTP �����Ф� Rest �� HTTP �����Ф�
Range �λ��ѡ��ץ����������ФΥ��ݡ��Ȥ�������ưפ���ޤ����ħ��
��äƤ��ޤ���

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do �ci�gania zasob�w
wsadowo. Umo�liwia �ci�ganie zasob�w z podkatalogami, a tak�e ma opcje
umo�liwiaj�ce wykonanie lokalnej kopii zasob�w (mirror). W razie
niemo�no�ci dostania si� do zasob�w lub gdy po��czenie z serwerem
FTP/HTTP zostanie zerwane, mo�e automatycznie ponawia� pr�by
kopiowania. Jest tak�e dobrze przystosowany do tego, �eby uruchamia�
go jako zadanie z crona.

%description -l pt_BR
O GNU wget � uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo n�o interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conex�es lentas ou inst�veis,
baixando o arquivo at� que ele seja completamente recebido.

%description -l ru
GNU Wget - ��� ������� ��������� ������ ��� ��������� ������ ��
���������� FTP � HTTP. ����� ������������ Wget - ������ � �������
������ ����� �� �������� �� �������, ����������� ���������� ���������,
����� ������ �� �������, ��������� ������� ��������� � ���������
������, ���������� ������� ��������� ������ ��� ��������,
������������� REST � FTP ��������� � Range � HTTP ��������� ���
�������� ������ �� ��������� ��� ������������ �������, ��������� Proxy
��������, �����������������.

%description -l uk
GNU Wget - �� ���̦�� ���������� ����� ��� ��������� ���̦� ��
���������� FTP �� HTTP. ����� ����������� Wget - ������ � ��������
����ͦ ���� �� �������� �� �������, ���������� ��������� ������Ǧ�,
��¦� ���̦� �� �������, ��Ҧ������ ���� צ�������� �� ���������
���̦�, ���������� ���� צ�������� ���̦� ��� ����������Φ,
������������ REST � FTP ��������� �� Range � HTTP ��������� ���
������������ ���̦� �� ��צ����� �� �����¦����� �������, Ц�������
Proxy �����Ҧ�, ���������Φ���.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--with-ssl \
	--enable-ipv6
%{__make}
tail -6 util/README >rmold.README

cd doc
makeinfo --force %{name}.texi; touch *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

echo "y" | \
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

install util/rmold.pl		$RPM_BUILD_ROOT%{_bindir}/rmold
install doc/sample.wgetrc	$RPM_BUILD_ROOT%{_sysconfdir}/wgetrc

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*.info*
