#
# PySNMP MIB module CISCO-SLB-DFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SLB-DFP-MIB
# Source digest sha256:8037c797c9115552e9230e5d3f43ddb5ba6dab50049832f5586a138e5fbdd4c7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbDfpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 689))
ciscoSlbDfpMIB.setRevisions(('2009-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbDfpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setLastUpdated('2009-01-29 00:00')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal:170 W. Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel:+1 800 553-NETS\n\n\n            E-mail:cs-asngw@cisco.com')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setDescription('This MIB reports the congestion status of the real server.\n        A server can be in congested state due to high memory\n        consumption, high CPU utilization or high number of clients\n        being served by it. Congestion can cause delay in server\n        response time.\n        DFP (Dynamic Feedback Protocol) weight values are used as a\n        metric to monitor the congestion of the server.\n\n        This MIB generates notifications when congestion state\n        is detected on the real server.   \n        DFP weight is calculated as follows\n\n        BindingWeight=(Maxbindings-numberOfBindings)/Maxbindings\n\n        CPUMemWeight=(cpu + mem)/32\n\n        Weight = BindingWeight*CPUMemWeight*dfp_max_weight\n\n        Here,\n         - Maxbindings is the maximum number of bindings allowed on the\n        server.\n         - dfp_max_weight is the maximum possible value of DFP weight\n        (24).\n         - numberOfBindings is the number of mobile bindings currently\n        present with the server.\n\n        The DFP weight at which congestion is detected is configurable.\n         If the DFP weight of the system falls below this value, then\n        the system is treated as congested and notification is\n        generated.')
ciscoSlbDfpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 0))
ciscoSlbDfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 1))
ciscoSlbDfpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2))
cslbcDfpCongestionThresholdType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reject", 1), ("abort", 2), ("redirect", 3), ("drop", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cslbcDfpCongestionThresholdType.setStatus('current')
if mibBuilder.loadTexts: cslbcDfpCongestionThresholdType.setDescription('This object specifies the action taken when the congestion\n        threshold is reached.\n        The valid congestion action type are\n        o reject - Incoming registration requests will be rejected when\n        this congestion type is configured.\n        o abort - Registration request being processed will be aborted\n        when this congestion type is configured.\n        o redirect - Incoming registration requests will be redirected\n        to another Home Agent when this congestion type is configured.\n        o drop - Existing idle mobile IP bindings will be dropped when\n        this congestion type is configured.\n\n        A mobile IP binding is a record present with the server that \n        associates the home address given to the mobile node by its\n        home network with the care of address granted to it by the\n        foreign network while it is roaming.  \n        The Home Agent is a real server that maintains mobile \n        bindings.')
cslbcProcessorDfpValTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cslbcProcessorDfpValTable.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValTable.setDescription('This table lists the DFP status for each processor for which\n        DFP weights are monitored.')
cslbcProcessorDfpValEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValPhysicalIndex"))
if mibBuilder.loadTexts: cslbcProcessorDfpValEntry.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValEntry.setDescription('The entry contains DFP value for one processor.\n        A row is added to this table when congestion needs to be\n        monitored on a processor. Row is deleted when congestion no\n        longer needs to be monitored.')
cslbcProcessorDfpValPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 1), EntPhysicalIndexOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cslbcProcessorDfpValPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValPhysicalIndex.setDescription('This element contains the index of the physical entity or\n        identifier of the processor for which the DFP value is\n        maintained.')
cslbcProcessorDfpValDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDescription.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValDescription.setDescription('This element contains the description for the congestion\n        configured on for processor.')
class CslbcDfpValue(TextualConvention, Unsigned32):
    description = 'This textual convention defines valid ranges DFP values\n        similar to slbDfpRealWeight object defined in CISCO-SLB-MIB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cslbcDfpCongestionOnsetThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 1), CslbcDfpValue().clone(0)).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionOnsetThreshold.setStatus('current')
