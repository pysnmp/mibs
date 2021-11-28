#
# PySNMP MIB module IPV6-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-TCP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 21:02:38 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, MibIdentifier, Bits, Counter64, experimental, TimeTicks, Counter32, Gauge32, Integer32, NotificationType, mib_2, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "MibIdentifier", "Bits", "Counter64", "experimental", "TimeTicks", "Counter32", "Gauge32", "Integer32", "NotificationType", "mib-2", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipv6TcpMIB = ModuleIdentity((1, 3, 6, 1, 3, 86))
ipv6TcpMIB.setRevisions(('2017-02-22 00:00', '1998-01-29 00:00',))
if mibBuilder.loadTexts: ipv6TcpMIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6TcpMIB.setOrganization('IETF IPv6 MIB Working Group')
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
ipv6TcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 16), )
if mibBuilder.loadTexts: ipv6TcpConnTable.setStatus('obsolete')
ipv6TcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 16, 1), ).setIndexNames((0, "IPV6-TCP-MIB", "ipv6TcpConnLocalAddress"), (0, "IPV6-TCP-MIB", "ipv6TcpConnLocalPort"), (0, "IPV6-TCP-MIB", "ipv6TcpConnRemAddress"), (0, "IPV6-TCP-MIB", "ipv6TcpConnRemPort"), (0, "IPV6-TCP-MIB", "ipv6TcpConnIfIndex"))
if mibBuilder.loadTexts: ipv6TcpConnEntry.setStatus('obsolete')
ipv6TcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6TcpConnLocalAddress.setStatus('obsolete')
ipv6TcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6TcpConnLocalPort.setStatus('obsolete')
ipv6TcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 3), Ipv6Address())
if mibBuilder.loadTexts: ipv6TcpConnRemAddress.setStatus('obsolete')
ipv6TcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6TcpConnRemPort.setStatus('obsolete')
ipv6TcpConnIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 5), Ipv6IfIndexOrZero())
if mibBuilder.loadTexts: ipv6TcpConnIfIndex.setStatus('obsolete')
ipv6TcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 16, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6TcpConnState.setStatus('obsolete')
ipv6TcpConformance = MibIdentifier((1, 3, 6, 1, 3, 86, 2))
ipv6TcpCompliances = MibIdentifier((1, 3, 6, 1, 3, 86, 2, 1))
ipv6TcpGroups = MibIdentifier((1, 3, 6, 1, 3, 86, 2, 2))
ipv6TcpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 86, 2, 1, 1)).setObjects(("IPV6-TCP-MIB", "ipv6TcpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6TcpCompliance = ipv6TcpCompliance.setStatus('obsolete')
ipv6TcpGroup = ObjectGroup((1, 3, 6, 1, 3, 86, 2, 2, 1)).setObjects(("IPV6-TCP-MIB", "ipv6TcpConnState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6TcpGroup = ipv6TcpGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IPV6-TCP-MIB", ipv6TcpGroup=ipv6TcpGroup, ipv6TcpConnLocalAddress=ipv6TcpConnLocalAddress, ipv6TcpConnLocalPort=ipv6TcpConnLocalPort, ipv6TcpConnTable=ipv6TcpConnTable, ipv6TcpConnEntry=ipv6TcpConnEntry, ipv6TcpConnState=ipv6TcpConnState, ipv6TcpGroups=ipv6TcpGroups, ipv6TcpConnRemPort=ipv6TcpConnRemPort, ipv6TcpCompliance=ipv6TcpCompliance, PYSNMP_MODULE_ID=ipv6TcpMIB, ipv6TcpMIB=ipv6TcpMIB, ipv6TcpConformance=ipv6TcpConformance, ipv6TcpConnRemAddress=ipv6TcpConnRemAddress, ipv6TcpCompliances=ipv6TcpCompliances, ipv6TcpConnIfIndex=ipv6TcpConnIfIndex, tcp=tcp)
