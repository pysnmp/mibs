#
# PySNMP MIB module AT-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-UDLD-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 12:47:07 2023
# On host fv-az575-466 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Counter64, NotificationType, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, ModuleIdentity, Gauge32, Bits, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Counter64", "NotificationType", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "ModuleIdentity", "Gauge32", "Bits", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("AT-UDLD-MIB", atUdld=atUdld, atUdldTrap=atUdldTrap, atUdldIfIndex=atUdldIfIndex, atUdldPortRecoveredTrap=atUdldPortRecoveredTrap, atUdldPortDisabledTrap=atUdldPortDisabledTrap, PYSNMP_MODULE_ID=atUdld)
