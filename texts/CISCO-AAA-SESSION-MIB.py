#
# PySNMP MIB module CISCO-AAA-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-AAA-SESSION-MIB
# Source digest sha256:5427826d0d706b06fa2f4fc225dfa7068d972f6535922e49fd2a565e1fed493d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowPointer, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention", "TruthValue")
ciscoAAASessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 150))
ciscoAAASessionMIB.setRevisions(('2006-03-21 00:00', '2002-04-11 00:00', '1999-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAAASessionMIB.setRevisionsDescriptions(('Added the casnNasPort and casnVaiIfIndex objects to the\n         casnActiveTable.\n        ', 'Imported Unsigned32 from SNMPv2-SMI instead of CISCO-TC\n        ', 'Initial version\n        ',))
if mibBuilder.loadTexts: ciscoAAASessionMIB.setLastUpdated('2006-03-21 00:00')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n \n                   Tel: +1 800 553-NETS\n \n                E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setDescription('This MIB module provides data for accounting sessions\n                 based on Authentication, Authorization, Accounting\n                 (AAA) protocols.\n\n\n                 References:\n                     RFC 2139 RADIUS Accounting\n                     The TACACS+ Protocol Version 1.78, Internet Draft\n\n\n                ')
class CctCallId(TextualConvention, Unsigned32):
    description = 'Represents a Call Identifier.\n         The call identifier is used as an unique identifier for an\n         call within the system.\n\n         A zero value indicates no call ID.\n        '
    status = 'current'

class CasnSessionId(TextualConvention, Unsigned32):
    description = 'Represents an Accounting Session Identifier.\n         The session identifier is used as an unique identifier for\n         a session within the system.\n        '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

casnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1))
casnActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1))
casnGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2))
casnActiveTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableEntries.setStatus('current')
if mibBuilder.loadTexts: casnActiveTableEntries.setDescription('Number of entries currently in casnActiveTable\n            ')
casnActiveTableHighWaterMark = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableHighWaterMark.setStatus('current')
if mibBuilder.loadTexts: casnActiveTableHighWaterMark.setDescription('Maximum number of entries present in casnActiveTable\n             since last system re-initialization.\n\n             This corresponds to the maximum value reported by\n             casnActiveTableEntries.\n            ')
casnActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: casnActiveTable.setStatus('current')
if mibBuilder.loadTexts: casnActiveTable.setDescription('This table contains entries for active AAA accounting\n             sessions in the system.\n            ')
casnActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-AAA-SESSION-MIB", "casnSessionId"))
if mibBuilder.loadTexts: casnActiveEntry.setStatus('current')
if mibBuilder.loadTexts: casnActiveEntry.setDescription('The information regarding a single accounting session.\n\n             Entries are created when a new accounting session\n             is begun.\n\n             Entries are removed when the accounting session\n             is ended.\n\n             Initiating termination of a session with the object\n             casnDisconnect will cause removal of the entry when\n             the session completes termination.\n            ')
casnSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 1), CasnSessionId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: casnSessionId.setStatus('current')
if mibBuilder.loadTexts: casnSessionId.setDescription("This is the session identification used by the\n             accounting protocol.\n\n             This value is unique to a session within the system,\n             even if multiple accounting protocols are in use.\n\n             The value of this object corresponds to these\n             accounting protocol attributes.\n                RADIUS:  attribute 44, Acct-Session-Id\n                TACACS+: attribute 'task_id'\n            ")
casnUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnUserId.setStatus('current')
if mibBuilder.loadTexts: casnUserId.setDescription("The User login ID or zero length string if unavailable.\n\n             The value of this object corresponds to these\n             accounting protocol attributes.\n                RADIUS:  attribute 1, User-Name\n                TACACS+: attribute 'user'\n            ")
casnIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIpAddr.setStatus('current')
if mibBuilder.loadTexts: casnIpAddr.setDescription("The IP address of the session or 0.0.0.0 if not\n             applicable or unavailable.\n\n             RADIUS:  attribute 8, Framed-IP-Address\n             TACACS+: attribute 'addr'\n            ")
casnIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 4), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIdleTime.setStatus('current')
if mibBuilder.loadTexts: casnIdleTime.setDescription('The elapsed time that this session has been idle.\n\n             This is the time since the last user-level data has been\n             received or transmitted. Protocol level handshaking\n             associated with the call is considered to be idle for\n             this object.\n            ')
casnDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: casnDisconnect.setStatus('current')
if mibBuilder.loadTexts: casnDisconnect.setDescription('This object is used to terminate this session.\n\n             Setting the value to true(1) will initiate termination\n             of this session.\n\n             The entry will be removed once the session has completed\n             termination.\n\n             Once this object has been set to true(1), the session\n             termination process can not be cancelled by setting the\n             value false(2).\n            ')
casnCallTrackerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 6), CctCallId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnCallTrackerId.setStatus('current')
if mibBuilder.loadTexts: casnCallTrackerId.setDescription('The value of this object is the entry index in the\n              CISCO-CALL-TRACKER-MIB cctActiveTable of the call\n              corresponding to this accounting session.\n\n              Using the value of this object to query the\n              cctActiveTable will provide more detailed data regarding\n              the session represented by this casnActiveEntry.\n             ')
casnNasPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnNasPort.setStatus('current')
if mibBuilder.loadTexts: casnNasPort.setDescription('The value of this object identifies a particular\n              conceptual row associated with the session identified by\n              casnSessionId.  The conceptual row that this object points\n              to represents a port that is used to transport a session.\n\n              If the port transporting the session cannot be determined,\n              the value of this object will be zeroDotZero.\n\n              For example, suppose a session is established using an ATM\n              PVC.  If the ifIndex of the ATM interface is 7, and the \n              VPI/VCI values of the PVC are 1, 100 respectively, then\n              the value of this object might be as follows:\n\n                     casnNasPort.15 = atmVclAdminStatus.7.1.100\n                                 ^                      ^ ^  ^\n                                 |                      | |  |\n                 casnSessionId --+                      | |  |\n                       ifIndex -------------------------+ |  |\n                     atmVclVpi ---------------------------+  |\n                     atmVclVci ------------------------------+\n\n              where atmVclAdminStatus is the first accessible object\n              of the atmVclTable of the ATM-MIB.\n             ')
casnVaiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnVaiIfIndex.setStatus('current')
if mibBuilder.loadTexts: casnVaiIfIndex.setDescription('The ifIndex of the Virtual Access Interface (VAI)\n              that is associated with the PPP session.\n\n              This interface may not be represented in the IF-MIB in\n              which case the value of this object will be zero.\n             ')
casnTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnTotalSessions.setStatus('current')
if mibBuilder.loadTexts: casnTotalSessions.setDescription('Total number of sessions since last system\n              re-initialization.\n \n              This value includes all sessions currently in the\n              casnActiveTable and all previous sessions whether\n              terminated via casnDisconnect or via other\n              mechanisms.\n             ')
casnDisconnectedSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnDisconnectedSessions.setStatus('current')
if mibBuilder.loadTexts: casnDisconnectedSessions.setDescription('Total number of sessions which have been disconnected using\n             casnDisconnect since last system re-initialization.\n\n             This value includes any sessions still in the\n             casnActiveTable with a casnDisconnect value of true(1) and\n             all previous sessions which terminated as a result of\n             setting casnDisconnect.\n            ')
casnMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2))
casnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2, 1))
casnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3))
casnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1))
casnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2))
casnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBCompliance = casnMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: casnMIBCompliance.setDescription('The compliance statement for entities which\n             implement the CISCO AAA Session MIB')
casnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"), ("CISCO-AAA-SESSION-MIB", "casnActiveGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBComplianceRev1 = casnMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: casnMIBComplianceRev1.setDescription('The compliance statement for entities which\n             implement the CISCO AAA Session MIB')
casnActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveTableEntries"), ("CISCO-AAA-SESSION-MIB", "casnActiveTableHighWaterMark"), ("CISCO-AAA-SESSION-MIB", "casnUserId"), ("CISCO-AAA-SESSION-MIB", "casnIpAddr"), ("CISCO-AAA-SESSION-MIB", "casnIdleTime"), ("CISCO-AAA-SESSION-MIB", "casnDisconnect"), ("CISCO-AAA-SESSION-MIB", "casnCallTrackerId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroup = casnActiveGroup.setStatus('current')
if mibBuilder.loadTexts: casnActiveGroup.setDescription('A collection of objects providing the\n             AAA session information.\n            ')
casnGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnTotalSessions"), ("CISCO-AAA-SESSION-MIB", "casnDisconnectedSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnGeneralGroup = casnGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: casnGeneralGroup.setDescription('A collection of objects providing the\n             AAA session information.\n            ')
casnActiveGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 3)).setObjects(("CISCO-AAA-SESSION-MIB", "casnNasPort"), ("CISCO-AAA-SESSION-MIB", "casnVaiIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroupSup1 = casnActiveGroupSup1.setStatus('current')
if mibBuilder.loadTexts: casnActiveGroupSup1.setDescription('A collection of objects that supplements\n             the casnActiveGroup.\n            ')
mibBuilder.exportSymbols("CISCO-AAA-SESSION-MIB", CasnSessionId=CasnSessionId, CctCallId=CctCallId, PYSNMP_MODULE_ID=ciscoAAASessionMIB, casnActive=casnActive, casnActiveEntry=casnActiveEntry, casnActiveGroup=casnActiveGroup, casnActiveGroupSup1=casnActiveGroupSup1, casnActiveTable=casnActiveTable, casnActiveTableEntries=casnActiveTableEntries, casnActiveTableHighWaterMark=casnActiveTableHighWaterMark, casnCallTrackerId=casnCallTrackerId, casnDisconnect=casnDisconnect, casnDisconnectedSessions=casnDisconnectedSessions, casnGeneral=casnGeneral, casnGeneralGroup=casnGeneralGroup, casnIdleTime=casnIdleTime, casnIpAddr=casnIpAddr, casnMIBCompliance=casnMIBCompliance, casnMIBComplianceRev1=casnMIBComplianceRev1, casnMIBCompliances=casnMIBCompliances, casnMIBConformance=casnMIBConformance, casnMIBGroups=casnMIBGroups, casnMIBNotificationPrefix=casnMIBNotificationPrefix, casnMIBNotifications=casnMIBNotifications, casnMIBObjects=casnMIBObjects, casnNasPort=casnNasPort, casnSessionId=casnSessionId, casnTotalSessions=casnTotalSessions, casnUserId=casnUserId, casnVaiIfIndex=casnVaiIfIndex, ciscoAAASessionMIB=ciscoAAASessionMIB)
