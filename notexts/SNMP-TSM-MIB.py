#
# PySNMP MIB module SNMP-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SNMP-TSM-MIB
# Source digest sha256:490c57e44b1ff41050c227cded50c10c566c0140243e8c282434a25263aeccee
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
snmpTsmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 190))
snmpTsmMIB.setRevisions(('2009-06-09 00:00',))
if mibBuilder.loadTexts: snmpTsmMIB.setLastUpdated('2009-06-09 00:00')
if mibBuilder.loadTexts: snmpTsmMIB.setOrganization('ISMS Working Group')
snmpTsmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 0))
snmpTsmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1))
snmpTsmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2))
snmpTsmStats = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 1))
snmpTsmInvalidCaches = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidCaches.setStatus('current')
snmpTsmInadequateSecurityLevels = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInadequateSecurityLevels.setStatus('current')
snmpTsmUnknownPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmUnknownPrefixes.setStatus('current')
snmpTsmInvalidPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidPrefixes.setStatus('current')
snmpTsmConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 2))
snmpTsmConfigurationUsePrefix = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTsmConfigurationUsePrefix.setStatus('current')
snmpTsmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 1))
snmpTsmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 2))
snmpTsmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 190, 2, 1, 1)).setObjects(("SNMP-TSM-MIB", "snmpTsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmCompliance = snmpTsmCompliance.setStatus('current')
snmpTsmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 190, 2, 2, 2)).setObjects(("SNMP-TSM-MIB", "snmpTsmInvalidCaches"), ("SNMP-TSM-MIB", "snmpTsmInadequateSecurityLevels"), ("SNMP-TSM-MIB", "snmpTsmUnknownPrefixes"), ("SNMP-TSM-MIB", "snmpTsmInvalidPrefixes"), ("SNMP-TSM-MIB", "snmpTsmConfigurationUsePrefix"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmGroup = snmpTsmGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-TSM-MIB", PYSNMP_MODULE_ID=snmpTsmMIB, snmpTsmCompliance=snmpTsmCompliance, snmpTsmCompliances=snmpTsmCompliances, snmpTsmConfiguration=snmpTsmConfiguration, snmpTsmConfigurationUsePrefix=snmpTsmConfigurationUsePrefix, snmpTsmConformance=snmpTsmConformance, snmpTsmGroup=snmpTsmGroup, snmpTsmGroups=snmpTsmGroups, snmpTsmInadequateSecurityLevels=snmpTsmInadequateSecurityLevels, snmpTsmInvalidCaches=snmpTsmInvalidCaches, snmpTsmInvalidPrefixes=snmpTsmInvalidPrefixes, snmpTsmMIB=snmpTsmMIB, snmpTsmMIBObjects=snmpTsmMIBObjects, snmpTsmNotifications=snmpTsmNotifications, snmpTsmStats=snmpTsmStats, snmpTsmUnknownPrefixes=snmpTsmUnknownPrefixes)
