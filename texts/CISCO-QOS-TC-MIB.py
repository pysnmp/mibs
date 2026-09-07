#
# PySNMP MIB module CISCO-QOS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-QOS-TC-MIB
# Source digest sha256:faf35e774dd3d5e08c9a988d309bca48e753be91733350a39bcbd3c3401ac107
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 573))
ciscoQosTcMIB.setRevisions(('2007-03-05 00:00', '2006-09-18 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosTcMIB.setRevisionsDescriptions(('Add QosPolicerType textual convention.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosTcMIB.setLastUpdated('2007-03-05 00:00')
if mibBuilder.loadTexts: ciscoQosTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosTcMIB.setContactInfo('       Cisco Systems\n                Customer Service\n        \n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n        \n           Tel: +1 800 553-NETS\n        \n        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosTcMIB.setDescription('This module defines the textual conventions used within\n         Cisco Qos MIBs.')
class QosIpPrecedence(TextualConvention, Unsigned32):
    reference = 'RFC791 INTERNET PROTOCOL, Chapter 3.1'
    description = 'Indicates the IP precedence.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosQueueNumber(TextualConvention, Unsigned32):
    description = 'An integer indicates a queue number.'
    status = 'current'

class QosThresholdNumber(TextualConvention, Unsigned32):
    description = 'An integer indicates a threshold number.'
    status = 'current'

class QosMplsExpValue(TextualConvention, Unsigned32):
    description = 'An integer indicates a MPLS-EXP (experimental) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosMutationMapName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of a mutation map.'
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 99)

class QosMutationMapNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n        QosMutationMapName convention. The latter defines a\n        non-empty mutation map name. This extension permits\n        the addtional value of empty string.'
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 99)

class QosPolicerType(TextualConvention, Integer32):
    description = 'An integer indicating the type of a QoS policer.\n\n         microflow(1):     a microflow policer.\n         aggregate(2):     an aggregate policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("microflow", 1), ("aggregate", 2))

mibBuilder.exportSymbols("CISCO-QOS-TC-MIB", PYSNMP_MODULE_ID=ciscoQosTcMIB, QosIpPrecedence=QosIpPrecedence, QosMplsExpValue=QosMplsExpValue, QosMutationMapName=QosMutationMapName, QosMutationMapNameOrEmpty=QosMutationMapNameOrEmpty, QosPolicerType=QosPolicerType, QosQueueNumber=QosQueueNumber, QosThresholdNumber=QosThresholdNumber, ciscoQosTcMIB=ciscoQosTcMIB)
