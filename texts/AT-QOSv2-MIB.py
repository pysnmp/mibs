#
# PySNMP MIB module AT-QOSv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-QOSv2-MIB
# Produced by pysmi-1.1.12 at Mon Sep 16 14:51:07 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Gauge32, iso, Integer32, Counter64, Counter32, NotificationType, ObjectIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Gauge32", "iso", "Integer32", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atQosv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503))
atQosv2.setRevisions(('2015-08-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atQosv2.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: atQosv2.setLastUpdated('201508310000Z')
if mibBuilder.loadTexts: atQosv2.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: atQosv2.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atQosv2.setDescription('This MIB file contains definitions of managed objects for the\n                QoS module.')
atQosv2Notification = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 0))
atQosv2StormDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 0, 1)).setObjects(("AT-QOSv2-MIB", "atQosv2IfIndex"), ("AT-QOSv2-MIB", "atQosv2VlanId"))
if mibBuilder.loadTexts: atQosv2StormDetectionTrap.setStatus('current')
if mibBuilder.loadTexts: atQosv2StormDetectionTrap.setDescription('Generated when QoS Storm Protection feature detects a storm.')
atQosv2NotificationVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1))
atQosv2IfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atQosv2IfIndex.setStatus('current')
if mibBuilder.loadTexts: atQosv2IfIndex.setDescription('The index of the interface where the storm is detected on.')
atQosv2VlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 503, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atQosv2VlanId.setStatus('current')
if mibBuilder.loadTexts: atQosv2VlanId.setDescription('The VLAN ID of the interface where the storm is detected on.')
mibBuilder.exportSymbols("AT-QOSv2-MIB", atQosv2StormDetectionTrap=atQosv2StormDetectionTrap, atQosv2=atQosv2, atQosv2NotificationVariables=atQosv2NotificationVariables, atQosv2VlanId=atQosv2VlanId, atQosv2Notification=atQosv2Notification, atQosv2IfIndex=atQosv2IfIndex, PYSNMP_MODULE_ID=atQosv2)
