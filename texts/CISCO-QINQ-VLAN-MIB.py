#
# PySNMP MIB module CISCO-QINQ-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-QINQ-VLAN-MIB
# Source digest sha256:666ad122a4e4f2a34d8637bd5ddd4a5e759280a09894d8b55451c0c68cc0aae0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoQinqVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 445))
ciscoQinqVlanMIB.setRevisions(('2004-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQinqVlanMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setLastUpdated('2004-11-29 00:00')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setContactInfo('            Cisco Systems\n                     Customer Service\n\n             Postal: 170 W Tasman Drive\n                     San Jose, CA  95134\n                     USA\n\n                Tel: +1 800 553-NETS\n\n             E-mail: cs-7600@cisco.com')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setDescription("This MIB defines configuration and monitoring capabilities\n        relating to 802.1QinQ interfaces.  QinQ interfaces are capable\n        of terminating QinQ traffic and translating QinQ tags.\n\n        IEEE 802.1Q VLAN specification provides for an option to tag\n        Ethernet frames with two VLAN tags:\n\n        - An inner tag that specifies the customer's VLAN ID.  This tag\n          is called the 'CE VLAN'.\n\n        - An outer tag that specifies the service provider's VLAN ID.\n          This tag is called the 'metro tag', or the 'PE VLAN'.\n\n        The combination of inner and outer VLAN tags is used to uniquely\n        identify a particular customer's service flow.")
ciscoQinqVlanMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 0))
ciscoQinqVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1))
ciscoQinqVlanMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2))
cqvTermination = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1))
cqvTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2))
class CqvVlanIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC-2674, Bridge MIB Extensions, August 1999, Q-BRIDGE-MIB,\n        E. Bell.'
    description = 'This textual convention is an extension of the VlanId\n        convention.  The VlanId convention defines a greater than zero\n        value to identify a VLAN ID in the managed system.  The\n        CqvVlanIdOrZero convention defines the additional value of\n        zero.  The value zero is object specific and must therefore be\n        defined as part of the description of any object that uses this\n        syntax.  An example of the usage of zero might include\n        situations where the VLAN ID is unknown.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class CqvEncapsulationType(TextualConvention, Integer32):
    description = 'This textual convention defines the different types of VLAN\n        trunking.\n\n        isl - Inter Switch Link, the Cisco proprietary trunking\n        protocol.\n\n        dot1Q - IEEE 802.1Q trunking standard.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isl", 1), ("dot1Q", 2))

cqvTerminationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTerminationTable.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationTable.setDescription("This table contains attributes pertaining to QinQ\n        terminated interfaces.\n\n        The ifIndex in the INDEX clause identifies the interface\n        that terminates QinQ traffic.\n\n        A management application can create a conceptual row in this\n        table by setting the cqvTerminationRowStatus to\n        'createAndWait' or 'createAndGo'.\n\n        A conceptual row in this table cannot be modified while\n        cqvTerminationRowStatus is set to 'active'.")
cqvTerminationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationCeVlanId"))
if mibBuilder.loadTexts: cqvTerminationEntry.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationEntry.setDescription('An entry in this table defines a QinQ terminated interface.')
cqvTerminationPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setDescription('The VLAN ID of the outer tag of a QinQ frame.')
cqvTerminationCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 2), VlanId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setDescription('The VLAN ID of the inner tag of a QinQ frame.')
cqvTerminationPeEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 3), CqvEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationPeEncap.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationPeEncap.setDescription('The encapsulation type of the PE VLAN\n        (cqvTerminationPeVlanId) of a QinQ frame.')
cqvTerminationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationRowStatus.setStatus('current')
if mibBuilder.loadTexts: cqvTerminationRowStatus.setDescription('This object facilitates the creation, modification, or deletion\n        of a conceptual row in this table.')
cqvTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTranslationTable.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationTable.setDescription("This table defines the translations performed on QinQ capable\n        interfaces.\n\n        The ifIndex in the INDEX clause identifies the QinQ interface.\n\n        A QinQ interface performs the following translations:\n\n        - Double Tagged to Single Tagged - the inner and outer tags of\n          the frames internal to the switch are replaced with a single\n          trunk VLAN tag when the outgoing frame is transmitted.\n\n        - Double Tagged to Double Tagged - the outer tag of the frames\n          internal to the switch are replaced with an outer trunk\n          VLAN tag when the outgoing frame is transmitted.  The inner\n          tag remains unchanged in the transmitted frame.\n\n        The following picture illustrates QinQ translations.\n\n               <----- Provider Side -----|----- Customer Side ----->\n\n                     Switch\n        +--------------------------------+\n        |                                |\n        |  +---------------+     +-------|     +------------------+\n        |  | Double Tagged |     |  QinQ |     | Single or Double |\n        |  | Frames        | --> |  Intf | --> | Tagged Frames    |\n        |  +---------------+     +-------|     +------------------+\n        |                                |\n        +--------------------------------+\n\n        Also, the QinQ interface sets the IEEE 802.1P prioritization\n        bits (P bits) in the outgoing frames by copying the P bits\n        either from the internal frame's outer or inner VLAN tag.\n\n        A management application can create a conceptual row in this\n        table by setting the cqvTranslationRowStatus to\n        'createAndWait' or 'createAndGo'.\n\n        A conceptual row in this table cannot be modified while\n        cqvTranslationRowStatus is set to 'active'.")
cqvTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalCeVlanId"))
if mibBuilder.loadTexts: cqvTranslationEntry.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationEntry.setDescription('An entry in this table contains translation information for\n        a particular QinQ interface.')
cqvTranslationInternalPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 1), CqvVlanIdOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setDescription('The QinQ outer VLAN ID of an internal double tagged frame.\n\n        This object will have the value of zero as described in the\n        cqvTranslationType object.')
cqvTranslationInternalCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 2), CqvVlanIdOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setDescription('The QinQ inner VLAN ID of an internal double tagged frame.\n\n        This object will have the value of zero as described in the\n        cqvTranslationType object.')
cqvTranslationTrunkPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 3), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setDescription('The QinQ outer VLAN ID of a trunk VLAN frame.\n\n        This object will have the value of zero as described in the\n        cqvTranslationType object.')
cqvTranslationTrunkCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 4), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setDescription('The QinQ inner VLAN ID of a trunk VLAN frame.\n\n        This object will have the value of zero as described in the\n        cqvTranslationType object.')
cqvTranslationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("doubleToSingle", 1), ("doubleToDouble", 2), ("doubleToDoubleOutOfRange", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationType.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationType.setDescription("The QinQ translation type being performed on the interface.\n\n            'doubleToSingle' - Double tagged to single tagged traffic.\n                               The value of cqvTranslationTrunkPeVlanId\n                               will be zero.  This indicates that the PE\n                               VLAN tag will be absent in the trunk\n                               interface.\n\n            'doubleToDouble' - Double tagged to double tagged traffic.\n                               The value of the internal PE and CE, and\n                               the trunk PE and CE VLAN IDs are\n                               non-zero.\n\n            'doubleToDoubleOutOfRange' - Double tagged to double tagged\n                               traffic that does not have a defined\n                               translation. The value of\n                               cqvTranslationInternalCeVlanId  will be\n                               zero.  This indicates that the CE\n                               VLAN tag is being used as a wildcard.")
cqvTranslationCosPBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copyFromOuterTag", 1), ("copyFromInnerTag", 2))).clone('copyFromOuterTag')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationCosPBits.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationCosPBits.setDescription("This object indicates how the IEEE 802.1P bits (P bits) in the\n        IEEE 802.1Q header of the trunk VLAN are to be set.  The P bits\n        in the trunk VLAN can be set by copying the P bits of the\n        outer PE tag or the inner CE tag.\n\n            'copyFromOuterTag' - Copy the P bits from the outer PE tag.\n\n            'copyFromInnerTag' - Copy the P bits from the inner CE tag.")
cqvTranslationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationRowStatus.setStatus('current')
if mibBuilder.loadTexts: cqvTranslationRowStatus.setDescription('This object facilitates the creation, modification, or deletion\n        of a conceptual row in this table.')
ciscoQinqVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1))
ciscoQinqVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2))
ciscoQinQVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTerminationGroup"), ("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinQVlanMIBCompliance = ciscoQinQVlanMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoQinQVlanMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco\n        QinQ MIB.')
ciscoQinqVlanTerminationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTerminationPeEncap"), ("CISCO-QINQ-VLAN-MIB", "cqvTerminationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTerminationGroup = ciscoQinqVlanTerminationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoQinqVlanTerminationGroup.setDescription('Objects for providing configuration for QinQ termination.')
ciscoQinqVlanTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 2)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkPeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkCeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationType"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationCosPBits"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTranslationGroup = ciscoQinqVlanTranslationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoQinqVlanTranslationGroup.setDescription('Objects for providing configuration for QinQ translation.')
mibBuilder.exportSymbols("CISCO-QINQ-VLAN-MIB", CqvEncapsulationType=CqvEncapsulationType, CqvVlanIdOrZero=CqvVlanIdOrZero, PYSNMP_MODULE_ID=ciscoQinqVlanMIB, ciscoQinQVlanMIBCompliance=ciscoQinQVlanMIBCompliance, ciscoQinqVlanMIB=ciscoQinqVlanMIB, ciscoQinqVlanMIBCompliances=ciscoQinqVlanMIBCompliances, ciscoQinqVlanMIBConform=ciscoQinqVlanMIBConform, ciscoQinqVlanMIBGroups=ciscoQinqVlanMIBGroups, ciscoQinqVlanMIBNotifs=ciscoQinqVlanMIBNotifs, ciscoQinqVlanMIBObjects=ciscoQinqVlanMIBObjects, ciscoQinqVlanTerminationGroup=ciscoQinqVlanTerminationGroup, ciscoQinqVlanTranslationGroup=ciscoQinqVlanTranslationGroup, cqvTermination=cqvTermination, cqvTerminationCeVlanId=cqvTerminationCeVlanId, cqvTerminationEntry=cqvTerminationEntry, cqvTerminationPeEncap=cqvTerminationPeEncap, cqvTerminationPeVlanId=cqvTerminationPeVlanId, cqvTerminationRowStatus=cqvTerminationRowStatus, cqvTerminationTable=cqvTerminationTable, cqvTranslation=cqvTranslation, cqvTranslationCosPBits=cqvTranslationCosPBits, cqvTranslationEntry=cqvTranslationEntry, cqvTranslationInternalCeVlanId=cqvTranslationInternalCeVlanId, cqvTranslationInternalPeVlanId=cqvTranslationInternalPeVlanId, cqvTranslationRowStatus=cqvTranslationRowStatus, cqvTranslationTable=cqvTranslationTable, cqvTranslationTrunkCeVlanId=cqvTranslationTrunkCeVlanId, cqvTranslationTrunkPeVlanId=cqvTranslationTrunkPeVlanId, cqvTranslationType=cqvTranslationType)
