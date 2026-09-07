#
# PySNMP MIB module CISCO-SECURE-SHELL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SECURE-SHELL-MIB
# Source digest sha256:dc2bc160f69262f264137607094d202abc82c42b24a925de60890586a803fd93
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
ciscoSecureShellMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 339))
ciscoSecureShellMIB.setRevisions(('2005-06-01 00:00', '2004-04-05 00:00', '2003-09-18 00:00', '2002-10-05 00:00',))
if mibBuilder.loadTexts: ciscoSecureShellMIB.setLastUpdated('2005-06-01 00:00')
if mibBuilder.loadTexts: ciscoSecureShellMIB.setOrganization('Cisco Systems, Inc.')
ciscoSecureShellMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 1))
cssConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1))
cssSessionInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2))
class CssVersions(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("v1", 0), ("v2", 1))

cssServiceActivation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssServiceActivation.setStatus('current')
cssKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cssKeyTable.setStatus('current')
cssKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-SECURE-SHELL-MIB", "cssKeyIndex"))
if mibBuilder.loadTexts: cssKeyEntry.setStatus('current')
cssKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rsa", 1), ("rsa1", 2), ("dsa", 3)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cssKeyIndex.setStatus('current')
cssKeyNBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cssKeyNBits.setStatus('current')
cssKeyOverWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cssKeyOverWrite.setStatus('current')
cssKeyLastCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssKeyLastCreationTime.setStatus('current')
cssKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cssKeyRowStatus.setStatus('current')
cssKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssKeyString.setStatus('current')
cssServiceCapability = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 3), CssVersions()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssServiceCapability.setStatus('current')
cssServiceMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 4), CssVersions()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cssServiceMode.setStatus('current')
cssKeyGenerationStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inProgress", 1), ("successful", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssKeyGenerationStatus.setStatus('current')
cssSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cssSessionTable.setStatus('current')
cssSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-SECURE-SHELL-MIB", "cssSessionID"))
if mibBuilder.loadTexts: cssSessionEntry.setStatus('current')
cssSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cssSessionID.setStatus('current')
cssSessionVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("one", 1), ("two", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionVersion.setStatus('current')
cssSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("sshSessionVersionOk", 1), ("sshSessionKeysExchanged", 2), ("sshSessionAuthenticated", 3), ("sshSessionOpen", 4), ("sshSessionDisconnecting", 5), ("sshSessionDisconnected", 6), ("sshSessionClosed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionState.setStatus('current')
cssSessionPID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionPID.setStatus('current')
cssSessionUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionUserID.setStatus('current')
cssSessionHostAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionHostAddrType.setStatus('current')
cssSessionHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 339, 1, 2, 1, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cssSessionHostAddr.setStatus('current')
ciscoSecureShellMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 2))
ciscoSecureShellMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1))
ciscoSecureShellMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2))
ciscoSecureShellMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 1)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBCompliance = ciscoSecureShellMIBCompliance.setStatus('deprecated')
ciscoSecureShellMIBComplianceRv1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 2)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBComplianceRv1 = ciscoSecureShellMIBComplianceRv1.setStatus('deprecated')
ciscoSecureShellMIBComplianceRv2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 3)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupRev1"), ("CISCO-SECURE-SHELL-MIB", "cssServiceModeCfgGroup"), ("CISCO-SECURE-SHELL-MIB", "cssSessionInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBComplianceRv2 = ciscoSecureShellMIBComplianceRv2.setStatus('deprecated')
ciscoSecureShellMIBComplianceRv3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 1, 4)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupRev1"), ("CISCO-SECURE-SHELL-MIB", "cssConfigurationGroupSupp1"), ("CISCO-SECURE-SHELL-MIB", "cssServiceModeCfgGroup"), ("CISCO-SECURE-SHELL-MIB", "cssSessionInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSecureShellMIBComplianceRv3 = ciscoSecureShellMIBComplianceRv3.setStatus('current')
cssConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 1)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssServiceActivation"), ("CISCO-SECURE-SHELL-MIB", "cssKeyNBits"), ("CISCO-SECURE-SHELL-MIB", "cssKeyOverWrite"), ("CISCO-SECURE-SHELL-MIB", "cssKeyLastCreationTime"), ("CISCO-SECURE-SHELL-MIB", "cssKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssConfigurationGroup = cssConfigurationGroup.setStatus('deprecated')
cssConfigurationGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 2)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssServiceActivation"), ("CISCO-SECURE-SHELL-MIB", "cssKeyNBits"), ("CISCO-SECURE-SHELL-MIB", "cssKeyOverWrite"), ("CISCO-SECURE-SHELL-MIB", "cssKeyLastCreationTime"), ("CISCO-SECURE-SHELL-MIB", "cssKeyString"), ("CISCO-SECURE-SHELL-MIB", "cssKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssConfigurationGroupRev1 = cssConfigurationGroupRev1.setStatus('current')
cssServiceModeCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 3)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssServiceCapability"), ("CISCO-SECURE-SHELL-MIB", "cssServiceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssServiceModeCfgGroup = cssServiceModeCfgGroup.setStatus('current')
cssSessionInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 4)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssSessionVersion"), ("CISCO-SECURE-SHELL-MIB", "cssSessionState"), ("CISCO-SECURE-SHELL-MIB", "cssSessionPID"), ("CISCO-SECURE-SHELL-MIB", "cssSessionUserID"), ("CISCO-SECURE-SHELL-MIB", "cssSessionHostAddrType"), ("CISCO-SECURE-SHELL-MIB", "cssSessionHostAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssSessionInfoGroup = cssSessionInfoGroup.setStatus('current')
cssConfigurationGroupSupp1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 339, 2, 2, 5)).setObjects(("CISCO-SECURE-SHELL-MIB", "cssKeyGenerationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cssConfigurationGroupSupp1 = cssConfigurationGroupSupp1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SECURE-SHELL-MIB", CssVersions=CssVersions, PYSNMP_MODULE_ID=ciscoSecureShellMIB, ciscoSecureShellMIB=ciscoSecureShellMIB, ciscoSecureShellMIBCompliance=ciscoSecureShellMIBCompliance, ciscoSecureShellMIBComplianceRv1=ciscoSecureShellMIBComplianceRv1, ciscoSecureShellMIBComplianceRv2=ciscoSecureShellMIBComplianceRv2, ciscoSecureShellMIBComplianceRv3=ciscoSecureShellMIBComplianceRv3, ciscoSecureShellMIBCompliances=ciscoSecureShellMIBCompliances, ciscoSecureShellMIBConformance=ciscoSecureShellMIBConformance, ciscoSecureShellMIBGroups=ciscoSecureShellMIBGroups, ciscoSecureShellMIBObjects=ciscoSecureShellMIBObjects, cssConfiguration=cssConfiguration, cssConfigurationGroup=cssConfigurationGroup, cssConfigurationGroupRev1=cssConfigurationGroupRev1, cssConfigurationGroupSupp1=cssConfigurationGroupSupp1, cssKeyEntry=cssKeyEntry, cssKeyGenerationStatus=cssKeyGenerationStatus, cssKeyIndex=cssKeyIndex, cssKeyLastCreationTime=cssKeyLastCreationTime, cssKeyNBits=cssKeyNBits, cssKeyOverWrite=cssKeyOverWrite, cssKeyRowStatus=cssKeyRowStatus, cssKeyString=cssKeyString, cssKeyTable=cssKeyTable, cssServiceActivation=cssServiceActivation, cssServiceCapability=cssServiceCapability, cssServiceMode=cssServiceMode, cssServiceModeCfgGroup=cssServiceModeCfgGroup, cssSessionEntry=cssSessionEntry, cssSessionHostAddr=cssSessionHostAddr, cssSessionHostAddrType=cssSessionHostAddrType, cssSessionID=cssSessionID, cssSessionInfo=cssSessionInfo, cssSessionInfoGroup=cssSessionInfoGroup, cssSessionPID=cssSessionPID, cssSessionState=cssSessionState, cssSessionTable=cssSessionTable, cssSessionUserID=cssSessionUserID, cssSessionVersion=cssSessionVersion)
