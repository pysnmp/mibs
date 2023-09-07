#
# PySNMP MIB module AT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-IP-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:08:24 2023
# On host fv-az548-537 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, TimeTicks, IpAddress, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
atIpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602))
atIpMib.setRevisions(('2010-06-14 05:09', '2008-11-10 00:00',))
if mibBuilder.loadTexts: atIpMib.setLastUpdated('201006140509Z')
if mibBuilder.loadTexts: atIpMib.setOrganization('Allied Telesis Labs New Zealand')
class AtIpAddressAssignmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notSet", 0), ("primary", 1), ("secondary", 2))

atIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1), )
if mibBuilder.loadTexts: atIpAddressTable.setStatus('current')
atIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1), ).setIndexNames((0, "AT-IP-MIB", "atIpAddressAddrType"), (0, "AT-IP-MIB", "atIpAddressAddr"))
if mibBuilder.loadTexts: atIpAddressEntry.setStatus('current')
atIpAddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: atIpAddressAddrType.setStatus('current')
atIpAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: atIpAddressAddr.setStatus('current')
atIpAddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressPrefixLen.setStatus('current')
atIpAddressLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressLabel.setStatus('current')
atIpAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressIfIndex.setStatus('current')
atIpAddressAssignmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 6), AtIpAddressAssignmentType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressAssignmentType.setStatus('current')
atIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressRowStatus.setStatus('current')
mibBuilder.exportSymbols("AT-IP-MIB", atIpAddressAssignmentType=atIpAddressAssignmentType, atIpAddressEntry=atIpAddressEntry, atIpAddressRowStatus=atIpAddressRowStatus, atIpAddressAddrType=atIpAddressAddrType, atIpAddressLabel=atIpAddressLabel, atIpMib=atIpMib, AtIpAddressAssignmentType=AtIpAddressAssignmentType, atIpAddressTable=atIpAddressTable, PYSNMP_MODULE_ID=atIpMib, atIpAddressAddr=atIpAddressAddr, atIpAddressIfIndex=atIpAddressIfIndex, atIpAddressPrefixLen=atIpAddressPrefixLen)
