#
# PySNMP MIB module CISCOWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOWORKS-MIB
# Source digest sha256:b20a8a808fdfc6215995fb77d605fe738a5d8dcb0b785f65617d736b839fa605
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoworks, = mibBuilder.importSymbols("CISCO-SMI", "ciscoworks")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 14, 1))
cwLogMIB.setRevisions(('2003-02-18 00:00', '1995-04-02 00:00',))
if mibBuilder.loadTexts: cwLogMIB.setLastUpdated('2003-02-18 00:00')
if mibBuilder.loadTexts: cwLogMIB.setOrganization('Cisco Systems, Inc.')
cwLog = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 1))
cwTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2))
cwMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3))
cwLogDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(15, 15)).setFixedLength(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogDate.setStatus('current')
cwLogSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ciscoworks", 2), ("device", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogSource.setStatus('current')
cwLogApp = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogApp.setStatus('current')
cwLogMsg = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogMsg.setStatus('current')
cwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0))
cwAppLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwAppLogTrap.setStatus('current')
cwDevLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwDevLogTrap.setStatus('current')
ciscoCwMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1))
ciscoCwMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2))
ciscoCwMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1, 1)).setObjects(("CISCOWORKS-MIB", "ciscoCwObjectsGroup"), ("CISCOWORKS-MIB", "ciscoCwNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwMIBCompliance = ciscoCwMIBCompliance.setStatus('current')
ciscoCwObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 7)).setObjects(("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwObjectsGroup = ciscoCwObjectsGroup.setStatus('current')
ciscoCwNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 12)).setObjects(("CISCOWORKS-MIB", "cwAppLogTrap"), ("CISCOWORKS-MIB", "cwDevLogTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwNotificationsGroup = ciscoCwNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCOWORKS-MIB", PYSNMP_MODULE_ID=cwLogMIB, ciscoCwMIBCompliance=ciscoCwMIBCompliance, ciscoCwMIBCompliances=ciscoCwMIBCompliances, ciscoCwMIBGroups=ciscoCwMIBGroups, ciscoCwNotificationsGroup=ciscoCwNotificationsGroup, ciscoCwObjectsGroup=ciscoCwObjectsGroup, cwAppLogTrap=cwAppLogTrap, cwDevLogTrap=cwDevLogTrap, cwLog=cwLog, cwLogApp=cwLogApp, cwLogDate=cwLogDate, cwLogMIB=cwLogMIB, cwLogMsg=cwLogMsg, cwLogSource=cwLogSource, cwMIBConform=cwMIBConform, cwTraps=cwTraps, cwTrapsPrefix=cwTrapsPrefix)
