#
# PySNMP MIB module TOKENRING-STATION-SR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source TOKENRING-STATION-SR-MIB
# Source digest sha256:87053e690b155db41906b535b10d10e9b27827368dbd7f7bb0fb6ede269d353b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
dot5SrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 42))
if mibBuilder.loadTexts: dot5SrMIB.setLastUpdated('1994-12-16 10:00')
if mibBuilder.loadTexts: dot5SrMIB.setOrganization('IETF Interfaces MIB Working Group')
if mibBuilder.loadTexts: dot5SrMIB.setContactInfo('       Keith McCloghrie\n            Postal: Cisco Systems, Inc.\n                    170 West Tasman Drive\n                    San Jose, CA  95134-1706\n                    US\n\n             Phone: +1 408 526 5260\n             Email: kzm@cisco.com')
if mibBuilder.loadTexts: dot5SrMIB.setDescription('The MIB module for managing source routes in\n            end-stations on IEEE 802.5 Token Ring networks.')
dot5SrMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 1))
class SourceRoute(TextualConvention, OctetString):
    reference = 'Annex C of ISO/IEC 10038: 1993,\n                 [ANSI/IEEE Std 802.1D, 1993]'
    description = "Represents a Source Route, containing an\n                 embedded sequence of bridge and ring ID's,\n                 as used by 802.5 Source Routing."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

dot5SrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 42, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dot5SrRouteTable.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteTable.setDescription('The table of source-routing routes.\n               This represents the 802.5 RIF database.')
dot5SrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 42, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TOKENRING-STATION-SR-MIB", "dot5SrRouteDestination"))
if mibBuilder.loadTexts: dot5SrRouteEntry.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteEntry.setDescription("Information on a specific route.\n\n                An entry is created whenever a 'Single Path\n                Explorer' or an 'All Paths Explorer' discovers\n                a route to a neighbor not currently in the table,\n                or whenever an 'All Paths Explorer' discovers a\n                better (e.g., shorter) route than the route currently\n                stored in the table.  This is done on behalf of\n                any network layer client.\n\n                The ifIndex value in the INDEX clause refers to\n                the value of MIB-II's ifIndex object for the\n                interface on which the route is in effect.")
dot5SrRouteDestination = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 2), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dot5SrRouteDestination.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteDestination.setDescription('The destination of this route.')
dot5SrRouteControl = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteControl.setReference('Annex C of ISO/IEC 10038: 1993,\n               [ANSI/IEEE Std 802.1D, 1993]')
if mibBuilder.loadTexts: dot5SrRouteControl.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteControl.setDescription('The value of Routing Control field for this\n               route.')
dot5SrRouteDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 4), SourceRoute()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteDescr.setReference('Annex C of ISO/IEC 10038: 1993,\n               [ANSI/IEEE Std 802.1D, 1993]')
if mibBuilder.loadTexts: dot5SrRouteDescr.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteDescr.setDescription("The embedded sequence of bridge and ring ID's\n               for this route.  For destinations on the\n               local ring, the value of this object is\n               the zero-length string.")
dot5SrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot5SrRouteStatus.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteStatus.setDescription("The status of this row.  Values of the instances\n             of dot5SrRouteControl and dot5SrRouteDescr can be\n             modified while the row's status is 'active.")
dot5SrConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2))
dot5SrGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 1))
dot5SrCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 42, 2, 2))
dot5SrCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 42, 2, 2, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrCompliance = dot5SrCompliance.setStatus('current')
if mibBuilder.loadTexts: dot5SrCompliance.setDescription('The compliance statement for SNMPv2 entities\n        which implement the IEEE 802.5 Station Source Route\n        MIB.')
dot5SrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 42, 2, 1, 1)).setObjects(("TOKENRING-STATION-SR-MIB", "dot5SrRouteControl"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteDescr"), ("TOKENRING-STATION-SR-MIB", "dot5SrRouteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot5SrRouteGroup = dot5SrRouteGroup.setStatus('current')
if mibBuilder.loadTexts: dot5SrRouteGroup.setDescription('A collection of objects providing for the management of\n        source routes in stations on IEEE 802.5 source-routing\n        networks.')
mibBuilder.exportSymbols("TOKENRING-STATION-SR-MIB", PYSNMP_MODULE_ID=dot5SrMIB, SourceRoute=SourceRoute, dot5SrCompliance=dot5SrCompliance, dot5SrCompliances=dot5SrCompliances, dot5SrConformance=dot5SrConformance, dot5SrGroups=dot5SrGroups, dot5SrMIB=dot5SrMIB, dot5SrMIBObjects=dot5SrMIBObjects, dot5SrRouteControl=dot5SrRouteControl, dot5SrRouteDescr=dot5SrRouteDescr, dot5SrRouteDestination=dot5SrRouteDestination, dot5SrRouteEntry=dot5SrRouteEntry, dot5SrRouteGroup=dot5SrRouteGroup, dot5SrRouteStatus=dot5SrRouteStatus, dot5SrRouteTable=dot5SrRouteTable)
