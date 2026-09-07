#
# PySNMP MIB module CISCO-FTP-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FTP-CLIENT-CAPABILITY
# Source digest sha256:6bc1545a7a689cc7eccf5284f388dcbe91eaaca173fd43289fb02034cafb6b42
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cftpclientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 483))
cftpclientCapability.setRevisions(('2006-01-02 00:00',))
if mibBuilder.loadTexts: cftpclientCapability.setLastUpdated('2006-01-02 00:00')
if mibBuilder.loadTexts: cftpclientCapability.setOrganization('Cisco Systems, Inc.')
cftpclientCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 483, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cftpclientCapabilityIOSXRV2R0CRS1 = cftpclientCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cftpclientCapabilityIOSXRV2R0CRS1 = cftpclientCapabilityIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FTP-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=cftpclientCapability, cftpclientCapability=cftpclientCapability, cftpclientCapabilityIOSXRV2R0CRS1=cftpclientCapabilityIOSXRV2R0CRS1)
