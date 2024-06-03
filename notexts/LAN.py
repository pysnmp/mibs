#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/LAN
# Produced by pysmi-1.1.12 at Mon Jun  3 03:07:46 2024
# On host fv-az736-440 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
enterprises, Integer32, IpAddress, iso, TimeTicks, NotificationType, Gauge32, Unsigned32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "IpAddress", "iso", "TimeTicks", "NotificationType", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier")
RowStatus, TruthValue, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString", "MacAddress")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
lanMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3))
lanInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1))
if mibBuilder.loadTexts: lanInfo.setLastUpdated('201305220000Z')
if mibBuilder.loadTexts: lanInfo.setOrganization('PEPLINK')
class PortSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

lanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1))
lanIp = MibScalar((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanIp.setStatus('current')
lanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSubnetMask.setStatus('current')
lanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 3), PortSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSpeed.setStatus('current')
mibBuilder.exportSymbols("LAN", lanIp=lanIp, peplink=peplink, lanMib=lanMib, PortSpeedType=PortSpeedType, lanStatus=lanStatus, lanSpeed=lanSpeed, PYSNMP_MODULE_ID=lanInfo, lanSubnetMask=lanSubnetMask, generalMib=generalMib, productMib=productMib, lanInfo=lanInfo)
