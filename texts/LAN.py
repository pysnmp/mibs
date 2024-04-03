#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/LAN
# Produced by pysmi-1.1.11 at Wed Apr  3 14:02:53 2024
# On host fv-az1200-481 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, Counter64, enterprises, MibIdentifier, iso, TimeTicks, IpAddress, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "Counter64", "enterprises", "MibIdentifier", "iso", "TimeTicks", "IpAddress", "Counter32", "ObjectIdentity")
MacAddress, RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("LAN", lanMib=lanMib, PYSNMP_MODULE_ID=lanInfo, PortSpeedType=PortSpeedType, productMib=productMib, lanSpeed=lanSpeed, lanIp=lanIp, lanStatus=lanStatus, peplink=peplink, generalMib=generalMib, lanSubnetMask=lanSubnetMask, lanInfo=lanInfo)
