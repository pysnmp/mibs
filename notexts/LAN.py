#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/LAN
# Produced by pysmi-1.1.12 at Fri Jul 19 10:09:12 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, TimeTicks, NotificationType, enterprises, Unsigned32, iso, ObjectIdentity, Counter32, MibIdentifier, Bits, Counter64, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "NotificationType", "enterprises", "Unsigned32", "iso", "ObjectIdentity", "Counter32", "MibIdentifier", "Bits", "Counter64", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, MacAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TextualConvention", "TruthValue")
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
mibBuilder.exportSymbols("LAN", lanSubnetMask=lanSubnetMask, peplink=peplink, lanStatus=lanStatus, generalMib=generalMib, lanIp=lanIp, lanInfo=lanInfo, lanMib=lanMib, PortSpeedType=PortSpeedType, PYSNMP_MODULE_ID=lanInfo, productMib=productMib, lanSpeed=lanSpeed)
