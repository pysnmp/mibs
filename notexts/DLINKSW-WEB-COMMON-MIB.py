#
# PySNMP MIB module DLINKSW-WEB-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-WEB-COMMON-MIB
# Source digest sha256:0e49e1fb757520ad147712e7a45c6262f04d68b5c331640febc23c6aa16cf99c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
dlinkSwWebCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 162))
dlinkSwWebCommonMIB.setRevisions(('2013-10-28 00:00',))
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setLastUpdated('2013-10-28 00:00')
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setOrganization('D-Link Corp.')
dWebCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 0))
dWebMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1))
dWebCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2))
dHttpServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1))
dSslServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2))
dHttpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpServerStatus.setStatus('current')
dHttpTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpTcpPort.setStatus('current')
dHttpIdleTimeoutVal = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 36000)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpIdleTimeoutVal.setStatus('current')
dSslServicePolicyName = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSslServicePolicyName.setStatus('current')
dSslServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSslServerStatus.setStatus('current')
dWebCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1))
dWebCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2))
dWebMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1, 1)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dHttpServerGroups"), ("DLINKSW-WEB-COMMON-MIB", "dSslServerGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dWebMIBCompliance = dWebMIBCompliance.setStatus('current')
dHttpServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 1)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dHttpServerStatus"), ("DLINKSW-WEB-COMMON-MIB", "dHttpTcpPort"), ("DLINKSW-WEB-COMMON-MIB", "dHttpIdleTimeoutVal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dHttpServerGroups = dHttpServerGroups.setStatus('current')
dSslServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 2)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dSslServicePolicyName"), ("DLINKSW-WEB-COMMON-MIB", "dSslServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSslServerGroups = dSslServerGroups.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-WEB-COMMON-MIB", PYSNMP_MODULE_ID=dlinkSwWebCommonMIB, dHttpIdleTimeoutVal=dHttpIdleTimeoutVal, dHttpServerGroups=dHttpServerGroups, dHttpServerObjects=dHttpServerObjects, dHttpServerStatus=dHttpServerStatus, dHttpTcpPort=dHttpTcpPort, dSslServerGroups=dSslServerGroups, dSslServerObjects=dSslServerObjects, dSslServerStatus=dSslServerStatus, dSslServicePolicyName=dSslServicePolicyName, dWebCommonGroups=dWebCommonGroups, dWebCommonMIBCompliances=dWebCommonMIBCompliances, dWebCommonMIBConformance=dWebCommonMIBConformance, dWebCommonMIBNotifications=dWebCommonMIBNotifications, dWebMIBCompliance=dWebMIBCompliance, dWebMIBObjects=dWebMIBObjects, dlinkSwWebCommonMIB=dlinkSwWebCommonMIB)
