#
# PySNMP MIB module CISCO-WAN-CELL-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-CELL-EXT-CAPABILITY
# Source digest sha256:7352db2df7c6bfc4b335441a279b9e4e1a29e9415c36ec4575a455a219dda0ec
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanCellExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 625))
ciscoWanCellExtCapability.setRevisions(('2014-03-21 00:00',))
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setLastUpdated('2014-03-21 00:00')
if mibBuilder.loadTexts: ciscoWanCellExtCapability.setOrganization('Cisco Systems, Inc.')
cwceCapV15R0501PIsr = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 625, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setProductRelease('Cisco IOS 15.5(1) Version on Cisco ISR\n                    3900/2900/1900/3800/2800/1800/800 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwceCapV15R0501PIsr = cwceCapV15R0501PIsr.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-CELL-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanCellExtCapability, ciscoWanCellExtCapability=ciscoWanCellExtCapability, cwceCapV15R0501PIsr=cwceCapV15R0501PIsr)
