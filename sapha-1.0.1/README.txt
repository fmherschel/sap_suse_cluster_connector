#
#
# BUILD
#
#    make all
#    make test
#
# INSTALL
#
#    1. Copy the library libsapha.so.1.0.1 and the symlink libsapha.so.1 to the exe directory where 
#    also sapstartsrv is located (you could also use an other directory but than you need
#    to change the configuration in the next step).
#    Example: scp libsapha.so.1* root@ls3198:/usr/sap/NA0/ASCS00/exe
#
#    2. Change the Profile read by the sapstartsrv and add the parameter service/halib
#    service/halib = $(DIR_EXECUTABLE)/libsapha.so
#    Example: START_ASCS00_sapna0as:service/halib = $(DIR_EXECUTABLE)/libsapha.so
#
#    3. Cluster needs a special op_default to enable the pending view (we need that also for ClusterTools2)
#    crm configure op_defaults record-pending=true
#
#    3. <sid>adm linux user must be member of the haclient group to be allowed to access the cluster shell
#
#    4. Force sapstartsrv to be restarted (i.e. by killing the sapstartsrv process)
#
# IMPLEMENTATION REMARKS / TODO :x
#
# - using crm_resource instead of crm, because of bugzilla: 
#   Bug 711960 - Command line interface crm fails with Traceback when called from a deamon via system()
# - test hardware at this moment is ls3198 / ls3199
# - test SAP system NA0 with an updated sapstartsrv, because sap kernel was to old
# 
