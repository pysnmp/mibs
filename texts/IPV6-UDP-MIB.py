#
# PySNMP MIB module IPV6-UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-UDP-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:27 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Unsigned32, mib_2, iso, Integer32, IpAddress, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Unsigned32", "mib-2", "iso", "Integer32", "IpAddress", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipv6UdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 87))
ipv6UdpMIB.setRevisions(('2017-02-22 00:00', '1998-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipv6UdpMIB.setRevisionsDescriptions(('Obsoleting this MIB module; it has been replaced by\n        the revised UDP-MIB (RFC 4113).', 'First revision, published as RFC 2454',))
if mibBuilder.loadTexts: ipv6UdpMIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6UdpMIB.setOrganization('IETF IPv6 MIB Working Group')
if mibBuilder.loadTexts: ipv6UdpMIB.setContactInfo('               Mike Daniele\n\n                Postal: Compaq Computer Corporation\n                        110 Spitbrook Rd\n                        Nashua, NH 03062.\n                        US\n\n                Phone:  +1 603 884 1423\n                Email:  daniele@zk3.dec.com')
if mibBuilder.loadTexts: ipv6UdpMIB.setDescription("The obsolete MIB module for entities implementing UDP\n        over IPv6.  Use the UDP-MIB instead.\n\n        Copyright (c) 2017 IETF Trust and the persons\n        identified as authors of the code.  All rights reserved.\n\n        Redistribution and use in source and binary forms,\n        with or without modification, is permitted pursuant to,\n        and subject to the license terms contained in, the\n        Simplified BSD License set forth in Section 4.c of the IETF\n        Trust's Legal Provisions Relating to IETF Documents\n        (http://trustee.ietf.org/license-info).")
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
ipv6UdpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 6), )
if mibBuilder.loadTexts: ipv6UdpTable.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpTable.setDescription('A table containing UDP listener information for\n         UDP/IPv6 endpoints.\n\n         This table is obsoleted by UDP-MIB::udpEndpointTable.')
ipv6UdpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 6, 1), ).setIndexNames((0, "IPV6-UDP-MIB", "ipv6UdpLocalAddress"), (0, "IPV6-UDP-MIB", "ipv6UdpLocalPort"), (0, "IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if mibBuilder.loadTexts: ipv6UdpEntry.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpEntry.setDescription('Information about a particular current UDP listener.\n\n         Note that conceptual rows in this table require an\n         additional index object compared to udpTable, since\n         IPv6 addresses are not guaranteed to be unique on the\n         managed node.\n\n         This entry is obsoleted by UDP-MIB::udpEndpointTable.')
ipv6UdpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6UdpLocalAddress.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpLocalAddress.setDescription('The local IPv6 address for this UDP listener.\n         In the case of a UDP listener which is willing\n         to accept datagrams for any IPv6 address\n         associated with the managed node, the value ::0\n         is used.\n\n         This object is obsoleted by UDP-MIB::udpEndpointLocalAddress.')
ipv6UdpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6UdpLocalPort.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpLocalPort.setDescription('The local port number for this UDP listener.\n\n        This object is obsoleted by UDP-MIB::udpEndpointLocalPort.')
ipv6UdpIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 3), Ipv6IfIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6UdpIfIndex.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpIfIndex.setDescription('An index object used to disambiguate conceptual rows in\n         the table, since the ipv6UdpLocalAddress/ipv6UdpLocalPort\n         pair may not be unique.\n\n         This object identifies the local interface that is\n         associated with ipv6UdpLocalAddress for this UDP listener.\n         If such a local interface cannot be determined, this object\n         should take on the value 0.  (A possible example of this\n         would be if the value of ipv6UdpLocalAddress is ::0.)\n\n         The interface identified by a particular non-0 value of\n         this index is the same interface as identified by the same\n         value of ipv6IfIndex.\n\n         The value of this object must remain constant during\n\n         the life of this UDP endpoint.\n\n         This object is obsoleted by the zone identifier in\n         an InetAddressIPv6z address in\n         UDP-MIB::udpEndpointLocalAddress.')
ipv6UdpConformance = MibIdentifier((1, 3, 6, 1, 3, 87, 2))
ipv6UdpCompliances = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 1))
ipv6UdpGroups = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 2))
ipv6UdpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 87, 2, 1, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6UdpCompliance = ipv6UdpCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpCompliance.setDescription('The compliance statement for SNMPv2 entities which\n         implement UDP over IPv6.\n\n         This object is obsoleted by UDP-MIB::udpMIBCompliance2.')
ipv6UdpGroup = ObjectGroup((1, 3, 6, 1, 3, 87, 2, 2, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6UdpGroup = ipv6UdpGroup.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpGroup.setDescription('The group of objects providing management of\n         UDP over IPv6.\n\n         This group is obsoleted by several groups in UDP-MIB.')
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpEntry=ipv6UdpEntry, ipv6UdpCompliance=ipv6UdpCompliance, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpMIB=ipv6UdpMIB, PYSNMP_MODULE_ID=ipv6UdpMIB, ipv6UdpGroups=ipv6UdpGroups, udp=udp, ipv6UdpLocalAddress=ipv6UdpLocalAddress, ipv6UdpConformance=ipv6UdpConformance, ipv6UdpIfIndex=ipv6UdpIfIndex, ipv6UdpTable=ipv6UdpTable, ipv6UdpGroup=ipv6UdpGroup, ipv6UdpCompliances=ipv6UdpCompliances)
