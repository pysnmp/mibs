#
# PySNMP MIB module ARISTA-VRF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-VRF-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:35:34 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Unsigned32, Integer32, TimeTicks, Counter32, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaVrfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 18))
aristaVrfMIB.setRevisions(('2015-01-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaVrfMIB.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: aristaVrfMIB.setLastUpdated('201501110000Z')
if mibBuilder.loadTexts: aristaVrfMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaVrfMIB.setContactInfo('Arista Networks, Inc.\n\n         Postal: 5453 Great America Parkway\n                 Santa Clara, CA 95054\n\n         Tel: +1 408 547-5500\n\n         E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaVrfMIB.setDescription('This MIB contains information related to Virtual \n           Routing and Forwarding (VRF).\n           \n           VRF is a mechanism by which a single device can provide\n           independent routing instances. This allows customers to \n           virtually isolate network traffic, and also use overlapping\n           IP addresses.\n\n           Layer3 or routed interfaces in the system will belong to\n           one VRF at a time. The datapath forwarding logic uses the\n           VRF membership of the input interface to determine a\n           specific forwarding table to use for routing the traffic.\n\n           VRF can also be used to isolate management traffic from\n           the rest of the data plane traffic.\n           \n           This MIB module provides the following pieces of\n           information:\n               * A table of all VRFs configured in the system\n               * A table that contains the VRF membership information\n               for all routed interfaces in the system by sparsely\n               augmenting the ifTable.')
aristaVrfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1))
aristaVrfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2))
class VrfName(TextualConvention, OctetString):
    description = 'A human-readable identifier assigned to every VRF. The\n        identifier is unique across all VRFs in the system.'
    status = 'current'
    displayHint = '100t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 100)

class VrfRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = "A route distinguisher as defined in [RFC4364], in the form\n        '<admin>:<local>', where <admin> is the administrator ID\n        (e.g., an AS number) and <local> is the locally assigned\n        number."
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VrfState(TextualConvention, Integer32):
    description = 'The state of a specific VRF. When the administrator\n        configures a VRF on the system, it stays inactive until a\n        route distinguisher is assigned to it. Also, when the\n        administrator deletes a VRF, there can be a small delay\n        before the VRF is completely unconfigured from the system,\n        during which time its status becomes inactive.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

aristaVrfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1), )
if mibBuilder.loadTexts: aristaVrfTable.setStatus('current')
if mibBuilder.loadTexts: aristaVrfTable.setDescription('This table contains information about VRFs currently\n           configured in the system.')
aristaVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1), ).setIndexNames((0, "ARISTA-VRF-MIB", "aristaVrfName"))
if mibBuilder.loadTexts: aristaVrfEntry.setStatus('current')
if mibBuilder.loadTexts: aristaVrfEntry.setDescription('A single row containing information for one VRF that is\n           configured in the system.')
aristaVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 1), VrfName())
if mibBuilder.loadTexts: aristaVrfName.setStatus('current')
if mibBuilder.loadTexts: aristaVrfName.setDescription('The name of the VRF that is represented by this row.')
aristaVrfRoutingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("ipv4", 0), ("ipv6", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfRoutingStatus.setStatus('current')
if mibBuilder.loadTexts: aristaVrfRoutingStatus.setDescription('The current status of data path routing in this VRF.\n           Routing for IPv4 and IPv6 packets can be independently\n           enabled by the administrator for a given VRF. This object\n           carries the routing status for both the protocol versions.\n           If data path routing is enabled for a protocol, the bit\n           for the protocol is 1.')
aristaVrfRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 3), VrfRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: aristaVrfRouteDistinguisher.setDescription('The route distinguisher for this VRF.')
aristaVrfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 4), VrfState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfState.setStatus('current')
if mibBuilder.loadTexts: aristaVrfState.setDescription('The state of the VRF.')
aristaVrfIfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2), )
if mibBuilder.loadTexts: aristaVrfIfTable.setStatus('current')
if mibBuilder.loadTexts: aristaVrfIfTable.setDescription('This table augments the ifTable and contains the \n           VRF membership information for every routed interface\n           in the system. A row is present only for each active\n           routed (or layer3) interface.')
aristaVrfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaVrfIfEntry.setStatus('current')
if mibBuilder.loadTexts: aristaVrfIfEntry.setDescription('VRF membership information for a single routed interface.')
aristaVrfIfMembership = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1, 1), VrfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfIfMembership.setStatus('current')
if mibBuilder.loadTexts: aristaVrfIfMembership.setDescription('The name of the VRF that this routed interface is currently\n           part of.')
aristaVrfMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1))
aristaVrfMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2))
aristaVrfMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1, 1)).setObjects(("ARISTA-VRF-MIB", "aristaVrfInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaVrfMibCompliance = aristaVrfMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaVrfMibCompliance.setDescription('The compliance statement for Arista switches that implement\n        the ARISTA-VRF-MIB.')
aristaVrfInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2, 1)).setObjects(("ARISTA-VRF-MIB", "aristaVrfRoutingStatus"), ("ARISTA-VRF-MIB", "aristaVrfRouteDistinguisher"), ("ARISTA-VRF-MIB", "aristaVrfState"), ("ARISTA-VRF-MIB", "aristaVrfIfMembership"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaVrfInformationGroup = aristaVrfInformationGroup.setStatus('current')
if mibBuilder.loadTexts: aristaVrfInformationGroup.setDescription('The collection of objects that provide VRF information in the\n        system.')
mibBuilder.exportSymbols("ARISTA-VRF-MIB", VrfRouteDistinguisher=VrfRouteDistinguisher, aristaVrfMibConformance=aristaVrfMibConformance, aristaVrfMIB=aristaVrfMIB, aristaVrfEntry=aristaVrfEntry, PYSNMP_MODULE_ID=aristaVrfMIB, aristaVrfState=aristaVrfState, aristaVrfTable=aristaVrfTable, aristaVrfInformationGroup=aristaVrfInformationGroup, VrfName=VrfName, aristaVrfIfTable=aristaVrfIfTable, aristaVrfMibCompliances=aristaVrfMibCompliances, aristaVrfIfEntry=aristaVrfIfEntry, aristaVrfMibObjects=aristaVrfMibObjects, aristaVrfMibGroups=aristaVrfMibGroups, aristaVrfMibCompliance=aristaVrfMibCompliance, aristaVrfRoutingStatus=aristaVrfRoutingStatus, aristaVrfIfMembership=aristaVrfIfMembership, VrfState=VrfState, aristaVrfName=aristaVrfName, aristaVrfRouteDistinguisher=aristaVrfRouteDistinguisher)
