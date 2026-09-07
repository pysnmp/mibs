#
# PySNMP MIB module CISCO-DISMAN-EXPRESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DISMAN-EXPRESSION-CAPABILITY
# Source digest sha256:bf3d0c5086752e82a849bf8a9c06738915112186cd0c12dc156031c2806ff14f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cdismanExpressionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 484))
cdismanExpressionCapability.setRevisions(('2006-02-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cdismanExpressionCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cdismanExpressionCapability.setLastUpdated('2006-02-16 00:00')
if mibBuilder.loadTexts: cdismanExpressionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cdismanExpressionCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: cdismanExpressionCapability.setDescription('The capabilities description of\n                 DISMAN-EXPRESSION-MIB.')
cdismanExpressionCapIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 484, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanExpressionCapIOSXRV3R2R0CRS1 = cdismanExpressionCapIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanExpressionCapIOSXRV3R2R0CRS1 = cdismanExpressionCapIOSXRV3R2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cdismanExpressionCapIOSXRV3R2R0CRS1.setDescription('DISMAN-EXPRESSION-MIB capabilities for\n                        IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-DISMAN-EXPRESSION-CAPABILITY", PYSNMP_MODULE_ID=cdismanExpressionCapability, cdismanExpressionCapIOSXRV3R2R0CRS1=cdismanExpressionCapIOSXRV3R2R0CRS1, cdismanExpressionCapability=cdismanExpressionCapability)
