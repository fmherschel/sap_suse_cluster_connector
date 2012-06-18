#
# spec file for package sap_suse_cluster_connector
#
# Copyright (c) 2011-2012 SUSE LINUX Products GmbH, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Author: Fabian Herschel
#
# GPL
#
# please send bugfixes or comments to feedback@suse.de.
#
Name:         sap_suse_cluster_connector
License:      GPL
Group:        Productivity/Clustering/HA
Autoreqprov:  on
Summary:      Connector between sapstartsrv and corosync/pacemeker based clusters
Version:      0.1.1
Release:      12.1
#Release:      16
Source:       %{name}-%{version}.tgz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Vendor:	      SUSE Linux Products GmbH
Requires:     pacemaker > 1.1.1
	
%description
Running SAP in a high availability cluster environment needs additional 
interfaces to communicate between the SAP program SAPSTARTSRV and the high 
availability cluster. 

At least it is essential to inform the cluster, if a SAP instance is started 
or shutdown. 

This package includes the reference interface implementation 
sap_suse_cluster_connector.

For more information you may also visit the SAP SCN at:
http://scn.sap.com/docs/DOC-25453

%prep
# WRONG %setup -c -T -a 0
# WRONG %setup -T -a 0
%setup  
pwd
ls
sleep 10

%build
pwd
ls
( cd man8; for mp in *8; do gzip $mp; done )
( cd bin; 
  ln -s sap_suse_cluster_connector sap_ha_cluster_connector 
  ln -s sap_suse_cluster_connector sap_cluster_connector 
)

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

#%post

%files
%defattr(-,root,root)
/usr/bin/sap_suse_cluster_connector
/usr/bin/sap_ha_cluster_connector
/usr/bin/sap_cluster_connector
%doc /usr/share/man/man8/*.gz
#%config(noreplace) /etc/ClusterTools2

%changelog -n sap_suse_cluster_connector
* Mon Jun 04 2012 - fabian.herschel@suse.com
  BZ 763793:
  - source archive with compression
  - secured temp file
* Wed Jan 25 2012 - fabian.herschel@suse.com
  - initial package version
