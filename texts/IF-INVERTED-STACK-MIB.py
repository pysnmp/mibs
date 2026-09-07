#
# PySNMP MIB module IF-INVERTED-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source IF-INVERTED-STACK-MIB
# Source digest sha256:fc47b49328c3e9f9878e995878f4b5c8702b122185b20261f3efde74ee0a02b4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifStackGroup2, ifStackHigherLayer, ifStackLowerLayer = mibBuilder.importSymbols("IF-MIB", "ifStackGroup2", "ifStackHigherLayer", "ifStackLowerLayer")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ifInvertedStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 77))
ifInvertedStackMIB.setRevisions(('2000-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ifInvertedStackMIB.setRevisionsDescriptions(('Initial revision, published as RFC 2864',))
if mibBuilder.loadTexts: ifInvertedStackMIB.setLastUpdated('2000-06-14 00:00')
if mibBuilder.loadTexts: ifInvertedStackMIB.setOrganization('IETF Interfaces MIB Working Group')
if mibBuilder.loadTexts: ifInvertedStackMIB.setContactInfo('   Keith McCloghrie\n              Cisco Systems, Inc.\n              170 West Tasman Drive\n              San Jose, CA  95134-1706\n              US\n\n              408-526-5260\n              kzm@cisco.com')
if mibBuilder.loadTexts: ifInvertedStackMIB.setDescription('The MIB module which provides the Inverted Stack Table for\n          interface sub-layers.')
ifInvMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1))
ifInvStackTable = MibTable((1, 3, 6, 1, 2, 1, 77, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ifInvStackTable.setReference('ifStackTable of RFC 2863')
if mibBuilder.loadTexts: ifInvStackTable.setStatus('current')
if mibBuilder.loadTexts: ifInvStackTable.setDescription("A table containing information on the relationships between\n          the multiple sub-layers of network interfaces.  In\n          particular, it contains information on which sub-layers run\n          'underneath' which other sub-layers, where each sub-layer\n          corresponds to a conceptual row in the ifTable.  For\n          example, when the sub-layer with ifIndex value x runs\n          underneath the sub-layer with ifIndex value y, then this\n          table contains:\n\n            ifInvStackStatus.x.y=active\n\n          For each ifIndex value, z, which identifies an active\n          interface, there are always at least two instantiated rows\n          in this table associated with z.  For one of these rows, z\n          is the value of ifStackHigherLayer; for the other, z is the\n          value of ifStackLowerLayer.  (If z is not involved in\n          multiplexing, then these are the only two rows associated\n          with z.)\n\n          For example, two rows exist even for an interface which has\n          no others stacked on top or below it:\n\n            ifInvStackStatus.z.0=active\n            ifInvStackStatus.0.z=active\n\n          This table contains exactly the same number of rows as the\n          ifStackTable, but the rows appear in a different order.")
ifInvStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 77, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvStackEntry.setStatus('current')
if mibBuilder.loadTexts: ifInvStackEntry.setDescription('Information on a particular relationship between two sub-\n          layers, specifying that one sub-layer runs underneath the\n          other sub-layer.  Each sub-layer corresponds to a conceptual\n          row in the ifTable.')
ifInvStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvStackStatus.setStatus('current')
if mibBuilder.loadTexts: ifInvStackStatus.setDescription('The status of the relationship between two sub-layers.\n\n          An instance of this object exists for each instance of the\n          ifStackStatus object, and vice versa.  For example, if the\n          variable ifStackStatus.H.L exists, then the variable\n          ifInvStackStatus.L.H must also exist, and vice versa.  In\n          addition, the two variables always have the same value.\n\n          However, unlike ifStackStatus, the ifInvStackStatus object\n          is NOT write-able.  A network management application wishing\n          to change a relationship between sub-layers H and L cannot\n          do so by modifying the value of ifInvStackStatus.L.H, but\n          must instead modify the value of ifStackStatus.H.L.  After\n          the ifStackTable is modified, the change will be reflected\n          in this table.')
ifInvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2))
ifInvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 1))
ifInvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 2))
ifInvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"), ("IF-MIB", "ifStackGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvCompliance = ifInvCompliance.setStatus('current')
if mibBuilder.loadTexts: ifInvCompliance.setDescription('The compliance statement for SNMP entities which provide\n          inverted information on the layering of network interfaces.')
ifInvStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvStackGroup = ifInvStackGroup.setStatus('current')
if mibBuilder.loadTexts: ifInvStackGroup.setDescription('A collection of objects providing inverted information on\n          the layering of MIB-II interfaces.')
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", PYSNMP_MODULE_ID=ifInvertedStackMIB, ifInvCompliance=ifInvCompliance, ifInvCompliances=ifInvCompliances, ifInvConformance=ifInvConformance, ifInvGroups=ifInvGroups, ifInvMIBObjects=ifInvMIBObjects, ifInvStackEntry=ifInvStackEntry, ifInvStackGroup=ifInvStackGroup, ifInvStackStatus=ifInvStackStatus, ifInvStackTable=ifInvStackTable, ifInvertedStackMIB=ifInvertedStackMIB)
