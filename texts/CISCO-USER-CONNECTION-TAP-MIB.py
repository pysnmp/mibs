#
# PySNMP MIB module CISCO-USER-CONNECTION-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-USER-CONNECTION-TAP-MIB
# Source digest sha256:89e0a6cb5fc110213d2f8a5098f9b1c2d6477542b5bbee8e550cddf3f4f6a7a3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoUserConnectionTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 400))
ciscoUserConnectionTapMIB.setRevisions(('2007-08-09 00:00', '2004-03-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setRevisionsDescriptions(('Correct the DESCRIPTION clause of cutcTapStreamTable.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setLastUpdated('2007-08-09 00:00')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal:170 W. Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:+1 800 553-NETS\n\n            E-mail:cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setDescription("This module manages Cisco's intercept feature for\n        user connections.\n\n        This MIB is used along with CISCO-TAP2-MIB to\n        intercept user traffic. CISCO-TAP2-MIB along with\n        specific filter MIBs like this MIB replace\n        CISCO-TAP-MIB.\n\n        To create an user connection intercept, an entry \n        cuctTapStreamEntry is created which contains the filter \n        details. An entry cTap2StreamEntry of CISCO-TAP2-MIB \n        is created, which is the common stream information \n        for all kinds of intercepts and type of the specific\n        stream is set to userconnection in this entry.")
cUserConnectionTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1))
cUserConnectionTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2))
cuctTapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1))
cuctTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("acctSessionId", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setDescription("This object displays the types of intercepts supported on\n        this device. This may be dependent on hardware capabilities\n        or software capabilities. The value of this object is non \n        zero, if the device supports interception of user connection\n        traffic. A device may support both types of intercepts at\n        the same time.\n        The following fields may be supported:\n            acctSessonId: packets belonging to a user connection \n                          identified by RADIUS attribute \n                          account-session-ID may be intercepted.\n            tapEnable:    set if table entries with\n                          cTap2StreamInterceptEnable set to 'false'\n                          are used to pre-screen packets for intercept;\n                          otherwise these entries are ignored.")
cuctTapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cuctTapStreamTable.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamTable.setDescription("The Intercept Stream Connection Table lists the user\n        connections (sessions) to be intercepted.  The same data \n        stream may be required by multiple taps, and one might \n        assume that often the intercepted stream is a small \n        subset of the traffic that could be intercepted.\n\n\n        This essentially provides options for packet selection.\n        The only option available is RADIUS attribute 44, \n        account session ID. When a user tries to use a service \n        provided by a Network Access Server(NAS) such as PPP,\n        NAS authenticates the user with RADIUS server. Upon\n        successful authentication of the user, the user is \n        provided with the requested service and NAS creates an\n        accounting record with RADIUS accounting server for \n        the user. The NAS assigns a unique account session id\n        for the user session in the accounting record created\n        with the RADIUS server. The account session ID may be\n        used to intercept traffic belonging to the user session.\n\n\n        The value of first index is that of an entry in the\n        cTap2MediationTable, which identifies the application\n        to which intercepted traffic will be sent to. The second \n        index permits connection classifiers to be used to \n        identify traffic to be intercepted. The value of the\n        second index is that of the stream's counter entry \n        in the cTap2StreamTable.")
cuctTapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cuctTapStreamEntry.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamEntry.setDescription('A stream entry indicates a single data stream to be\n        intercepted to a Mediation Device. Many selected data\n        streams may go to the same application interface, and \n        many application interfaces are supported.')
cuctTapStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setReference('RFC 2059, RFC 2865')
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setDescription('This is the RADIUS attribute 44 acct-session-ID. It\n        identifies a user connection.  It is used to specify\n        a user connection to intercept.')
cuctTapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamStatus.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamStatus.setDescription("The status of this conceptual row. This object manages\n        creation, modification, and deletion of rows in this\n        table. When any rows must be changed, \n        cuctTapStreamStatus must be first set to \n        'notInService'.")
cUserConnectionTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1))
cUserConnectionTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2))
cUserConnectionTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cUserConnectionTapMIBCompliance = cUserConnectionTapMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cUserConnectionTapMIBCompliance.setDescription('The compliance statement for entities which implement the\n        Cisco Intercept MIB for user connections.')
cuctTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamCapabilities"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamAcctSessID"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cuctTapStreamComplianceGroup = cuctTapStreamComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: cuctTapStreamComplianceGroup.setDescription('These objects are necessary for a description of user\n        traffic packets to select for interception.')
mibBuilder.exportSymbols("CISCO-USER-CONNECTION-TAP-MIB", PYSNMP_MODULE_ID=ciscoUserConnectionTapMIB, cUserConnectionTapMIBCompliance=cUserConnectionTapMIBCompliance, cUserConnectionTapMIBCompliances=cUserConnectionTapMIBCompliances, cUserConnectionTapMIBConform=cUserConnectionTapMIBConform, cUserConnectionTapMIBGroups=cUserConnectionTapMIBGroups, cUserConnectionTapMIBObjects=cUserConnectionTapMIBObjects, ciscoUserConnectionTapMIB=ciscoUserConnectionTapMIB, cuctTapStreamAcctSessID=cuctTapStreamAcctSessID, cuctTapStreamCapabilities=cuctTapStreamCapabilities, cuctTapStreamComplianceGroup=cuctTapStreamComplianceGroup, cuctTapStreamEncodePacket=cuctTapStreamEncodePacket, cuctTapStreamEntry=cuctTapStreamEntry, cuctTapStreamStatus=cuctTapStreamStatus, cuctTapStreamTable=cuctTapStreamTable)
