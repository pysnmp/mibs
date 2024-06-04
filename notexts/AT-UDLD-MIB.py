#
# PySNMP MIB module AT-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-UDLD-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 02:36:40 2024
# On host fv-az1200-411 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Integer32, ModuleIdentity, IpAddress, MibIdentifier, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Bits, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550))
atUdld.setRevisions(('2011-11-22 00:00', '2011-05-15 00:00',))
if mibBuilder.loadTexts: atUdld.setLastUpdated('201111220000Z')
if mibBuilder.loadTexts: atUdld.setOrganization('Allied Telesis, Inc.')
atUdldTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0))
atUdldPortDisabledTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 1)).setObjects(("AT-UDLD-MIB", "atUdldIfIndex"))
if mibBuilder.loadTexts: atUdldPortDisabledTrap.setStatus('current')
atUdldPortRecoveredTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 2)).setObjects(("AT-UDLD-MIB", "atUdldIfIndex"))
if mibBuilder.loadTexts: atUdldPortRecoveredTrap.setStatus('current')
atUdldIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUdldIfIndex.setStatus('current')
mibBuilder.exportSymbols("AT-UDLD-MIB", PYSNMP_MODULE_ID=atUdld, atUdld=atUdld, atUdldPortRecoveredTrap=atUdldPortRecoveredTrap, atUdldIfIndex=atUdldIfIndex, atUdldPortDisabledTrap=atUdldPortDisabledTrap, atUdldTrap=atUdldTrap)
