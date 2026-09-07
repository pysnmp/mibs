#
# PySNMP MIB module CISCO-OTN-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-OTN-IF-CAPABILITY
# Source digest sha256:0a58d9b1ea5ea737775f01f8550fd302fb6b2bbb165858382bdcce61198068dd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoOtnIfMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 562))
ciscoOtnIfMIBCapability.setRevisions(('2007-10-20 00:00',))
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setLastUpdated('2007-10-20 00:00')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setOrganization('Cisco Systems, Inc.')
ciscoOtnIfCapIOSXRV3R06CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 562, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtnIfCapIOSXRV3R06CRS1 = ciscoOtnIfCapIOSXRV3R06CRS1.setProductRelease('Cisco IOS-XR Release 3.6 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtnIfCapIOSXRV3R06CRS1 = ciscoOtnIfCapIOSXRV3R06CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-OTN-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoOtnIfMIBCapability, ciscoOtnIfCapIOSXRV3R06CRS1=ciscoOtnIfCapIOSXRV3R06CRS1, ciscoOtnIfMIBCapability=ciscoOtnIfMIBCapability)
