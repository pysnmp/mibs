#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/LAN
# Produced by pysmi-1.1.8 at Wed Jun 29 13:40:32 2022
# On host fv-az128-12 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, TimeTicks, ModuleIdentity, MibIdentifier, Gauge32, enterprises, IpAddress, iso, ObjectIdentity, Unsigned32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Gauge32", "enterprises", "IpAddress", "iso", "ObjectIdentity", "Unsigned32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType")
TextualConvention, TruthValue, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "MacAddress", "DisplayString")
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
mibBuilder.exportSymbols("LAN", productMib=productMib, lanInfo=lanInfo, lanSpeed=lanSpeed, lanStatus=lanStatus, peplink=peplink, PortSpeedType=PortSpeedType, lanIp=lanIp, lanSubnetMask=lanSubnetMask, lanMib=lanMib, generalMib=generalMib, PYSNMP_MODULE_ID=lanInfo)
