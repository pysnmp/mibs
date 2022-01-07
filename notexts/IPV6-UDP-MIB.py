#
# PySNMP MIB module IPV6-UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-UDP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:30:22 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
Ipv6Address, Ipv6IfIndexOrZero = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6IfIndexOrZero")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, experimental, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, Gauge32, iso, Integer32, NotificationType, Counter64, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "experimental", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Gauge32", "iso", "Integer32", "NotificationType", "Counter64", "IpAddress", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpMIB=ipv6UdpMIB, ipv6UdpCompliances=ipv6UdpCompliances, ipv6UdpGroup=ipv6UdpGroup, ipv6UdpIfIndex=ipv6UdpIfIndex, PYSNMP_MODULE_ID=ipv6UdpMIB, ipv6UdpConformance=ipv6UdpConformance, ipv6UdpLocalAddress=ipv6UdpLocalAddress, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpGroups=ipv6UdpGroups, ipv6UdpTable=ipv6UdpTable, ipv6UdpCompliance=ipv6UdpCompliance, udp=udp, ipv6UdpEntry=ipv6UdpEntry)
