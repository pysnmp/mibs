#
# PySNMP MIB module CISCO-LLDP-EXT-MED-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LLDP-EXT-MED-CAPABILITY
# Source digest sha256:b6b964145f1effbd846e74cff435e51020b1fad6bfc48d9240e9282f799e6d99
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLldpExtMedCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 584))
ciscoLldpExtMedCapability.setRevisions(('2009-12-02 00:00',))
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setLastUpdated('2009-12-02 00:00')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setOrganization('Cisco Systems, Inc.')
lldpExtMedCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 584, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setProductRelease('Cisco IOS 12.2SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setStatus('current')
mibBuilder.exportSymbols("CISCO-LLDP-EXT-MED-CAPABILITY", PYSNMP_MODULE_ID=ciscoLldpExtMedCapability, ciscoLldpExtMedCapability=ciscoLldpExtMedCapability, lldpExtMedCapability1=lldpExtMedCapability1)
