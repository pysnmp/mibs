#
# PySNMP MIB module CISCO-SYSAPPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SYSAPPL-CAPABILITY
# Source digest sha256:06b89321fe16c0e0a8b77e380ceef671537665b20626221f9cf22311c131c42f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSysApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSysApplCapability.setRevisions(('2007-09-14 00:00',))
if mibBuilder.loadTexts: ciscoSysApplCapability.setLastUpdated('2007-09-14 00:00')
if mibBuilder.loadTexts: ciscoSysApplCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysApplCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSAPPL-CAPABILITY", PYSNMP_MODULE_ID=ciscoSysApplCapability, ciscoSysApplCapability=ciscoSysApplCapability, ciscoSysApplCapabilityCTSV120=ciscoSysApplCapabilityCTSV120)
