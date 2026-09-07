#
# PySNMP MIB module CISCO-MOBILITY-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MOBILITY-TAP-MIB
# Source digest sha256:4804b3d4c038a99df5d42c157516d2d4b610a96269b471adb45db3bd0e251f1d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, StorageType, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention", "TruthValue")
ciscoMobilityTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 672))
ciscoMobilityTapMIB.setRevisions(('2010-06-16 00:00', '2010-04-15 00:00', '2008-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMobilityTapMIB.setRevisionsDescriptions(('Added a new textual convention:\n        CmtapLawfulInterceptID.\n        Added following three objects to cmtapStreamTable.\n        cmtapStreamLIIdentifier.\n        cmtapStreamLocationInfo.\n        cmtapStreamInterceptType.\n        Added the following new MODULE-COMPLIANCE.\n        ciscoMobilityTapMIBComplianceRev01.\n        Added the following new OBJECT-GROUP.\n        ciscoMobilityTapStreamGroupSup1.', "Added enumeration 'servedMdn' for mtapStreamCapabilities object\n        and CmtapSubscriberIDType.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setLastUpdated('2010-06-16 00:00')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal:170 W. Tasman Drive\n            San Jose, CA  95134\n            USA\n\n\n            Tel:+1 800 553-NETS\n\n\n            E-mail:cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setDescription("This module manages Cisco's intercept feature for\n        Mobility Gateway Products.\n\n        This MIB is used along with CISCO-TAP2-MIB MIB to\n        intercept Mobility Gateway traffic. CISCO-TAP2-MIB MIB \n        along with specific filter MIBs like this MIB replace\n        the CISCO-TAP-MIB MIB.\n\n        To create a Mobility intercept, an entry \n        cmtapStreamEntry is created which contains the filter \n        details. An entry cTap2StreamEntry of CISCO-TAP2-MIB is \n        created which is the common stream information for all \n        kinds of intercepts and type of the specific stream is \n        set to 'mobility' in this entry.")
ciscoMobilityTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 0))
ciscoMobilityTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1))
ciscoMobilityTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2))
cmtapStreamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1))
class CmtapLawfulInterceptID(TextualConvention, OctetString):
    description = 'An octet string containing the Lawful Intercept Identifier\n        (LIID)assigned to the intercepted target by a law enforcement\n        agency defined by Communications Assistance for Law Enforcement\n        Act (CALEA).'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

class CmtapSubscriberIDType(TextualConvention, Integer32):
    description = "A value that represents the type of address that is used to\n        identify a subscriber.  The following types are\n        currently supported:\n                unknown:   The Subscriber's identifier type is not\n                           known.\n                msid:      A Mobile Subscriber Identity (MSID).\n                imsi:      An International Mobile Subscriber\n        Identity(IMSI) number.\n                nai:       A Network Access Identifier (NAI).\n                esn:       An Electronic Serial Number (ESN).\n                servedMdn: Served Mdn(mobile directory number) \n                           is a vendor specific attribute.\n                           It is similar to the class IETF attribute.\n                           Refer to RFC 2865 for vendor \n                           specific attribute format.\n                           Example:dsg-mdn."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("msid", 2), ("imsi", 3), ("nai", 4), ("esn", 5), ("servedMdn", 6))

class CmtapSubscriberID(TextualConvention, OctetString):
    description = "An octet string containing a subscriber's\n        identification, preferably in human-readable form.\n\n        A CmtapStreamSubscriberID value is always interpreted\n        within the context of an CmtapStreamSubscriberIDType value.\n        Every usage of the CmtapStreamSubscriberID textual\n        convention is required to specify the identity that \n        corresponds to a CmtapStreamSubscriberIDType object."
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

cmtapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("calledSubscriberID", 2), ("nonvolatileStorage", 3), ("msid", 4), ("imsi", 5), ("nai", 6), ("esn", 7), ("servedMdn", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmtapStreamCapabilities.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamCapabilities.setDescription("This object indicates the Mobility Gateway intercept\n        features that are implemented by this device and are\n        manageable through this MIB.\n            tapEnable:          set if table entries with\n                                cTap2StreamInterceptEnable set to \n                                'false' are used to pre-screen packets\n                                for intercept; otherwise these entries\n                                are ignored.\n            interface:          SNMP ifIndex Value may be used to\n                                select interception of all data \n                                crossing an interface or set of\n                                interfaces.\n            nonvolatileStorage: The cmTapStreamTable supports the\n                                ability to store rows in nonvolatile\n                                memory.\n            calledSubscriberID: The cmtapStreamCalledSubscriberID can\n                                be used to specify intercepts.\n                                Otherwise, this field is disabled.\n            msid:               A Mobile Subscriber Identity (MSID) can\n                                be used in the ID strings to specify\n                                intercepts.\n            imsi:               An International Mobile Subscriber\n                                Identity (IMSI) number can be used ID\n                                strings to specify intercepts.\n            nai:                A Network Access Identifier (NAI) can\n                                be used in the ID strings to specify\n                                intercepts.\n            esn:                An Electronic Serial Number (ESN) can\n                                be used in the ID strings to specify\n                                intercepts. \n           servedMdn:           Vendor specific attribute Served-Mobile Directory\n                                Number(MDN) can be used in the ID strings \n                                to specify intercepts.")
cmtapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmtapStreamTable.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamTable.setDescription('The Mobility Stream Table lists the data streams to be\n        intercepted. The same data stream may be required by multiple \n        taps. \n\n\n        This essentially provides options for packet selection, only \n        some of which might be used. For example, if all the traffic to \n        or from a subscriber is to be intercepted, one would configure \n        an entry listing SubscriberID along with the SubscriberIDType  \n        corresponding to the stream that one wishes to intercept. \n\n\n        The first index indicates which Mediation Device the \n        intercepted traffic will be diverted to. The second index,\n        which indicates the specific intercept stream, permits multiple\n        classifiers to be used together.  For example, an IP stream\n        and a Mobility stream could both be listed in their respective\n        tables, yet still correspond to the same Mediation Device\n        entry.\n\n        Entries are added to this table via cmtapStreamStatus in  \n        accordance with the RowStatus convention.')
cmtapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cmtapStreamEntry.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamEntry.setDescription('A stream entry indicates a single data stream to be\n        intercepted to a Mediation Device. Many selected data\n        streams may go to the same application interface and many\n        application interfaces are supported.')
cmtapStreamCalledSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 1), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberIDType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberIDType.setDescription('Identifies the type of address that is stored in the\n        cmtapStreamCalledSubscriberID string.')
cmtapStreamCalledSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 2), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberID.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberID.setDescription('A string used to identify the party being contacted.\n\n        The type of this identification is determined by the\n        cmtapStreamCalledSubscriberIDType object.')
cmtapStreamSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 3), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberIDType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamSubscriberIDType.setDescription('Identifies the type of address that is stored in the\n        cmtapStreamSubscriberID string.')
cmtapStreamSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 4), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberID.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamSubscriberID.setDescription('A string used to identify the subscriber to tap.\n\n        The type of this indentification is determined by the\n        cmtapStreamSubscriberIDType object.')
cmtapStreamStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStorageType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamStorageType.setDescription("This object specifies the storage type of this conceptual row.\n        If it is set to 'nonVolatile', this entry can be saved into\n        non-volatile memory.")
cmtapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStatus.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamStatus.setDescription("The status of this conceptual row. This object manages\n        creation, modification, and deletion of rows in this table.\n        When any field must be changed, cmtapStreamStatus must be\n        first set to 'notInService'.")
cmtapStreamLIIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 7), CmtapLawfulInterceptID().clone('not set')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLIIdentifier.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamLIIdentifier.setDescription('This object is an identifier assigned by a Law Enforcement\n        Agency (LEA) to facilitate LI operations as defined in 3GPP TS\n        33.108 v8.7.0 standards document.')
cmtapStreamLocationInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLocationInfo.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamLocationInfo.setDescription('This object indicates, if the userLocationInfo object should be\n        included in the Intercept Related Information (IRI) messages\n        sent by the gateway to mediation gateway(s) for interception\n        taps.\n\n        The userLocationInfo is defined as part of the IRI messages in\n        3GPP 33.108 v8.7.0 standards document.')
cmtapStreamInterceptType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ccOnly", 1), ("iriOnly", 2), ("both", 3))).clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamInterceptType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamInterceptType.setDescription('This object indicates the intercept type of the tapped stream.\n        The tap can be provisioned to intercept control messages (IRI)\n        from the tapped stream, the payload (CC) messages from the\n        tapped stream or both.  The format of these messages in defined\n        in 3GPP TS 33.108 v8.7.0 standards document.    \n        ccOnly(1)  - Content of communication interception only. \n        iriOnly(2) - Intercept Related Information only.\n        both(3)    - Intercept both:  CC and IRI.')
ciscoMobilityTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1))
ciscoMobilityTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2))
ciscoMobilityTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBCompliance = ciscoMobilityTapMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoMobilityTapMIBCompliance.setDescription('The compliance statement for entities which implement the\n        Cisco Intercept MIB for Mobility Gateways')
ciscoMobilityTapMIBComplianceRev01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBComplianceRev01 = ciscoMobilityTapMIBComplianceRev01.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapMIBComplianceRev01.setDescription('The compliance statement for entities which implement the Cisco\n        Intercept MIB for Mobility Gateways.')
ciscoMobilityTapCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapCapabilityGroup = ciscoMobilityTapCapabilityGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapCapabilityGroup.setDescription('A collection of objects which provide Mobility Gateway\n        capabilities for the system.')
ciscoMobilityTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStorageType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroup = ciscoMobilityTapStreamGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapStreamGroup.setDescription('A collection of objects which provide information about\n        the stream from which we wish to intercept packets.')
ciscoMobilityTapStreamGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 3)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLIIdentifier"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLocationInfo"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamInterceptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroupSup1 = ciscoMobilityTapStreamGroupSup1.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapStreamGroupSup1.setDescription('A collection of objects which provide additional information\n        about the stream from which we wish to intercept packets.')
mibBuilder.exportSymbols("CISCO-MOBILITY-TAP-MIB", CmtapLawfulInterceptID=CmtapLawfulInterceptID, CmtapSubscriberID=CmtapSubscriberID, CmtapSubscriberIDType=CmtapSubscriberIDType, PYSNMP_MODULE_ID=ciscoMobilityTapMIB, ciscoMobilityTapCapabilityGroup=ciscoMobilityTapCapabilityGroup, ciscoMobilityTapMIB=ciscoMobilityTapMIB, ciscoMobilityTapMIBCompliance=ciscoMobilityTapMIBCompliance, ciscoMobilityTapMIBComplianceRev01=ciscoMobilityTapMIBComplianceRev01, ciscoMobilityTapMIBCompliances=ciscoMobilityTapMIBCompliances, ciscoMobilityTapMIBConform=ciscoMobilityTapMIBConform, ciscoMobilityTapMIBGroups=ciscoMobilityTapMIBGroups, ciscoMobilityTapMIBNotifs=ciscoMobilityTapMIBNotifs, ciscoMobilityTapMIBObjects=ciscoMobilityTapMIBObjects, ciscoMobilityTapStreamGroup=ciscoMobilityTapStreamGroup, ciscoMobilityTapStreamGroupSup1=ciscoMobilityTapStreamGroupSup1, cmtapStreamCalledSubscriberID=cmtapStreamCalledSubscriberID, cmtapStreamCalledSubscriberIDType=cmtapStreamCalledSubscriberIDType, cmtapStreamCapabilities=cmtapStreamCapabilities, cmtapStreamEntry=cmtapStreamEntry, cmtapStreamGroup=cmtapStreamGroup, cmtapStreamInterceptType=cmtapStreamInterceptType, cmtapStreamLIIdentifier=cmtapStreamLIIdentifier, cmtapStreamLocationInfo=cmtapStreamLocationInfo, cmtapStreamStatus=cmtapStreamStatus, cmtapStreamStorageType=cmtapStreamStorageType, cmtapStreamSubscriberID=cmtapStreamSubscriberID, cmtapStreamSubscriberIDType=cmtapStreamSubscriberIDType, cmtapStreamTable=cmtapStreamTable)
