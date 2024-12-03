#
# PySNMP MIB module SAEUROPE-TRAPCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saeurope/SAEUROPE-TRAPCONTROL-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:47:25 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
msgSourceName, msgBehaviour, msgSubClass, msgStatus, msgSequenceNumber, msgDetail, msgDetailPresent, msgSubject, msgSeverity, msgGenerationTime, msgClass, msgPhysicalEntity, msgSubClassNbr, msgId, msgText = mibBuilder.importSymbols("SAEUROPE-MESSAGES-MIB", "msgSourceName", "msgBehaviour", "msgSubClass", "msgStatus", "msgSequenceNumber", "msgDetail", "msgDetailPresent", "msgSubject", "msgSeverity", "msgGenerationTime", "msgClass", "msgPhysicalEntity", "msgSubClassNbr", "msgId", "msgText")
trapControlMIBGroups, trapControl = mibBuilder.importSymbols("SAEUROPE-ROOT-MIB", "trapControlMIBGroups", "trapControl")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, Bits, Counter32, NotificationType, ObjectIdentity, Integer32, Counter64, iso, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "Integer32", "Counter64", "iso", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SAEUROPE-TRAPCONTROL-MIB", trapControlNotificationGroup2=trapControlNotificationGroup2, PYSNMP_MODULE_ID=saEuropeTrapControl, trapControlTrap=trapControlTrap, trapControlMsgTrap=trapControlMsgTrap, trapControlNotificationGroup=trapControlNotificationGroup, trapControlModuleCompliance=trapControlModuleCompliance, trapControlTrapRoot=trapControlTrapRoot, saEuropeTrapControl=saEuropeTrapControl, trapControlMsgTrap2=trapControlMsgTrap2)
