#
# PySNMP MIB module CISCO-HC-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-HC-RMON-CAPABILITY
# Source digest sha256:d1eac32669b932f2374ce466fdfbcedecabb7913f2f9dbc875f3b66e5936010d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHcRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 358))
ciscoHcRmonCapability.setRevisions(('2003-09-30 00:00',))
if mibBuilder.loadTexts: ciscoHcRmonCapability.setLastUpdated('2003-09-30 00:00')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setOrganization('Cisco Systems, Inc.')
ciscoHcRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-HC-RMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoHcRmonCapability, ciscoHcRmonCapCatOSV08R0101=ciscoHcRmonCapCatOSV08R0101, ciscoHcRmonCapability=ciscoHcRmonCapability)
