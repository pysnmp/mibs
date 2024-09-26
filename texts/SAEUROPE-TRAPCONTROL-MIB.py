#
# PySNMP MIB module SAEUROPE-TRAPCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saeurope/SAEUROPE-TRAPCONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 26 02:18:32 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
msgSubClass, msgDetail, msgSequenceNumber, msgSeverity, msgClass, msgSubClassNbr, msgGenerationTime, msgStatus, msgDetailPresent, msgPhysicalEntity, msgSourceName, msgText, msgSubject, msgId, msgBehaviour = mibBuilder.importSymbols("SAEUROPE-MESSAGES-MIB", "msgSubClass", "msgDetail", "msgSequenceNumber", "msgSeverity", "msgClass", "msgSubClassNbr", "msgGenerationTime", "msgStatus", "msgDetailPresent", "msgPhysicalEntity", "msgSourceName", "msgText", "msgSubject", "msgId", "msgBehaviour")
trapControlMIBGroups, trapControl = mibBuilder.importSymbols("SAEUROPE-ROOT-MIB", "trapControlMIBGroups", "trapControl")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, IpAddress, iso, Gauge32, Bits, Unsigned32, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "IpAddress", "iso", "Gauge32", "Bits", "Unsigned32", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
saEuropeTrapControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1))
saEuropeTrapControl.setRevisions(('2015-11-10 13:00', '2005-09-09 08:00', '2002-11-30 14:00', '2002-07-02 17:30', '2002-06-21 13:30', '2001-08-31 13:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: saEuropeTrapControl.setRevisionsDescriptions(('Updated contact info.', 'V01.01.00\n       Added trapControlMsgTrap2.', 'V01.00.03       \n       Initial version of the SA Europe Trap Control MIB.\n       Changes to MIB name and OID names, contents of the MIB are \n       the same as BarcoNet Trap Control MIB V01.00.02.', 'V01.00.02       \n       Small editorial changes.', 'V01.00.01       \n       trapControlNotificationGroup is chosen as mandatory group.', 'V01.00.00       \n       Initial version of the Trap Control MIB.',))
if mibBuilder.loadTexts: saEuropeTrapControl.setLastUpdated('201511101300Z')
if mibBuilder.loadTexts: saEuropeTrapControl.setOrganization('Synamedia')
if mibBuilder.loadTexts: saEuropeTrapControl.setContactInfo('https://www.synamedia.com/video-professional-services/')
if mibBuilder.loadTexts: saEuropeTrapControl.setDescription('MIB for the Synamedia Trap Control')
trapControlTrapRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 1))
trapControlTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 1, 0))
trapControlMsgTrap = NotificationType((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 0)).setObjects(("SAEUROPE-MESSAGES-MIB", "msgId"), ("SAEUROPE-MESSAGES-MIB", "msgSourceName"), ("SAEUROPE-MESSAGES-MIB", "msgText"), ("SAEUROPE-MESSAGES-MIB", "msgSubject"), ("SAEUROPE-MESSAGES-MIB", "msgGenerationTime"), ("SAEUROPE-MESSAGES-MIB", "msgBehaviour"), ("SAEUROPE-MESSAGES-MIB", "msgClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClassNbr"), ("SAEUROPE-MESSAGES-MIB", "msgDetailPresent"), ("SAEUROPE-MESSAGES-MIB", "msgStatus"), ("SAEUROPE-MESSAGES-MIB", "msgSeverity"), ("SAEUROPE-MESSAGES-MIB", "msgSequenceNumber"), ("SAEUROPE-MESSAGES-MIB", "msgDetail"))
if mibBuilder.loadTexts: trapControlMsgTrap.setStatus('current')
if mibBuilder.loadTexts: trapControlMsgTrap.setDescription('This trap is sent when a message is generated in the device for\n         which msgPhysicalEntity, msgNetworkInterfaceAddress and msgUdpPort\n         are not relevant.')
trapControlMsgTrap2 = NotificationType((1, 3, 6, 1, 4, 1, 1482, 20, 1, 1, 1, 1, 0, 1)).setObjects(("SAEUROPE-MESSAGES-MIB", "msgId"), ("SAEUROPE-MESSAGES-MIB", "msgSourceName"), ("SAEUROPE-MESSAGES-MIB", "msgText"), ("SAEUROPE-MESSAGES-MIB", "msgSubject"), ("SAEUROPE-MESSAGES-MIB", "msgGenerationTime"), ("SAEUROPE-MESSAGES-MIB", "msgBehaviour"), ("SAEUROPE-MESSAGES-MIB", "msgClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClass"), ("SAEUROPE-MESSAGES-MIB", "msgSubClassNbr"), ("SAEUROPE-MESSAGES-MIB", "msgDetailPresent"), ("SAEUROPE-MESSAGES-MIB", "msgStatus"), ("SAEUROPE-MESSAGES-MIB", "msgSeverity"), ("SAEUROPE-MESSAGES-MIB", "msgDetail"), ("SAEUROPE-MESSAGES-MIB", "msgPhysicalEntity"))
if mibBuilder.loadTexts: trapControlMsgTrap2.setStatus('current')
if mibBuilder.loadTexts: trapControlMsgTrap2.setDescription('This trap is sent when a message is generated in the device\n         for which the msgPhysicalEntity, msgNetworkInterfaceAddress and\n         msgUdpPort are relevant.')
trapControlModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1482, 1, 1, 1, 1)).setObjects(("SAEUROPE-TRAPCONTROL-MIB", "trapControlNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapControlModuleCompliance = trapControlModuleCompliance.setStatus('current')
if mibBuilder.loadTexts: trapControlModuleCompliance.setDescription('The compliance statement for entities which\n         implement the SA Europe Trap Control MIB')
trapControlNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1482, 1, 1, 1, 2)).setObjects(("SAEUROPE-TRAPCONTROL-MIB", "trapControlMsgTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapControlNotificationGroup = trapControlNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: trapControlNotificationGroup.setDescription('Trap control notification group.')
trapControlNotificationGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 1482, 1, 1, 1, 3)).setObjects(("SAEUROPE-TRAPCONTROL-MIB", "trapControlMsgTrap2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trapControlNotificationGroup2 = trapControlNotificationGroup2.setStatus('current')
if mibBuilder.loadTexts: trapControlNotificationGroup2.setDescription('Trap control notification group version 2.')
mibBuilder.exportSymbols("SAEUROPE-TRAPCONTROL-MIB", trapControlModuleCompliance=trapControlModuleCompliance, trapControlNotificationGroup=trapControlNotificationGroup, trapControlMsgTrap=trapControlMsgTrap, saEuropeTrapControl=saEuropeTrapControl, trapControlTrapRoot=trapControlTrapRoot, trapControlMsgTrap2=trapControlMsgTrap2, trapControlNotificationGroup2=trapControlNotificationGroup2, PYSNMP_MODULE_ID=saEuropeTrapControl, trapControlTrap=trapControlTrap)
