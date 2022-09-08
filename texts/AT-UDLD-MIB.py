#
# PySNMP MIB module AT-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-UDLD-MIB
# Produced by pysmi-1.1.8 at Thu Sep  8 09:47:00 2022
# On host fv-az173-382 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Bits, Gauge32, MibIdentifier, ObjectIdentity, Unsigned32, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Bits", "Gauge32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550))
atUdld.setRevisions(('2011-11-22 00:00', '2011-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atUdld.setRevisionsDescriptions(('The definition of OBJECT IDENTIFIER was modified.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: atUdld.setLastUpdated('201111220000Z')
if mibBuilder.loadTexts: atUdld.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: atUdld.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atUdld.setDescription('This MIB file contains definitions of managed objects for the\n                UDLD module.')
atUdldTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0))
atUdldPortDisabledTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 1)).setObjects(("AT-UDLD-MIB", "atUdldIfIndex"))
if mibBuilder.loadTexts: atUdldPortDisabledTrap.setStatus('current')
if mibBuilder.loadTexts: atUdldPortDisabledTrap.setDescription('Generated when UDLD feature disabled an interface when\n                 detecting uni-directional link.')
atUdldPortRecoveredTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 2)).setObjects(("AT-UDLD-MIB", "atUdldIfIndex"))
if mibBuilder.loadTexts: atUdldPortRecoveredTrap.setStatus('current')
if mibBuilder.loadTexts: atUdldPortRecoveredTrap.setDescription('Generated when an interface recovers from error disable\n                 status when detecting uni-directional link.')
atUdldIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUdldIfIndex.setStatus('current')
if mibBuilder.loadTexts: atUdldIfIndex.setDescription('The index value of an interface of which the link status\n                 is changed.')
mibBuilder.exportSymbols("AT-UDLD-MIB", atUdldPortDisabledTrap=atUdldPortDisabledTrap, PYSNMP_MODULE_ID=atUdld, atUdldPortRecoveredTrap=atUdldPortRecoveredTrap, atUdld=atUdld, atUdldTrap=atUdldTrap, atUdldIfIndex=atUdldIfIndex)
