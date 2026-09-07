#
# PySNMP MIB module CISCO-VIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VIM-MIB
# Source digest sha256:d7e6d723763293503237c2586dac15f7b7f7e5d973a295895375d4d82b8260f7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ciscoVimMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 855))
ciscoVimMIB.setRevisions(('2018-07-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVimMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVimMIB.setLastUpdated('2018-07-16 00:00')
if mibBuilder.loadTexts: ciscoVimMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVimMIB.setContactInfo('Cisco Systems\n\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-cvim@cisco.com')
if mibBuilder.loadTexts: ciscoVimMIB.setDescription('The MIB module for the Cisco Virtualized Infrastructure Manager\n        (CVIM) platform.\n\n        This MIB only handles notifications from the CVIM.')
class CFaultSeverity(TextualConvention, Integer32):
    description = 'A code used to identify the severity of a fault.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("emergency", 1), ("critical", 2), ("major", 3), ("alert", 4), ("informational", 5))

class CFaultCode(TextualConvention, Integer32):
    description = 'A code identifying a class of fault.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("resourceUsage", 2), ("resourceThreshold", 3), ("serviceFailure", 4), ("hardwareFailure", 5), ("networkConnectivity", 6))

ciscoVimMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 0))
ciscoVimMIBFaults = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 1))
ciscoVimMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2))
cvimPodId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimPodId.setStatus('current')
if mibBuilder.loadTexts: cvimPodId.setDescription('Object identificating the CVIM PodId')
cvimFaultCreationTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 2), DateAndTime()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimFaultCreationTime.setStatus('current')
if mibBuilder.loadTexts: cvimFaultCreationTime.setDescription('The date and time when the fault is detected.')
cvimNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimNodeId.setStatus('current')
if mibBuilder.loadTexts: cvimNodeId.setDescription('This object is hostname which uniquely identifies the\n        server on which this fault got detected.')
cvimFaultSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 100))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimFaultSource.setStatus('current')
if mibBuilder.loadTexts: cvimFaultSource.setDescription('Service or component name that generated the fault.')
cvimFaultSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 5), CFaultSeverity()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimFaultSeverity.setStatus('current')
if mibBuilder.loadTexts: cvimFaultSeverity.setDescription('A code identifying the perceived severity of the fault.')
cvimFaultCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 6), CFaultCode()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimFaultCode.setStatus('current')
if mibBuilder.loadTexts: cvimFaultCode.setDescription('A code uniquely identifying the fault.')
cvimFaultDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 855, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2048))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvimFaultDescription.setStatus('current')
if mibBuilder.loadTexts: cvimFaultDescription.setDescription('A human-readable message providing details about the fault.')
cvimFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 1)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimNodeId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"), ("CISCO-VIM-MIB", "cvimFaultDescription"))
if mibBuilder.loadTexts: cvimFaultActiveNotif.setStatus('current')
if mibBuilder.loadTexts: cvimFaultActiveNotif.setDescription('This notification is generated by CVIM whenever a fault gets\n        triggered.')
cvimFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 855, 0, 2)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimNodeId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"), ("CISCO-VIM-MIB", "cvimFaultDescription"))
if mibBuilder.loadTexts: cvimFaultClearNotif.setStatus('current')
if mibBuilder.loadTexts: cvimFaultClearNotif.setDescription('This notification is generated by a CVIM whenever a\n        fault is resolved.')
ciscoVimMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1))
ciscoVimMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2))
cvimMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 1, 1)).setObjects(("CISCO-VIM-MIB", "cvimMIBFaultGroup"), ("CISCO-VIM-MIB", "cvimMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBCompliance = cvimMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvimMIBCompliance.setDescription('The compliance statement for entities that support\n        the Cisco CVIM Managed Objects')
cvimMIBFaultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 1)).setObjects(("CISCO-VIM-MIB", "cvimPodId"), ("CISCO-VIM-MIB", "cvimFaultSource"), ("CISCO-VIM-MIB", "cvimFaultCreationTime"), ("CISCO-VIM-MIB", "cvimFaultSeverity"), ("CISCO-VIM-MIB", "cvimFaultCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBFaultGroup = cvimMIBFaultGroup.setStatus('current')
if mibBuilder.loadTexts: cvimMIBFaultGroup.setDescription('The set of CVIM Fault groups defined by this MIB')
cvimMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 855, 2, 2, 2)).setObjects(("CISCO-VIM-MIB", "cvimFaultActiveNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvimMIBNotificationGroup = cvimMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cvimMIBNotificationGroup.setDescription('The set of CVIM notifications defined by this MIB')
mibBuilder.exportSymbols("CISCO-VIM-MIB", CFaultCode=CFaultCode, CFaultSeverity=CFaultSeverity, PYSNMP_MODULE_ID=ciscoVimMIB, ciscoVimMIB=ciscoVimMIB, ciscoVimMIBCompliances=ciscoVimMIBCompliances, ciscoVimMIBConform=ciscoVimMIBConform, ciscoVimMIBFaults=ciscoVimMIBFaults, ciscoVimMIBGroups=ciscoVimMIBGroups, ciscoVimMIBNotifs=ciscoVimMIBNotifs, cvimFaultActiveNotif=cvimFaultActiveNotif, cvimFaultClearNotif=cvimFaultClearNotif, cvimFaultCode=cvimFaultCode, cvimFaultCreationTime=cvimFaultCreationTime, cvimFaultDescription=cvimFaultDescription, cvimFaultSeverity=cvimFaultSeverity, cvimFaultSource=cvimFaultSource, cvimMIBCompliance=cvimMIBCompliance, cvimMIBFaultGroup=cvimMIBFaultGroup, cvimMIBNotificationGroup=cvimMIBNotificationGroup, cvimNodeId=cvimNodeId, cvimPodId=cvimPodId)
