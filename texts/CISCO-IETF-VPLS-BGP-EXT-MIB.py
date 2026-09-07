#
# PySNMP MIB module CISCO-IETF-VPLS-BGP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-VPLS-BGP-EXT-MIB
# Source digest sha256:301fff8ebf89c0f268788d5d20016cf3992000d85c854b8a5d89ec658047fb4b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cvplsConfigIndex, cvplsPwBindIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex", "cvplsPwBindIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention")
ciscoIetfVplsBgpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 140))
ciscoIetfVplsBgpExtMIB.setRevisions(('2008-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setLastUpdated('2008-10-24 00:00')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-l2vpn@cisco.com')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIB.setDescription('This MIB module enables the use of any underlying Pseudo Wire network.\n\n        This MIB extends the MIB module published in the RFC 4188 to manage\n        object definitions for BGP signalled VPLS.\n\n                              GLOSSARY\n        PE \n        The term PE refers to Provider-Edge devices.\n\n        Pseudo Wire\n        An emulation of a native service over a Packet Switched Network. \n\n        RD (Route Distinguisher)\n        They are used to create VPN-IPv4 addresses, as specified in [RFC4364].\n\n        RT (Route Target)\n        A Route Target attribute can be thought of as identifying a set of\n        sites. More description specified in [RFC4364].\n\n        u-PE\n        A Layer 2 PE device used for Layer 2 aggregation. The notion of u-PE is \n        described further in [RFC4761].\n\n        VE\n        The term VE refers to a VPLS Edge device, which could be either\n        a PE or a u-PE.\n\n        VPLS\n        Virtual private LAN service. A type of layer 2 VPN.')
class CiVplsBgpExtRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = 'This textual convention represents a Route Distinguisher.\n        Please refer to RFC 4364 for more details about the \n        Route Distinguisher. Please refer to draft-ietf-l2vpn-vpls-bgp-08 \n        on the use of a Route Distinguisher for a VPLS.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    description = 'This textual convention represents a Route Target.\n        Please refer to RFC 4364 for more details about the \n        Route Target. Please refer to draft-ietf-l2vpn-vpls-bgp-08 \n        on the use of a Route Target for a VPLS.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiVplsBgpExtRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC 4364]'
    description = 'This textual convention represents the type of a route target usage.\n        Route targets can be specified to be imported, exported, or both.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

class CiVplsBgpExtVEID(TextualConvention, Unsigned32):
    description = 'This textual convention represents a VE id.'
    status = 'current'

ciscoIetfVplsBgpExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 0))
ciscoIetfVplsBgpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 1))
ciscoIetfVplsBgpExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2))
ciVplsBgpExtConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciVplsBgpExtConfigTable.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigTable.setDescription('This table specifies information for configuring\n        and monitoring BGP-specific parameters for VPLS.\n\n        A row is automatically created when a VPLS is\n        configured using BGP signalling.\n\n        None of the read-write objects values can be\n        changed when cvplsConfigRowStatus is in the active(1)\n        state. Changes are allowed when the cvplsConfigRowStatus\n        is in notInService(2) or notReady(3) states only.\n        If the operator need to change one of the values\n        for an active row the cvplsConfigRowStatus should be\n        first changed to notInService(2), the objects may\n        be changed now, and later to active(1) in order to\n        re-initiate the signaling process with the new\n        values in effect.')
ciVplsBgpExtConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigEntry.setDescription('Each Entry represents a conceptual row in ciVplsBgpExtConfigTable\n        and provides the information about BGP-specific information\n        for VPLS in a packet network.')
ciVplsBgpExtConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 1), CiVplsBgpExtRouteDistinguisher().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigRouteDistinguisher.setDescription('This object represents the Route Distingiusher for this VPLS.')
ciVplsBgpExtConfigVERangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciVplsBgpExtConfigVERangeSize.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigVERangeSize.setDescription('This object represents the size of the range of VE identifiers in this VPLS.\n        This number controls the size of the label block advertised for this \n        VE by the PE.\n        A value of 0 indicates that the range is not configured and the PE \n        derives the range value from received advertisements from other PEs.')
civplsBgpExtRTTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: civplsBgpExtRTTable.setStatus('current')
if mibBuilder.loadTexts: civplsBgpExtRTTable.setDescription('This table specifies information for the list of RTs imported or \n         exported by BGP during auto-discovery of VPLS.')
civplsBgpExtRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"))
if mibBuilder.loadTexts: civplsBgpExtRTEntry.setStatus('current')
if mibBuilder.loadTexts: civplsBgpExtRTEntry.setDescription('Each Entry represents a conceptual row in civplsBgpExtRTTable\n        and provides the information about the value of the RT being used by BGP. \n        Depending on the value of civplsBgpExtRTType, an RT might be exported or\n        imported or both. Every VPLS, which uses auto-discovery for finding peer \n        nodes, can import and export multiple RTs. This representation allows \n        support for hierarchical VPLS. A row is created by the operator or agent \n        prior to autodiscovery.')
ciVplsBgpExtRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 1), CiVplsBgpExtRouteTargetType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTType.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTType.setDescription('This object represents the type of a RT usage. RTs can be specified \n        to be imported, exported, or both.')
ciVplsBgpExtRT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 2), CiVplsBgpExtRouteTarget().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRT.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRT.setDescription('The RT associated with the VPLS service.')
ciVplsBgpExtRTStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTStorageType.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTStorageType.setDescription('This object indicates the storage type for this row.')
ciVplsBgpExtRTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtRTRowStatus.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTRowStatus.setDescription('This object is used to create, modify, and/or\n        delete a row in this table.  When a row in this\n        table is in active(1) state, no objects in that row\n        can be modified.')
ciVplsBgpExtVETable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciVplsBgpExtVETable.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVETable.setDescription('This table associates VPLS Edge devices to a VPLS.\n        The VEs assigned to a VPLS can be configured on a PE.\n        This table has an expansion dependant relationship \n        with cvplsConfigTable. For each row identified by \n        cvplsConfigIndex, there may exist one or more rows \n        in this table. ciVplsBgpExtVEId is the expansion index. \n\n        None of the read-create objects values can be\n        changed when ciVplsBgpExtVERowStatus is in the active(1)\n        state. Changes are allowed when the ciVplsBgpExtVERowStatus\n        is in notInService(2) or notReady(3) states only.\n        If the operator need to change one of the values\n        for an active row the ciVplsBgpExtVERowStatus should be\n        first changed to notInService(2), the objects may\n        be changed now, and later to active(1) in order to\n        re-initiate the signaling process with the new\n        values in effect.')
ciVplsBgpExtVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEId"))
if mibBuilder.loadTexts: ciVplsBgpExtVEEntry.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEEntry.setDescription('Each Entry represents a conceptual row in ciVplsBgpExtVETable\n        and provides the information about VPLS Edge devices.')
ciVplsBgpExtVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 1), CiVplsBgpExtVEID()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciVplsBgpExtVEId.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEId.setDescription('This object identifies a VE associated with a VPLS.')
ciVplsBgpExtVEName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 2), SnmpAdminString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEName.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEName.setDescription('This object represents the name of the site or u-PE associated with this VE.')
ciVplsBgpExtVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEPreference.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEPreference.setDescription('This object represents the preference of the VE if the site is multi-homed and VE Id is used.')
ciVplsBgpExtVEStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVEStorageType.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEStorageType.setDescription('This object indicates the storage type for this row.')
ciVplsBgpExtVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciVplsBgpExtVERowStatus.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVERowStatus.setDescription('This object is used to create, modify, and/or\n        delete a row in this table.  When a row in this\n        table is in active(1) state, no objects in that row\n        can be modified.')
ciVplsBgpExtPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindTable.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindTable.setDescription('This table provides BGP-specific information for\n        an association between a VPLS and the \n        corresponding Pseudo Wires. A service can have more\n        than one Pseudo Wire association. Pseudo Wires are\n        defined in the cpwvcTable.\n\n        Each row represents an association between a VPLS instance \n        and one or more Pseudo Wires defined in the cpwVcTable in \n        CISCO-IETF-PW-MIB. \n\n        An Entry in this table in instantiated only when\n        BGP signalling is used to configure VPLS.')
ciVplsBgpExtPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: ciVplsBgpExtPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindEntry.setDescription('Each Entry represents a conceptual row in ciVplsBgpExtPwBindTable\n        and provides the information about BGP-specific information for\n        an association between a VPLS and the \n        corresponding Pseudo Wires.')
ciVplsBgpExtPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 1), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindLocalVEId.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindLocalVEId.setDescription('This object represents the local VE this Pseudo Wire is associated with.')
ciVplsBgpExtPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 2), CiVplsBgpExtVEID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciVplsBgpExtPwBindRemoteVEId.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindRemoteVEId.setDescription('This object represents the remote VE this Pseudo Wire is associated with.')
ciscoIetfVplsBgpExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1))
ciscoIetfVplsBgpExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2))
ciscoIetfVplsBgpExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEGroup"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfVplsBgpExtMIBCompliance = ciscoIetfVplsBgpExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfVplsBgpExtMIBCompliance.setDescription('Compliance statement for the entities that implement\n        the ciscoIetfVplsBgpExtMIB module.')
ciVplsBgpExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigRouteDistinguisher"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigVERangeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtConfigGroup = ciVplsBgpExtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtConfigGroup.setDescription('This group of objects help to configure L2VPN  VPLS using BGP.')
ciVplsBgpExtRTGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 2)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTStorageType"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtRTGroup = ciVplsBgpExtRTGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtRTGroup.setDescription('The group of objects help to manage RTs\n        for L2VPN VPLS using BGP.')
ciVplsBgpExtVEGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 3)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEName"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEPreference"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVERowStatus"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtVEGroup = ciVplsBgpExtVEGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtVEGroup.setDescription('The group of objects help to manage VE devices\n        for L2VPN VPLS using BGP.')
ciVplsBgpExtPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 4)).setObjects(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindLocalVEId"), ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindRemoteVEId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciVplsBgpExtPwBindGroup = ciVplsBgpExtPwBindGroup.setStatus('current')
if mibBuilder.loadTexts: ciVplsBgpExtPwBindGroup.setDescription('The group of objects help to manage\n        Pseudo Wires for L2VPN VPLS using BGP.')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-BGP-EXT-MIB", CiVplsBgpExtRouteDistinguisher=CiVplsBgpExtRouteDistinguisher, CiVplsBgpExtRouteTarget=CiVplsBgpExtRouteTarget, CiVplsBgpExtRouteTargetType=CiVplsBgpExtRouteTargetType, CiVplsBgpExtVEID=CiVplsBgpExtVEID, PYSNMP_MODULE_ID=ciscoIetfVplsBgpExtMIB, ciVplsBgpExtConfigEntry=ciVplsBgpExtConfigEntry, ciVplsBgpExtConfigGroup=ciVplsBgpExtConfigGroup, ciVplsBgpExtConfigRouteDistinguisher=ciVplsBgpExtConfigRouteDistinguisher, ciVplsBgpExtConfigTable=ciVplsBgpExtConfigTable, ciVplsBgpExtConfigVERangeSize=ciVplsBgpExtConfigVERangeSize, ciVplsBgpExtPwBindEntry=ciVplsBgpExtPwBindEntry, ciVplsBgpExtPwBindGroup=ciVplsBgpExtPwBindGroup, ciVplsBgpExtPwBindLocalVEId=ciVplsBgpExtPwBindLocalVEId, ciVplsBgpExtPwBindRemoteVEId=ciVplsBgpExtPwBindRemoteVEId, ciVplsBgpExtPwBindTable=ciVplsBgpExtPwBindTable, ciVplsBgpExtRT=ciVplsBgpExtRT, ciVplsBgpExtRTGroup=ciVplsBgpExtRTGroup, ciVplsBgpExtRTRowStatus=ciVplsBgpExtRTRowStatus, ciVplsBgpExtRTStorageType=ciVplsBgpExtRTStorageType, ciVplsBgpExtRTType=ciVplsBgpExtRTType, ciVplsBgpExtVEEntry=ciVplsBgpExtVEEntry, ciVplsBgpExtVEGroup=ciVplsBgpExtVEGroup, ciVplsBgpExtVEId=ciVplsBgpExtVEId, ciVplsBgpExtVEName=ciVplsBgpExtVEName, ciVplsBgpExtVEPreference=ciVplsBgpExtVEPreference, ciVplsBgpExtVERowStatus=ciVplsBgpExtVERowStatus, ciVplsBgpExtVEStorageType=ciVplsBgpExtVEStorageType, ciVplsBgpExtVETable=ciVplsBgpExtVETable, ciscoIetfVplsBgpExtMIB=ciscoIetfVplsBgpExtMIB, ciscoIetfVplsBgpExtMIBCompliance=ciscoIetfVplsBgpExtMIBCompliance, ciscoIetfVplsBgpExtMIBCompliances=ciscoIetfVplsBgpExtMIBCompliances, ciscoIetfVplsBgpExtMIBConform=ciscoIetfVplsBgpExtMIBConform, ciscoIetfVplsBgpExtMIBGroups=ciscoIetfVplsBgpExtMIBGroups, ciscoIetfVplsBgpExtMIBNotifs=ciscoIetfVplsBgpExtMIBNotifs, ciscoIetfVplsBgpExtMIBObjects=ciscoIetfVplsBgpExtMIBObjects, civplsBgpExtRTEntry=civplsBgpExtRTEntry, civplsBgpExtRTTable=civplsBgpExtRTTable)
