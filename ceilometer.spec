#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ceilometer
Version  : 6.0.0
Release  : 38
URL      : http://tarballs.openstack.org/ceilometer/ceilometer-6.0.0.tar.gz
Source0  : http://tarballs.openstack.org/ceilometer/ceilometer-6.0.0.tar.gz
Source1  : ceilometer-agent-central.service
Source2  : ceilometer-agent-compute.service
Source3  : ceilometer-agent-notification.service
Source4  : ceilometer-alarm-evaluator.service
Source5  : ceilometer-alarm-notifier.service
Source6  : ceilometer-api.service
Source7  : ceilometer-collector.service
Source8  : ceilometer.tmpfiles
Summary  : OpenStack Telemetry
Group    : Development/Tools
License  : Apache-2.0
Requires: ceilometer-bin
Requires: ceilometer-python3
Requires: ceilometer-config
Requires: ceilometer-data
Requires: ceilometer-license
Requires: ceilometer-python
Requires: PasteDeploy
Requires: PyYAML
Requires: SQLAlchemy
Requires: WSME
Requires: WebOb
Requires: Werkzeug
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: lxml
Requires: msgpack-python
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.reports
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: pecan
Requires: pysnmp
Requires: python-ceilometerclient
Requires: python-dateutil
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: python-swiftclient
Requires: requests
Requires: retrying
Requires: six
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: tooz
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-Ceilometer-sudoers-entry.patch
Patch2: 0002-Added-default-configuration-file.patch
Patch3: 0003-Enable-systemd-notification.patch
Patch4: 0004-Move-rootwrap-location.patch
Patch5: 0005-Add-support-to-httdp-and-nginx.patch

%description
==========

%package bin
Summary: bin components for the ceilometer package.
Group: Binaries
Requires: ceilometer-data
Requires: ceilometer-config
Requires: ceilometer-license

%description bin
bin components for the ceilometer package.


%package config
Summary: config components for the ceilometer package.
Group: Default

%description config
config components for the ceilometer package.


%package data
Summary: data components for the ceilometer package.
Group: Data

%description data
data components for the ceilometer package.


%package license
Summary: license components for the ceilometer package.
Group: Default

%description license
license components for the ceilometer package.


%package python
Summary: python components for the ceilometer package.
Group: Default
Requires: ceilometer-python3

%description python
python components for the ceilometer package.


%package python3
Summary: python3 components for the ceilometer package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ceilometer package.


%prep
%setup -q -n ceilometer-6.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532217014
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ceilometer
cp LICENSE %{buildroot}/usr/share/doc/ceilometer/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/ceilometer-agent-central.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/ceilometer-agent-compute.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/ceilometer-agent-notification.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/ceilometer-alarm-evaluator.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/ceilometer-alarm-notifier.service
install -m 0644 %{SOURCE6} %{buildroot}/usr/lib/systemd/system/ceilometer-api.service
install -m 0644 %{SOURCE7} %{buildroot}/usr/lib/systemd/system/ceilometer-collector.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE8} %{buildroot}/usr/lib/tmpfiles.d/ceilometer.conf
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/ceilometer
install -p -D -m 644 etc/ceilometer/*.ini %{buildroot}/usr/share/defaults/ceilometer
install -p -D -m 644 etc/ceilometer/*.yaml %{buildroot}/usr/share/defaults/ceilometer
install -p -D -m 644 etc/ceilometer/*.json %{buildroot}/usr/share/defaults/ceilometer
install -p -D -m 644 etc/ceilometer/*.conf %{buildroot}/usr/share/defaults/ceilometer
install -d -m 755 %{buildroot}/usr/share/ceilometer/rootwrap.d
mv %{buildroot}/usr/share/defaults/ceilometer/rootwrap.conf %{buildroot}/usr/share/ceilometer/
install -p -D -m 640 etc/ceilometer/rootwrap.d/*.filters %{buildroot}/usr/share/ceilometer/rootwrap.d/
install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -p -D -m 440 etc/sudoers.d/ceilometer.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/ceilometer
install -m 0755 -d %{buildroot}/usr/share/httpd/cgi-bin/ceilometer
cp ceilometer/api/app.wsgi %{buildroot}/usr/share/httpd/cgi-bin/ceilometer
install -m 0755 -d %{buildroot}/usr/share/defaults/httpd/conf.d
install -p -D -m 644 ceilometer-api.httpd %{buildroot}/usr/share/defaults/httpd/conf.d/ceilometer-api.template
install -m 0755 -d %{buildroot}/usr/share/uwsgi/ceilometer
install -p -D -m 644 api.ini %{buildroot}/usr/share/uwsgi/ceilometer
install -m 0755 -d %{buildroot}/usr/share/nginx/conf.d
install -p -D -m 644 ceilometer-api.nginx %{buildroot}/usr/share/nginx/conf.d/ceilometer-api.template
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ceilometer-agent-notification
/usr/bin/ceilometer-api
/usr/bin/ceilometer-collector
/usr/bin/ceilometer-dbsync
/usr/bin/ceilometer-expirer
/usr/bin/ceilometer-polling
/usr/bin/ceilometer-rootwrap
/usr/bin/ceilometer-send-sample

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ceilometer-agent-central.service
/usr/lib/systemd/system/ceilometer-agent-compute.service
/usr/lib/systemd/system/ceilometer-agent-notification.service
/usr/lib/systemd/system/ceilometer-alarm-evaluator.service
/usr/lib/systemd/system/ceilometer-alarm-notifier.service
/usr/lib/systemd/system/ceilometer-api.service
/usr/lib/systemd/system/ceilometer-collector.service
/usr/lib/tmpfiles.d/ceilometer.conf

%files data
%defattr(-,root,root,-)
/usr/share/ceilometer/rootwrap.conf
/usr/share/ceilometer/rootwrap.d/ipmi.filters
/usr/share/defaults/ceilometer/api_paste.ini
/usr/share/defaults/ceilometer/ceilometer-config-generator.conf
/usr/share/defaults/ceilometer/ceilometer.conf
/usr/share/defaults/ceilometer/event_definitions.yaml
/usr/share/defaults/ceilometer/event_pipeline.yaml
/usr/share/defaults/ceilometer/gnocchi_resources.yaml
/usr/share/defaults/ceilometer/pipeline.yaml
/usr/share/defaults/ceilometer/policy.json
/usr/share/defaults/httpd/conf.d/ceilometer-api.template
/usr/share/defaults/sudo/sudoers.d/ceilometer
/usr/share/httpd/cgi-bin/ceilometer/app.wsgi
/usr/share/nginx/conf.d/ceilometer-api.template
/usr/share/uwsgi/ceilometer/api.ini

%files license
%defattr(-,root,root,-)
/usr/share/doc/ceilometer/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
