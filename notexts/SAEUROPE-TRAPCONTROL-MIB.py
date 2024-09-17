#
# PySNMP MIB module SAEUROPE-TRAPCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saeurope/SAEUROPE-TRAPCONTROL-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:27:52 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
msgGenerationTime, msgSubClassNbr, msgSeverity, msgSubClass, msgDetailPresent, msgClass, msgStatus, msgSourceName, msgSubject, msgDetail, msgPhysicalEntity, msgBehaviour, msgText, msgSequenceNumber, msgId = mibBuilder.importSymbols("SAEUROPE-MESSAGES-MIB", "msgGenerationTime", "msgSubClassNbr", "msgSeverity", "msgSubClass", "msgDetailPresent", "msgClass", "msgStatus", "msgSourceName", "msgSubject", "msgDetail", "msgPhysicalEntity", "msgBehaviour", "msgText", "msgSequenceNumber", "msgId")
trapControlMIBGroups, trapControl = mibBuilder.importSymbols("SAEUROPE-ROOT-MIB", "trapControlMIBGroups", "trapControl")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, Counter32, MibIdentifier, IpAddress, Bits, Counter64, NotificationType, TimeTicks, Integer32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Counter32", "MibIdentifier", "IpAddress", "Bits", "Counter64", "NotificationType", "TimeTicks", "Integer32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
saEuropeTrapControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1))
saEuropeTrapControl.setRevisions(('2015-11-10 13:00', '2005-09-09 08:00', '2002-11-30 14:00', '2002-07-02 17:30', '2002-06-21 13:30', '2001-08-31 13:30',))
if mibBuilder.loadTexts: saEuropeTrapControl.setLastUpdated('201511101300Z')
if mibBuilder.loadTexts: saEuropeTrapControl.setOrganization('Synamedia')
trapControlTrapRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 1))
trapControlTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 1, 0))
trapControlMsgTrap = NotificationType((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 0)).setObjects(("SAEUROPE-MESSAGES-MIB", "msgId"), ("SAEUROPE-MESSAGES-MIB", "msgSourceName"), ("SAEUROPE-MESSAGES-MIB", "msgText"), ("SAEUROPE-MESSAGES-MIB", "msgSubject"), ("SAEUROPE-MESSAGES-MIB", "msgGenerationTime"), ("SAEUROPE-MESSAGES-MIB", "msgBehaviour"), ("SAEUROPE-MESSAGES-MIB", "msgClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClassNbr"), ("SAEUROPE-MESSAGES-MIB", "msgDetailPresent"), ("SAEUROPE-MESSAGES-MIB", "msgStatus"), ("SAEUROPE-MESSAGES-MIB", "msgSeverity"), ("SAEUROPE-MESSAGES-MIB", "msgSequenceNumber"), ("SAEUROPE-MESSAGES-MIB", "msgDetail"))
if mibBuilder.loadTexts: trapControlMsgTrap.setStatus('current')
trapControlMsgTrap2 = NotificationType((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 1, 0, 1)).setObjects(("SAEUROPE-MESSAGES-MIB", "msgId"), ("SAEUROPE-MESSAGES-MIB", "msgSourceName"), ("SAEUROPE-MESSAGES-MIB", "msgText"), ("SAEUROPE-MESSAGES-MIB", "msgSubject"), ("SAEUROPE-MESSAGES-MIB", "msgGenerationTime"), ("SAEUROPE-MESSAGES-MIB", "msgBehaviour"), ("SAEUROPE-MESSAGES-MIB", "msgClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClassNbr"), ("SAEUROPE-MESSAGES-MIB", "msgDetailPresent"), ("SAEUROPE-MESSAGES-MIB", "msgStatus"), ("SAEUROPE-MESSAGES-MIB", "msgSeverity"), ("SAEUROPE-MESSAGES-MIB", "msgDetail"), ("SAEUROPE-MESSAGES-MIB", "msgPhysicalEntity"))
if mibBuilder.loadTexts: trapControlMsgTrap2.setStatus('current')
trapControlModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1482, 1, 1, 1, 1)).setObjects(("SAEUROPE-TRAPCONTROL-MIB", "trapControlNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapControlModuleCompliance = trapControlModuleCompliance.setStatus('current')
trapControlNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1482, 1, 1, 1, 2)).setObjects(("SAEUROPE-TRAPCONTROL-MIB", "trapControlMsgTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapControlNotificationGroup = trapControlNotificationGroup.setStatus('current')
trapControlNotificationGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 1482, 1, 1, 1, 3)).setObjects(("SAEUROPE-TRAPCONTROL-MIB", "trapControlMsgTrap2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapControlNotificationGroup2 = trapControlNotificationGroup2.setStatus('current')
mibBuilder.exportSymbols("SAEUROPE-TRAPCONTROL-MIB", PYSNMP_MODULE_ID=saEuropeTrapControl, trapControlMsgTrap=trapControlMsgTrap, trapControlTrap=trapControlTrap, trapControlModuleCompliance=trapControlModuleCompliance, trapControlNotificationGroup=trapControlNotificationGroup, trapControlMsgTrap2=trapControlMsgTrap2, trapControlNotificationGroup2=trapControlNotificationGroup2, saEuropeTrapControl=saEuropeTrapControl, trapControlTrapRoot=trapControlTrapRoot)
