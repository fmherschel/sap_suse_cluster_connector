#
# spec file for package sap_suse_cluster_connector
#
# Copyright (c) 2011-2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           sap_suse_cluster_connector
License:        GPL v2 only
Group:          Productivity/Clustering/HA
AutoReqProv:    on
Summary:        Connector between sapstartsrv and corosync/pacemeker based clusters
Version:        1.0.0
Release:        0.<RELEASE5>
#Release:      16
Source:         %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       pacemaker > 1.1.1

%description
Running SAP in a high availability cluster environment needs additional
interfaces to communicate between the SAP program SAPSTARTSRV and the
high availability cluster.

At least it is essential to inform the cluster, if a SAP instance is
started or shutdown.

This package includes the reference interface implementation
sap_suse_cluster_connector.

For more information you may also visit the SAP SCN at:
http://scn.sap.com/docs/DOC-25453



Authors:
--------
    Fabian Herschel

%prep
# WRONG %setup -c -T -a 0
# WRONG %setup -T -a 0
%setup  

%build
pwd
ls
( cd man8; for mp in *8; do gzip $mp; done )

%clean
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%install
#mkdir -p %{buildroot}/etc/cron.d
#mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man8

#
# "binaries"
#
cp -va bin/* %{buildroot}/usr/bin/
#
# etc
#
#
# share 
#
#
# man pages and license
#
cp -a man8/*.gz %{buildroot}/usr/share/man/man8/

%post
if [ ! -e /usr/local/bin/sap_cluster_connector ]; then
    ln -s /usr/bin/sap_suse_cluster_connector \
	/usr/local/bin/sap_cluster_connector
fi

%files
%defattr(-,root,root)
/usr/bin/sap_suse_cluster_connector
#/usr/bin/sap_ha_cluster_connector
#/usr/bin/sap_cluster_connector
%doc /usr/share/man/man8/*.gz
#%config(noreplace) /etc/ClusterTools2

%changelog
