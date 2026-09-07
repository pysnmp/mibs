#
# PySNMP MIB module CISCO-WAN-ATM-PARTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-ATM-PARTY-MIB
# Source digest sha256:1c751f1b2fb67edcdf6a64d03eeecd456834218bec6dc208974b7cca27822a35
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoWanAtmPartyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99998))
ciscoWanAtmPartyMIB.setRevisions(('2002-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setRevisionsDescriptions(('Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setLastUpdated('2002-06-17 00:00')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setContactInfo('               Cisco Systems\n                        Customer Service\n\n                        Postal: 170 W Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n                        E-mail: cs-wanatm@cisco.com\n        ')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setDescription("A management station can use this MIB to provision,\n        manage or delete one or more 'parties' on an ATM\n        point-to-multipoint Soft PVCC(SPVC) connection. \n\n        The user must add a root endpoint to the managed system \n        before proceed to add one or more 'parties' to the root.\n        The provision and management of a 'root' endpoint is \n        beyond the scope of this MIB. Please refer to \n        CISCO-WAN-ATM-CONN-MIB.my for the provisioning and\n        management of a 'root' endpoint.\n\n        This MIB is based on 'ITU-T recommendation Q.2971 (10/95) \n        BROADBAND INTEGRATED SERVICES DIGITAL NETWORK (B-ISDN)\n        - DIGITAL SUBSCRIBER SIGNALLING SYSTEM No. 2 (DSS 2) -\n        USER-NETWORK INTERFACE LAYER 3 SPECIFICATION FOR POINT-\n        TO-MULTIPOINT CALL/CONNECTION CONTROL")
ciscoWanAtmPartyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 0))
ciscoWanAtmPartyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1))
cwapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1))
ciscoWanAtmPartyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2))
class WanPartyAdminStatus(TextualConvention, Integer32):
    description = "Defines 'administrative status' of a 'party'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WanPartyOperStatus(TextualConvention, Integer32):
    description = "Defines 'operational status' of a 'party'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fail", 2))

class WanNsapAtmAddress(TextualConvention, OctetString):
    description = 'ATM address used by the managed system. The only\n        address type presently supported is ATM Network Service\n        Access Point (NSAP) addresses (20 octets).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

cwapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapConfigTable.setStatus('current')
if mibBuilder.loadTexts: cwapConfigTable.setDescription("This table contains mandatory 'party' configuration\n        for all ATM point-to-multipoint Soft Permanent Virtual\n        Channel Connections (SPVC).\n        ")
cwapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVpi"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVci"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapReference"))
if mibBuilder.loadTexts: cwapConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cwapConfigEntry.setDescription("An entry in the 'cwapConfigTable'. Each entry\n        corresponds to one party of a point-to-multipoint\n        connection.\n\n        (1) To add an entry, the management \n        application must first provision a 'root' endpoint. \n\n        (2) While adding an entry, the variables\n        'cwapNSAPAddress', 'cwapVpi' and 'cwapVci' are \n        mandatory. The 'cwapNSAPAddress', 'csapVpi'  \n        and 'cwapVci' are not required to be unique.  \n        \n        (3) The row creation will fail if the root endpoint does \n        not exist.\n\n        (4) The following management operations are permitted on\n        a row when the 'cwapRowStatus' is 'active':\n            a) row deletion.\n            b) toggling of the administrative status of a 'party'\n               via the 'cwapAdminStatus' object. \n            c) triggering a reroute via the 'cwapReroute' object.\n\n        (5) The table index 'ifIndex' refers to that of the root.\n        The 'ifIndex' identifies an ATM Virtual Interface\n        ('ifType' atmVirtual(149)). \n        ")
cwapRootVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapRootVpi.setStatus('current')
if mibBuilder.loadTexts: cwapRootVpi.setDescription('This object identifies the Virtual Path\n        Identifier(VPI) of the root endpoint\n        this party is associated with.')
cwapRootVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapRootVci.setStatus('current')
if mibBuilder.loadTexts: cwapRootVci.setDescription('This object identifies the Virtual \n        Channel Identifier (VCI) of the root \n        endpoint this party is associated with.')
cwapReference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapReference.setStatus('current')
if mibBuilder.loadTexts: cwapReference.setDescription('An arbitrary integer which serves to distinguish\n        between the multiple parties attached to a root of\n        a point-to-multipoint SPVC.')
cwapNSAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 4), WanNsapAtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapNSAPAddress.setStatus('current')
if mibBuilder.loadTexts: cwapNSAPAddress.setDescription('The ATM NSAP address of this party.')
cwapVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVpi.setStatus('current')
if mibBuilder.loadTexts: cwapVpi.setDescription('The VPI value of this party.')
cwapVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVci.setStatus('current')
if mibBuilder.loadTexts: cwapVci.setDescription('The VCI value of this party.')
cwapReroute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapReroute.setStatus('current')
if mibBuilder.loadTexts: cwapReroute.setDescription("The management station uses this object to trigger the\n        re-routing of the party.\n\n        * Rerouting takes effect, when this object is set to true(1).\n          When set to false(2), no action is taken.\n\n        * The value 'false' will always be returned on snmp query\n          to this variable. \n\n        * During reroute operation, the 'cwapOperStatus' will contain\n          the value 'fail'. Upon successful completion of reroute,\n          the 'cwapOperStatus' will change to the value 'ok'. If the  \n          reroute operation failed, the 'cwapOperStatus' will stay in   \n          'fail'. The management station should query the \n          'cwapOperStatus' to decide if a reroute request is \n          successful or not.")
cwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 8), WanPartyAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cwapAdminStatus.setDescription("The 'administrative status' of this party. \n        ")
cwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 9), WanPartyOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapOperStatus.setStatus('current')
if mibBuilder.loadTexts: cwapOperStatus.setDescription("The 'operational status' of this party.")
cwapIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapIdentifier.setStatus('current')
if mibBuilder.loadTexts: cwapIdentifier.setDescription('An arbitrary integer which serves to \n        distinguish all parties on a node.\n        This value is assigned by the managed\n        system when a party is added.\n\n        The use of this variable is implementation specific.')
cwapUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapUploadCounter.setStatus('current')
if mibBuilder.loadTexts: cwapUploadCounter.setDescription('This counter is used by the management station to \n        determine if a party had been modified and requires \n        further action from management station.\n\n        The use of this variable is implementation specific.\n\n        This functionality is conventionally achieved by time\n        stamping using a time-of-day clock. However, in switches\n        where time-of-day clock is not available, the following\n        scheme is used:\n\n        The upload counter is incremented, when:\n\n        * assignment of a party to a cwapIdentifier. This\n          happens when a party is added and assigned this\n          cwapIdentifier.\n        * de-assignment of connection from a cwapIdentifier. This\n          happens when a connection is deleted. \n        * When there is a status change done to this party.')
cwapRootPhysicalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapRootPhysicalId.setStatus('current')
if mibBuilder.loadTexts: cwapRootPhysicalId.setDescription('This object contains physical description of the\n        physical interface the root resides. The presentation of\n        this object is implementation specific.')
cwapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapRowStatus.setStatus('current')
if mibBuilder.loadTexts: cwapRowStatus.setDescription("This object is used to create, modify or delete an entry\n        in the ciscoWanAtmPartyTable.\n \n        * A row may be created using the 'CreateAndGo' option. When\n          the row is successfully created, the RowStatus would be\n          set to 'active' by the agent.\n \n        * A row may be deleted by setting the RowStatus to 'destroy'.\n        ")
ciscoWanAtmPartyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1))
ciscoWanAtmPartyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2))
ciscoWanAtmPartyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "ciscoWanAtmPartyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyMIBCompliance = ciscoWanAtmPartyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIBCompliance.setDescription('The compliance statement for SNMPv2 entities which\n         implement one or more parties of an ATM point-to-\n         multi-point connection.')
ciscoWanAtmPartyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2, 2)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "cwapNSAPAddress"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVpi"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVci"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapAdminStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapOperStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapReroute"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapIdentifier"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapUploadCounter"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRootPhysicalId"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyGroup = ciscoWanAtmPartyGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmPartyGroup.setDescription("This group contains the information of a\n        'party' per each SPVC point-to-multipoint\n        connection.")
mibBuilder.exportSymbols("CISCO-WAN-ATM-PARTY-MIB", PYSNMP_MODULE_ID=ciscoWanAtmPartyMIB, WanNsapAtmAddress=WanNsapAtmAddress, WanPartyAdminStatus=WanPartyAdminStatus, WanPartyOperStatus=WanPartyOperStatus, ciscoWanAtmPartyGroup=ciscoWanAtmPartyGroup, ciscoWanAtmPartyMIB=ciscoWanAtmPartyMIB, ciscoWanAtmPartyMIBCompliance=ciscoWanAtmPartyMIBCompliance, ciscoWanAtmPartyMIBCompliances=ciscoWanAtmPartyMIBCompliances, ciscoWanAtmPartyMIBConform=ciscoWanAtmPartyMIBConform, ciscoWanAtmPartyMIBGroups=ciscoWanAtmPartyMIBGroups, ciscoWanAtmPartyMIBNotifs=ciscoWanAtmPartyMIBNotifs, ciscoWanAtmPartyMIBObjects=ciscoWanAtmPartyMIBObjects, cwapAdminStatus=cwapAdminStatus, cwapConfig=cwapConfig, cwapConfigEntry=cwapConfigEntry, cwapConfigTable=cwapConfigTable, cwapIdentifier=cwapIdentifier, cwapNSAPAddress=cwapNSAPAddress, cwapOperStatus=cwapOperStatus, cwapReference=cwapReference, cwapReroute=cwapReroute, cwapRootPhysicalId=cwapRootPhysicalId, cwapRootVci=cwapRootVci, cwapRootVpi=cwapRootVpi, cwapRowStatus=cwapRowStatus, cwapUploadCounter=cwapUploadCounter, cwapVci=cwapVci, cwapVpi=cwapVpi)
