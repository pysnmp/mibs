#
# PySNMP MIB module ARISTA-NEXTHOP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-NEXTHOP-GROUP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 13:05:20 2023
# On host fv-az574-39 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Integer32, MibIdentifier, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, IpAddress, ModuleIdentity, iso, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Integer32", "MibIdentifier", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaNexthopGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 21))
aristaNexthopGroupMIB.setRevisions(('2016-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaNexthopGroupMIB.setRevisionsDescriptions(('Initial revision of the MIB module.',))
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setLastUpdated('201604170000Z')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setContactInfo('Arista Networks, Inc.\n\n         Postal: 5453 Great America Parkway\n                 Santa Clara, CA 95054\n\n         Tel: +1 408 547-5500\n\n         E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setDescription("This MIB contains information about NextHop Groups (NHG).\n            \n            General L3 routing creates routing table entries, each of\n            which are associated with a nexthop. If multiple paths\n            exist for a specific route, the route points to a set of\n            nexthops (commonly referred as ECMP or Equal Cost\n            MultiPath).\n\n            Arista devices support a feature which allows customers to\n            manually create a nexthop list, and use this list to\n            route packets to the specified set of nexthop\n            addresses. Customers can associate a tunnel type (GRE,\n            for example) with the nexthop group, allowing relevant\n            packets to be tunneled as well. The packet forwarding or\n            routing decision happens in hardware. \n\n            Nexthop group feature gives customers full control of how\n            a route should be forwarded (tunneled or otherwise). The\n            number of entries in the nexthop group is also determined\n            by the user, and directly translates to the number of\n            nexthop entries in the hardware for the specified route.\n\n            Let's provide an example, looking at EOS CLI example.\n\n            nexthop-group foo type ip-in-ip\n              ttl 64 \n              entry 0 tunnel-destination 10.1.1.1 \n              entry 1 tunnel-destination 20.1.1.1 \n            !\n            ip route 30.1.1.0/24 Nexthop-Group foo\n\n            In the above configuration, any packet destined to\n            30.1.1.0/24 will be forwarded by the nexthop group\n            'foo'. Each entry inside the nexthop group specifies a\n            particular nexthop ('tunnel destination') chosen by the\n            customer. In this example, packets can be forwarded via\n            either of the nexthop (traffic split equally between the 2\n            entries).\n\n            This MIB module provides information relevant to the\n            nexthop group feature, specifically the status of various\n            nexthop groups configured, and traffic statistics.")
aristaNexthopGroupMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1))
aristaNexthopGroupMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2))
class NexthopGroupName(TextualConvention, OctetString):
    description = 'Each nexthop group configured by the user is associated with\n        a name, by configuration.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NexthopGroupType(TextualConvention, Integer32):
    description = "A nexthop group is associated with a type, which determines\n        the packet forwarding behavior. \n\n        Type 'ip' refers to L3 IP routing. A route pointing to a\n        nexthop group in this case is equivalent to multiple static\n        route configuration entries each with a particular nexthop.\n        \n        Types 'gre', 'mpls', 'ip-in-ip' all refer to tunnel types. In\n        this case a route pointing to the specified nexthop group is\n        used to tunnel packets using the appropriate encapsulation to\n        a tunnel destination. The encapsulation information depends on\n        the tunnel type itself."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("ipInIp", 1), ("gre", 2), ("mpls", 3), ("ip", 4), ("mplsOverGre", 5))

aristaNexthopGroupTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1), )
if mibBuilder.loadTexts: aristaNexthopGroupTable.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupTable.setDescription('This table contains information about the nexthop groups\n        that are present in the device.')
aristaNexthopGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1), ).setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"))
if mibBuilder.loadTexts: aristaNexthopGroupEntry.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupEntry.setDescription('A conceptual row, containing information for a specific\n        nexthop group.')
aristaNexthopGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaNexthopGroupId.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupId.setDescription('Unique index identifying a nexthop group.')
aristaNexthopGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 2), NexthopGroupName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupName.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupName.setDescription('Unique name identifying a nexthop group.')
aristaNexthopGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 3), NexthopGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupType.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupType.setDescription('The type of the nexthop group. The encapsulation information\n        provided for each entry in the nexthop group corresponds to\n        the type.')
aristaNexthopGroupCounterTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2), )
if mibBuilder.loadTexts: aristaNexthopGroupCounterTable.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterTable.setDescription('Each nexthop group contains several entries - each\n        entry specifies a particular nexthop through which a packet\n        can be forwarded. There is packet and byte counter information\n        associated with each such nexthop. \n\n        This table represents the per nexthop counter information for\n        every nexthop group.')
aristaNexthopGroupCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1), ).setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"), (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupEntryIndex"))
if mibBuilder.loadTexts: aristaNexthopGroupCounterEntry.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterEntry.setDescription('A conceptual row, containing counter information for every\n        nexthop defined inside the nexthop group.')
aristaNexthopGroupEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaNexthopGroupEntryIndex.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupEntryIndex.setDescription("As described in the beginning of the MIB module each nexthop\n        group can have multiple entries, one per 'destination' or\n        'nexthop'. Each entry within a nexthop group has a number or\n        index as configured by the user. This MIB object represents\n        the entry index within the nexthop group.")
aristaNexthopGroupCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterIndex.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterIndex.setDescription('For every nexthop within a nexthop group, packet and byte\n        counters are maintained by the device. Counters can be shared\n        by multiple such nexthops and the counter index will be the\n        same for all of those nexthops.')
aristaNexthopGroupCounterPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterPacketCount.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterPacketCount.setDescription('The number of packets forwarded through the specific\n        nexthop. Note that since counters are shared with multiple\n        nexthops, the packet count is an aggregate of packets\n        forwarded through all the relevant nexthops.')
aristaNexthopGroupCounterByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterByteCount.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterByteCount.setDescription('The byte count of packets forwarded through the specific\n        nexthop. Note that since counters are shared with multiple\n        nexthops, the byte count is an aggregate of packets\n        forwarded through all the relevant nexthops.')
aristaNexthopGroupMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1))
aristaNexthopGroupMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2))
aristaNexthopGroupMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupGroup"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupMibCompliance = aristaNexthopGroupMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupMibCompliance.setDescription('The compliance statement for Arista switches that implement\n        the ARISTA-NEXTHOP-GROUP-MIB.')
aristaNexthopGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupName"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupGroup = aristaNexthopGroupGroup.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupGroup.setDescription('The collection of objects that provide nexthop group\n        information in the system.')
aristaNexthopGroupCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 2)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterIndex"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterPacketCount"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterByteCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupCounterGroup = aristaNexthopGroupCounterGroup.setStatus('current')
if mibBuilder.loadTexts: aristaNexthopGroupCounterGroup.setDescription('The collection of objects that provide counter information\n        for every nexthop in the nexthop group.')
mibBuilder.exportSymbols("ARISTA-NEXTHOP-GROUP-MIB", aristaNexthopGroupMIB=aristaNexthopGroupMIB, PYSNMP_MODULE_ID=aristaNexthopGroupMIB, aristaNexthopGroupCounterTable=aristaNexthopGroupCounterTable, aristaNexthopGroupMibGroups=aristaNexthopGroupMibGroups, aristaNexthopGroupCounterGroup=aristaNexthopGroupCounterGroup, NexthopGroupType=NexthopGroupType, aristaNexthopGroupCounterIndex=aristaNexthopGroupCounterIndex, aristaNexthopGroupMibConformance=aristaNexthopGroupMibConformance, aristaNexthopGroupMibObjects=aristaNexthopGroupMibObjects, aristaNexthopGroupId=aristaNexthopGroupId, aristaNexthopGroupName=aristaNexthopGroupName, aristaNexthopGroupCounterByteCount=aristaNexthopGroupCounterByteCount, aristaNexthopGroupMibCompliance=aristaNexthopGroupMibCompliance, aristaNexthopGroupEntryIndex=aristaNexthopGroupEntryIndex, aristaNexthopGroupCounterEntry=aristaNexthopGroupCounterEntry, aristaNexthopGroupTable=aristaNexthopGroupTable, aristaNexthopGroupEntry=aristaNexthopGroupEntry, aristaNexthopGroupMibCompliances=aristaNexthopGroupMibCompliances, aristaNexthopGroupType=aristaNexthopGroupType, aristaNexthopGroupGroup=aristaNexthopGroupGroup, aristaNexthopGroupCounterPacketCount=aristaNexthopGroupCounterPacketCount, NexthopGroupName=NexthopGroupName)
