#
# PySNMP MIB module IPV6-UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-UDP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:50:53 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Gauge32, experimental, ObjectIdentity, iso, Integer32, Unsigned32, mib_2, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Gauge32", "experimental", "ObjectIdentity", "iso", "Integer32", "Unsigned32", "mib-2", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipv6UdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 87))
ipv6UdpMIB.setRevisions(('2017-02-22 00:00', '1998-01-29 00:00',))
if mibBuilder.loadTexts: ipv6UdpMIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6UdpMIB.setOrganization('IETF IPv6 MIB Working Group')
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
ipv6UdpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 6), )
if mibBuilder.loadTexts: ipv6UdpTable.setStatus('obsolete')
ipv6UdpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 6, 1), ).setIndexNames((0, "IPV6-UDP-MIB", "ipv6UdpLocalAddress"), (0, "IPV6-UDP-MIB", "ipv6UdpLocalPort"), (0, "IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if mibBuilder.loadTexts: ipv6UdpEntry.setStatus('obsolete')
ipv6UdpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6UdpLocalAddress.setStatus('obsolete')
ipv6UdpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6UdpLocalPort.setStatus('obsolete')
ipv6UdpIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 3), Ipv6IfIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6UdpIfIndex.setStatus('obsolete')
ipv6UdpConformance = MibIdentifier((1, 3, 6, 1, 3, 87, 2))
ipv6UdpCompliances = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 1))
ipv6UdpGroups = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 2))
ipv6UdpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 87, 2, 1, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6UdpCompliance = ipv6UdpCompliance.setStatus('obsolete')
ipv6UdpGroup = ObjectGroup((1, 3, 6, 1, 3, 87, 2, 2, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6UdpGroup = ipv6UdpGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IPV6-UDP-MIB", udp=udp, PYSNMP_MODULE_ID=ipv6UdpMIB, ipv6UdpCompliance=ipv6UdpCompliance, ipv6UdpGroup=ipv6UdpGroup, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpCompliances=ipv6UdpCompliances, ipv6UdpTable=ipv6UdpTable, ipv6UdpIfIndex=ipv6UdpIfIndex, ipv6UdpLocalAddress=ipv6UdpLocalAddress, ipv6UdpGroups=ipv6UdpGroups, ipv6UdpMIB=ipv6UdpMIB, ipv6UdpConformance=ipv6UdpConformance, ipv6UdpEntry=ipv6UdpEntry)
