#
# PySNMP MIB module DLINKSW-BPDU-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-BPDU-PROTECTION-MIB
# Source digest sha256:14482f014b39017b65e4e0c914d78c9cd2f079bc27447a9e0c12c1d27a879d77
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
dlinkSwBpduProtectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 47))
dlinkSwBpduProtectionMIB.setRevisions(('2013-02-19 00:00',))
if mibBuilder.loadTexts: dlinkSwBpduProtectionMIB.setLastUpdated('2013-02-19 00:00')
if mibBuilder.loadTexts: dlinkSwBpduProtectionMIB.setOrganization('D-Link Corp.')
dBpduProtectionNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 0))
dBpduProtectionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 1))
dBpduProtectionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 2))
dBpduProtectionGlobalEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dBpduProtectionGlobalEnabled.setStatus('current')
dBpduProtectionNotifyEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dBpduProtectionNotifyEnabled.setStatus('current')
dBpduProtectionIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dBpduProtectionIfTable.setStatus('current')
dBpduProtectionIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dBpduProtectionIfEntry.setStatus('current')
dBpduProtectionIfCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("drop", 2), ("block", 3), ("shutdown", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dBpduProtectionIfCfgMode.setStatus('current')
dBpduProtectionIfAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("underAttack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dBpduProtectionIfAttackStatus.setStatus('current')
dBpduProtectionAttackOccur = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 47, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfCfgMode"))
if mibBuilder.loadTexts: dBpduProtectionAttackOccur.setStatus('current')
dBpduProtectionAttackRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 47, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dBpduProtectionAttackRecover.setStatus('current')
dBpduProtectionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 1))
dBpduProtectionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2))
dBpduProtectionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 1, 1)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionCfgGroup"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionMIBCompliance = dBpduProtectionMIBCompliance.setStatus('current')
dBpduProtectionCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 1)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionGlobalEnabled"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionNotifyEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionCfgGroup = dBpduProtectionCfgGroup.setStatus('current')
dBpduProtectionIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 2)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfCfgMode"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfAttackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionIfGroup = dBpduProtectionIfGroup.setStatus('current')
dBpduProtectionNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 3)).setObjects(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionAttackOccur"), ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionAttackRecover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dBpduProtectionNotifyGroup = dBpduProtectionNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-BPDU-PROTECTION-MIB", PYSNMP_MODULE_ID=dlinkSwBpduProtectionMIB, dBpduProtectionAttackOccur=dBpduProtectionAttackOccur, dBpduProtectionAttackRecover=dBpduProtectionAttackRecover, dBpduProtectionCfgGroup=dBpduProtectionCfgGroup, dBpduProtectionConformance=dBpduProtectionConformance, dBpduProtectionGlobalEnabled=dBpduProtectionGlobalEnabled, dBpduProtectionIfAttackStatus=dBpduProtectionIfAttackStatus, dBpduProtectionIfCfgMode=dBpduProtectionIfCfgMode, dBpduProtectionIfEntry=dBpduProtectionIfEntry, dBpduProtectionIfGroup=dBpduProtectionIfGroup, dBpduProtectionIfTable=dBpduProtectionIfTable, dBpduProtectionMIBCompliance=dBpduProtectionMIBCompliance, dBpduProtectionMIBCompliances=dBpduProtectionMIBCompliances, dBpduProtectionMIBGroups=dBpduProtectionMIBGroups, dBpduProtectionNotifications=dBpduProtectionNotifications, dBpduProtectionNotifyEnabled=dBpduProtectionNotifyEnabled, dBpduProtectionNotifyGroup=dBpduProtectionNotifyGroup, dBpduProtectionObjects=dBpduProtectionObjects, dlinkSwBpduProtectionMIB=dlinkSwBpduProtectionMIB)
