#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/LAN
# Produced by pysmi-1.1.8 at Fri Jan 27 15:52:59 2023
# On host fv-az551-95 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, IpAddress, Bits, NotificationType, ObjectIdentity, enterprises, iso, Integer32, Unsigned32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "Bits", "NotificationType", "ObjectIdentity", "enterprises", "iso", "Integer32", "Unsigned32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32")
RowStatus, TextualConvention, DisplayString, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue", "MacAddress")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
lanMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3))
lanInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1))
if mibBuilder.loadTexts: lanInfo.setLastUpdated('201305220000Z')
if mibBuilder.loadTexts: lanInfo.setOrganization('PEPLINK')
if mibBuilder.loadTexts: lanInfo.setContactInfo('')
if mibBuilder.loadTexts: lanInfo.setDescription('MIB module for LAN.')
class PortSpeedType(TextualConvention, Integer32):
    description = 'Describe the port speed and type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

lanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1))
lanIp = MibScalar((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanIp.setStatus('current')
if mibBuilder.loadTexts: lanIp.setDescription('LAN IP address.')
lanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSubnetMask.setStatus('current')
if mibBuilder.loadTexts: lanSubnetMask.setDescription('LAN subnet mask.')
lanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 23695, 200, 1, 3, 1, 1, 3), PortSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSpeed.setStatus('current')
if mibBuilder.loadTexts: lanSpeed.setDescription('LAN speed status (Auto/10baseT-FD/\n\t\t\t\t\t\t10baseT-HD/100baseTx-FD/100baseTx-HD/1000baseTx-FD/\n\t\t\t\t\t\t1000baseTx-HD.')
mibBuilder.exportSymbols("LAN", generalMib=generalMib, lanMib=lanMib, lanSubnetMask=lanSubnetMask, lanIp=lanIp, PYSNMP_MODULE_ID=lanInfo, productMib=productMib, lanInfo=lanInfo, lanSpeed=lanSpeed, peplink=peplink, PortSpeedType=PortSpeedType, lanStatus=lanStatus)