if mibBuilder.loadTexts: cslbcDfpCongestionOnsetThreshold.setDescription('This object specifes when congestion occurs.  When the DFP\n        level of the system drops below this value, the system is\n        marked as congested.  This value is same for all the\n        processors.')
cslbcDfpCongestionAbateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 2), CslbcDfpValue().clone(0)).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionAbateThreshold.setStatus('current')
if mibBuilder.loadTexts: cslbcDfpCongestionAbateThreshold.setDescription('This object specifies when decongestion occurs.  When the DFP\n        level of the system rises above this value, the system is\n        marked as decongested.  This value is same for all processors.')
cslbcProcessorDfpValDfpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 3), CslbcDfpValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDfpValue.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValDfpValue.setDescription('This object indicates DFP value for the processor.')
cslbcSlbDfpCongestionOnset = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionOnset.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpCongestionOnset.setDescription('The server generates this notification when value of\n        cslbcInstanceDfpValue object drops below the threshold\n        indicated\n        by the cslbcDfpCongestionOnsetThreshold object.')
cslbcSlbDfpCongestionAbate = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionAbate.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpCongestionAbate.setDescription('The server generates this notification when value of\n        cslbcInstanceDfpValue object rises above the threshold\n        indicated\n        by the cslbcDfpCongestionAbateThreshold object.')
ciscoSlbDfpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1))
ciscoSlbDfpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2))
ciscoSlbDfpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1, 1)).setObjects(("CISCO-SLB-DFP-MIB", "ciscoSlbDfpInstanceGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpScalarsGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpMIBCompliance = ciscoSlbDfpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbDfpMIBCompliance.setDescription('The compliance statement for entities which implement\n        ciscoSlbDfp MIB module.')
ciscoSlbDfpInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpInstanceGroup = ciscoSlbDfpInstanceGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbDfpInstanceGroup.setDescription('This group represents the fields that identifies the processor\n        and associated DFP value.')
cslbcSlbDfpScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpScalarsGroup = cslbcSlbDfpScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpScalarsGroup.setDescription('This group represents the set of thresholds against which the\n        DFP value is compared.')
cslbcSlbDfpCongestionGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 3)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionOnset"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionAbate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpCongestionGroup = cslbcSlbDfpCongestionGroup.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpCongestionGroup.setDescription('This groutp represents the group of notifications on Home\n        Agent.')
mibBuilder.exportSymbols("CISCO-SLB-DFP-MIB", CslbcDfpValue=CslbcDfpValue, PYSNMP_MODULE_ID=ciscoSlbDfpMIB, ciscoSlbDfpInstanceGroup=ciscoSlbDfpInstanceGroup, ciscoSlbDfpMIB=ciscoSlbDfpMIB, ciscoSlbDfpMIBCompliance=ciscoSlbDfpMIBCompliance, ciscoSlbDfpMIBCompliances=ciscoSlbDfpMIBCompliances, ciscoSlbDfpMIBConform=ciscoSlbDfpMIBConform, ciscoSlbDfpMIBGroups=ciscoSlbDfpMIBGroups, ciscoSlbDfpMIBNotifs=ciscoSlbDfpMIBNotifs, ciscoSlbDfpMIBObjects=ciscoSlbDfpMIBObjects, cslbcDfpCongestionAbateThreshold=cslbcDfpCongestionAbateThreshold, cslbcDfpCongestionOnsetThreshold=cslbcDfpCongestionOnsetThreshold, cslbcDfpCongestionThresholdType=cslbcDfpCongestionThresholdType, cslbcProcessorDfpValDescription=cslbcProcessorDfpValDescription, cslbcProcessorDfpValDfpValue=cslbcProcessorDfpValDfpValue, cslbcProcessorDfpValEntry=cslbcProcessorDfpValEntry, cslbcProcessorDfpValPhysicalIndex=cslbcProcessorDfpValPhysicalIndex, cslbcProcessorDfpValTable=cslbcProcessorDfpValTable, cslbcSlbDfpCongestionAbate=cslbcSlbDfpCongestionAbate, cslbcSlbDfpCongestionGroup=cslbcSlbDfpCongestionGroup, cslbcSlbDfpCongestionOnset=cslbcSlbDfpCongestionOnset, cslbcSlbDfpScalarsGroup=cslbcSlbDfpScalarsGroup)
