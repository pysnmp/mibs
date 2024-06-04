#
# PySNMP MIB module AT-QOSv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-QOSv2-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:17:48 2024
# On host fv-az1789-327 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, TimeTicks, Counter32, Counter64, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atQosv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503))
atQosv2.setRevisions(('2015-08-31 00:00',))
if mibBuilder.loadTexts: atQosv2.setLastUpdated('201508310000Z')
if mibBuilder.loadTexts: atQosv2.setOrganization('Allied Telesis, Inc.')
atQosv2Notification = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 0))
atQosv2StormDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 0, 1)).setObjects(("AT-QOSv2-MIB", "atQosv2IfIndex"), ("AT-QOSv2-MIB", "atQosv2VlanId"))
if mibBuilder.loadTexts: atQosv2StormDetectionTrap.setStatus('current')
atQosv2NotificationVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1))
atQosv2IfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atQosv2IfIndex.setStatus('current')
atQosv2VlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atQosv2VlanId.setStatus('current')
mibBuilder.exportSymbols("AT-QOSv2-MIB", atQosv2NotificationVariables=atQosv2NotificationVariables, atQosv2VlanId=atQosv2VlanId, atQosv2IfIndex=atQosv2IfIndex, atQosv2=atQosv2, PYSNMP_MODULE_ID=atQosv2, atQosv2Notification=atQosv2Notification, atQosv2StormDetectionTrap=atQosv2StormDetectionTrap)
