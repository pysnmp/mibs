#
# PySNMP MIB module AT-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-UDLD-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:53:46 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter64, NotificationType, Counter32, Gauge32, Unsigned32, MibIdentifier, IpAddress, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter64", "NotificationType", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "Integer32", "ModuleIdentity")
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
mibBuilder.exportSymbols("AT-UDLD-MIB", atUdldTrap=atUdldTrap, PYSNMP_MODULE_ID=atUdld, atUdldPortDisabledTrap=atUdldPortDisabledTrap, atUdld=atUdld, atUdldPortRecoveredTrap=atUdldPortRecoveredTrap, atUdldIfIndex=atUdldIfIndex)
