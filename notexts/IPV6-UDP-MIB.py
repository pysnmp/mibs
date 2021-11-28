#
# PySNMP MIB module IPV6-UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-UDP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:23:23 2021
# On host fv-az36-794 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Counter64, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, ObjectIdentity, experimental, Bits, mib_2, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "experimental", "Bits", "mib-2", "iso", "TimeTicks", "Integer32")
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
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpTable=ipv6UdpTable, ipv6UdpMIB=ipv6UdpMIB, ipv6UdpGroups=ipv6UdpGroups, ipv6UdpCompliance=ipv6UdpCompliance, ipv6UdpCompliances=ipv6UdpCompliances, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpEntry=ipv6UdpEntry, ipv6UdpConformance=ipv6UdpConformance, PYSNMP_MODULE_ID=ipv6UdpMIB, ipv6UdpGroup=ipv6UdpGroup, ipv6UdpLocalAddress=ipv6UdpLocalAddress, udp=udp, ipv6UdpIfIndex=ipv6UdpIfIndex)
