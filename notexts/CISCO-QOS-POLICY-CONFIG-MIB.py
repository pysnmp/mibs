#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-QOS-POLICY-CONFIG-MIB
# Source digest sha256:21d37ead967edb591f0cde00adac22f8f883ec73603cfff2010c896d96bbaea7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
QosInterfaceQueueType, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "QosInterfaceQueueType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoQosPolicyConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 159))
ciscoQosPolicyConfigMIB.setRevisions(('2000-11-02 10:30', '2000-02-26 19:30',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setLastUpdated('2000-11-02 10:30')
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setOrganization('Cisco Systems Inc.')
class QosPolicySource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("local", 2), ("cops", 3))

ciscoQosPolicyConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1))
qosPolicyGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1))
qosPolicyInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2))
qosEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEnabled.setStatus('current')
qosPrAdminPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 2), QosPolicySource().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosPrAdminPolicySource.setStatus('current')
qosPrOperPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 3), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPrOperPolicySource.setStatus('current')
qosRsvpAdminPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 4), QosPolicySource().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosRsvpAdminPolicySource.setStatus('current')
qosRsvpOperPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 5), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosRsvpOperPolicySource.setStatus('current')
qosCopsPolicyStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keep", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCopsPolicyStatus.setStatus('current')
qosPrIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: qosPrIfTable.setStatus('current')
qosPrIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qosPrIfEntry.setStatus('current')
qosPrIfAdminPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 1), QosPolicySource().clone('cops')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosPrIfAdminPolicySource.setStatus('current')
qosPrIfOperPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 2), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPrIfOperPolicySource.setStatus('current')
qosIfCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: qosIfCapabilityTable.setStatus('current')
qosIfCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfDirection"), (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfQType"))
if mibBuilder.loadTexts: qosIfCapabilityEntry.setStatus('current')
qosIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2), ("both", 3)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: qosIfDirection.setStatus('current')
qosIfQType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 2), QosInterfaceQueueType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: qosIfQType.setStatus('current')
qosIfCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 3), Bits().clone(namedValues=NamedValues(("unspecified", 0), ("inputL2Classification", 1), ("inputIpClassification", 2), ("outputL2Classification", 3), ("outputIpClassification", 4), ("inputPortClassification", 19), ("outputPortClassification", 20), ("inputUflowPolicing", 5), ("inputAggregatePolicing", 6), ("outputUflowPolicing", 7), ("outputAggregatePolicing", 8), ("policeByMarkingDown", 9), ("policeByDropping", 10), ("inputUflowShaping", 21), ("inputAggregateShaping", 22), ("outputUflowShaping", 23), ("outputAggregateShaping", 24), ("fifo", 11), ("wrr", 12), ("wfq", 13), ("cq", 14), ("pq", 15), ("cbwfq", 16), ("pqWrr", 25), ("pqCbwfq", 26), ("tailDrop", 17), ("wred", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosIfCapabilities.setStatus('current')
ciscoQosPolicyMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 2))
ciscoQosPolicyConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3))
ciscoQosPolicyConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1))
ciscoQosPolicyConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2))
ciscoQosPolicyConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1, 1)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrInterfaceGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosInterfaceCapabilityGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPolicyConfigMIBCompliance = ciscoQosPolicyConfigMIBCompliance.setStatus('current')
qosGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 1)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosGlobalGroup = qosGlobalGroup.setStatus('current')
qosPrGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 2)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPrGlobalGroup = qosPrGlobalGroup.setStatus('current')
qosRsvpGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 3)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosRsvpGlobalGroup = qosRsvpGlobalGroup.setStatus('current')
qosPrInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 4)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPrInterfaceGroup = qosPrInterfaceGroup.setStatus('current')
qosInterfaceCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 5)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosIfCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosInterfaceCapabilityGroup = qosInterfaceCapabilityGroup.setStatus('current')
qosCopsPolicyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 6)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosCopsPolicyStatusGroup = qosCopsPolicyStatusGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-MIB", PYSNMP_MODULE_ID=ciscoQosPolicyConfigMIB, QosPolicySource=QosPolicySource, ciscoQosPolicyConfigMIB=ciscoQosPolicyConfigMIB, ciscoQosPolicyConfigMIBCompliance=ciscoQosPolicyConfigMIBCompliance, ciscoQosPolicyConfigMIBCompliances=ciscoQosPolicyConfigMIBCompliances, ciscoQosPolicyConfigMIBConformance=ciscoQosPolicyConfigMIBConformance, ciscoQosPolicyConfigMIBGroups=ciscoQosPolicyConfigMIBGroups, ciscoQosPolicyConfigMIBObjects=ciscoQosPolicyConfigMIBObjects, ciscoQosPolicyMIBNotifications=ciscoQosPolicyMIBNotifications, qosCopsPolicyStatus=qosCopsPolicyStatus, qosCopsPolicyStatusGroup=qosCopsPolicyStatusGroup, qosEnabled=qosEnabled, qosGlobalGroup=qosGlobalGroup, qosIfCapabilities=qosIfCapabilities, qosIfCapabilityEntry=qosIfCapabilityEntry, qosIfCapabilityTable=qosIfCapabilityTable, qosIfDirection=qosIfDirection, qosIfQType=qosIfQType, qosInterfaceCapabilityGroup=qosInterfaceCapabilityGroup, qosPolicyGlobalObjects=qosPolicyGlobalObjects, qosPolicyInterfaceObjects=qosPolicyInterfaceObjects, qosPrAdminPolicySource=qosPrAdminPolicySource, qosPrGlobalGroup=qosPrGlobalGroup, qosPrIfAdminPolicySource=qosPrIfAdminPolicySource, qosPrIfEntry=qosPrIfEntry, qosPrIfOperPolicySource=qosPrIfOperPolicySource, qosPrIfTable=qosPrIfTable, qosPrInterfaceGroup=qosPrInterfaceGroup, qosPrOperPolicySource=qosPrOperPolicySource, qosRsvpAdminPolicySource=qosRsvpAdminPolicySource, qosRsvpGlobalGroup=qosRsvpGlobalGroup, qosRsvpOperPolicySource=qosRsvpOperPolicySource)
