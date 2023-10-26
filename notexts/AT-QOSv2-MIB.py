#
# PySNMP MIB module AT-QOSv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-QOSv2-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:22:51 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, NotificationType, iso, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Bits, Gauge32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "NotificationType", "iso", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Bits", "Gauge32", "MibIdentifier", "IpAddress")
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
mibBuilder.exportSymbols("AT-QOSv2-MIB", atQosv2VlanId=atQosv2VlanId, atQosv2Notification=atQosv2Notification, atQosv2IfIndex=atQosv2IfIndex, atQosv2StormDetectionTrap=atQosv2StormDetectionTrap, atQosv2NotificationVariables=atQosv2NotificationVariables, atQosv2=atQosv2, PYSNMP_MODULE_ID=atQosv2)
