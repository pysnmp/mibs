#
# PySNMP MIB module CISCO-VOICE-DNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-DNIS-MIB
# Source digest sha256:f7e2b6a9996b1bf879663285f5a7cc74d557f10147f364ae7519a5de19151b7a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoVoiceDnisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 219))
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setLastUpdated('2002-05-01 00:00')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n \n                Tel: +1 800 553-NETS\n \n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setDescription('The MIB module provides management support for Dialer\n                 Number Information Service (DNIS) mapping.  A DNIS\n                 entry is associated with a Voice XML (VXML) page to\n                 provide audio play back features. Multiple DNIS\n                 entries can be grouped together to form a DNIS\n                 mapping with a unique map name.\n\n                 *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS ***\n                 \n                 DNIS - Dialer Number Information Service\n\n                 XML  - Extensible Markup Language\n\n                 VXML - Voice XML\n\n                 URL  - Uniform Resource Locator  \n                ')
class DnisMapname(TextualConvention, OctetString):
    description = 'An identification for a DNIS map name or a DNIS name. A\n             DNIS map name correspods to a group of individual DNIS\n             names. The DNIS map names are unique in the system, and\n             within each map name, individual DNIS names are unique.\n            '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvE164String(TextualConvention, OctetString):
    description = "A UTF-8 string limited to the character set defined for\n             E.164, '0123456789*#,<quote>'.\n             Note that <quote> represents the double quote which\n             cannot be contained in a SMI description clause."
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

cvDnisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1))
cvDnisMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1))
cvDnisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisMappingTable.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingTable.setDescription('The table contains the map name and a url specifying\n             a file name. The file contains DNIS entries that belong\n             to the DNIS mapping.\n            ')
cvDnisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"))
if mibBuilder.loadTexts: cvDnisMappingEntry.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingEntry.setDescription('Information about a single DNIS mapping. There is a\n             unique DNIS map name. New DNIS mapping can be created\n             using cvDnisMappingStatus.\n\n             The entry can be created with or without a file location \n             specified by cvDnisMappingUrl. The mapping file contains\n             DNIS name and VXML page per line. For example, a \n             cvDnisMappingUrl could be tftp://someserver/dnismap.txt.\n             This file is a text file and the content format is\n               dnis <dnisname> url <urlname>.\n             An example of the contents of the file itself can be\n               dnis 18004251234 url http://www.b.com/p/vwelcome.vxml\n               dnis 18004253421 url http://www.c.com/j/vxmlintf.vxml\n             If a mapping file location is specified, then new rows\n             corresponding to this map name are created and populated\n             in cvDnisNodeTable from the contents of the file. The\n             rows corresponding to this map name in cvDnisNodeTable\n             cannot be created or modified or deleted but can be\n             read. \n\n             If a mapping file location is not specified in\n             cvDnisMappingUrl, then individual DNIS entries\n             corresponding to this map name can be created, modified\n             and deleted in cvDnisNodeTable. \n\n             Deleting an entry deletes all the related entries in\n             cvDnisNodeTable. \n            ')
cvDnisMappingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 1), DnisMapname().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisMappingName.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingName.setDescription('The name which uniquely identifies a DNIS mapping. \n            ')
cvDnisMappingUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 2), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingUrl.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingUrl.setDescription('The url specifies a file location. The file contains\n             individual DNIS entries that belong to the DNIS map \n             name specified by cvDnisMappingName.\n\n             Once a url is created and associated with a map name (the\n             association is complete when the row is made active(1)),\n             it cannot be modified while cvDnisMappingStatus is\n             active. If a different url needs to be associated with\n             the current map name, the row status should be made\n             notInService(2) and this object has to be modified to\n             associate a new url. When a new association is made all\n             the DNIS entries corresponding to the old association\n             will be deleted from the cvDnisNodeTable.\n\n             The url is read when the row status is made active(1) or\n             when the row status is active and the object \n\t     cvDnisMappingRefresh is explicitly set to refresh(2). \n\t     If the url is not accessible then a\n             cvDnisMappingUrlInaccessible notification will be\n             generted. \n            ')
cvDnisMappingRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("refresh", 2))).clone('idle')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingRefresh.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingRefresh.setDescription('Whenever there is a need to re-read the contents of the\n             file specified by cvDnisMappingUrl, this object can be\n             set to refresh(2). This will cause the contents of the\n             file to be re-read and correspondingly update the\n             cvDnisNodeTable. After the completion of this operation,\n             the value of this object is reset to idle(1). The only\n             operation allowed on this object is setting it to\n             refresh(2). This can only be done when the current value\n             is idle(1) and the rowstatus is active(1).\n \n             idle       - The refreshing process is idle and the user\n                          can modify this object to refresh.\n             refresh    - The refreshing process is currently busy and\n                          the user have to wait till the object\n                          becomes idle to issue new refresh.\n            ')
cvDnisMappingUrlAccessError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 4), DisplayString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setDescription('ASCII text describing the error on last access of the url\n             specified in cvDnisMappingUrl.\n\n             If the url access does not succeed, then this object is\n             populated with an error message indicating the reason for\n             failure. If the url access succeeds, this object is set\n             to null string.\n            ')
cvDnisMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingStatus.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingStatus.setDescription('This object is used to create a new row or modify or\n             delete an existing row in this table. When making the\n             status active(1), if a valid cvDnisMappingUrl is present\n             the contents of the url is downloaded and during that\n             time cvDnisMappingRefresh is set to refresh(2). When\n             cvDnisMappingRefresh is set to refresh(2), only the\n             destroy(6) operation is allowed.\n            ')
cvDnisNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisNodeTable.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeTable.setDescription('The table contains a DNIS name and a url. The url is a\n             pointer to a VXML page for the DNIS name. \n            ')
cvDnisNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"), (1, "CISCO-VOICE-DNIS-MIB", "cvDnisNumber"))
if mibBuilder.loadTexts: cvDnisNodeEntry.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeEntry.setDescription("Each entry is a DNIS name and the location of the\n             associated VXML page. New DNIS entries can be created or\n             the existing entries can be modified or deleted only if\n             the corresponding map name (defined in\n             cvDnisMappingTable) does not have any file name provided\n             in the cvDnisMappingUrl object. \n\n             If a file name is provided in cvDnisMappingUrl\n             corresponding to this entry's map name, then this row\n             will have read permission only.\n            ")
cvDnisNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 1), CvE164String()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisNumber.setStatus('current')
if mibBuilder.loadTexts: cvDnisNumber.setDescription('The individual DNIS name. It is unique within a DNIS\n             mapping.\n            ')
cvDnisNodeUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 2), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeUrl.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeUrl.setDescription('The url specifies a VXML page. This page contains\n             voice XML links to play audio data.\n\n             This url which is a VXML page is not read immediately\n             when the row is made active(1), but only when a call that\n             requires the use of this DNIS comes through.\n            ')
cvDnisNodeModifiable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisNodeModifiable.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeModifiable.setDescription('This object specifies whether the object in a particular\n             row is modifiable. The object is set to true(1) if the\n             corresponding map name (defined in cvDnisMappingTable)\n             does not have any file name provided in the\n             cvDnisMappingUrl object. Otherwise this object is set to\n             false(2) and the row becomes read only.  \n            ')
cvDnisNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeStatus.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeStatus.setDescription('This object is used to create a new row or modify or\n             delete an existing row in this table. The objects in a\n             row can be modified or deleted while the row status is\n             active(1) and cvDnisNodeModifiable is true(1). The row\n             status cannot be set to notInService(2) or\n             createAndWait(5). \n            ')
cvDnisMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2))
cvDnisMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0))
cvDnisMappingUrlInaccessible = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"))
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setDescription('Inaccessible DNIS mapping url notification. A\n             cvDnisMappingUrlInaccessible notification is sent if the\n             specified url is not accessible.\n            ')
cvDnisMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3))
cvDnisMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1))
cvDnisMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2))
cvDnisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisGroup"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisMIBCompliance = cvDnisMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvDnisMIBCompliance.setDescription('The compliance statement for entities which\n             implement the CISCO VOICE DNIS MIB')
cvDnisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingRefresh"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingStatus"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeModifiable"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisGroup = cvDnisGroup.setStatus('current')
if mibBuilder.loadTexts: cvDnisGroup.setDescription('A collection of objects provides a relation between a\n             DNIS map name and the DNIS entries belonging to that map\n             name. \n            ')
cvDnisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 2)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlInaccessible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisNotificationGroup = cvDnisNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cvDnisNotificationGroup.setDescription('The notifications for CISCO-VOICE-DNIS-MIB.\n            ')
mibBuilder.exportSymbols("CISCO-VOICE-DNIS-MIB", CvE164String=CvE164String, DnisMapname=DnisMapname, PYSNMP_MODULE_ID=ciscoVoiceDnisMIB, ciscoVoiceDnisMIB=ciscoVoiceDnisMIB, cvDnisGroup=cvDnisGroup, cvDnisMIBCompliance=cvDnisMIBCompliance, cvDnisMIBCompliances=cvDnisMIBCompliances, cvDnisMIBConformance=cvDnisMIBConformance, cvDnisMIBGroups=cvDnisMIBGroups, cvDnisMIBNotificationPrefix=cvDnisMIBNotificationPrefix, cvDnisMIBNotifications=cvDnisMIBNotifications, cvDnisMIBObjects=cvDnisMIBObjects, cvDnisMap=cvDnisMap, cvDnisMappingEntry=cvDnisMappingEntry, cvDnisMappingName=cvDnisMappingName, cvDnisMappingRefresh=cvDnisMappingRefresh, cvDnisMappingStatus=cvDnisMappingStatus, cvDnisMappingTable=cvDnisMappingTable, cvDnisMappingUrl=cvDnisMappingUrl, cvDnisMappingUrlAccessError=cvDnisMappingUrlAccessError, cvDnisMappingUrlInaccessible=cvDnisMappingUrlInaccessible, cvDnisNodeEntry=cvDnisNodeEntry, cvDnisNodeModifiable=cvDnisNodeModifiable, cvDnisNodeStatus=cvDnisNodeStatus, cvDnisNodeTable=cvDnisNodeTable, cvDnisNodeUrl=cvDnisNodeUrl, cvDnisNotificationGroup=cvDnisNotificationGroup, cvDnisNumber=cvDnisNumber)
