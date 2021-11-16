#
# PySNMP MIB module AT-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-UDLD-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:52:14 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, iso, ModuleIdentity, NotificationType, MibIdentifier, Counter32, ObjectIdentity, Bits, TimeTicks, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "iso", "ModuleIdentity", "NotificationType", "MibIdentifier", "Counter32", "ObjectIdentity", "Bits", "TimeTicks", "IpAddress", "Unsigned32")
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
mibBuilder.exportSymbols("AT-UDLD-MIB", atUdld=atUdld, atUdldPortRecoveredTrap=atUdldPortRecoveredTrap, atUdldPortDisabledTrap=atUdldPortDisabledTrap, atUdldTrap=atUdldTrap, atUdldIfIndex=atUdldIfIndex, PYSNMP_MODULE_ID=atUdld)
