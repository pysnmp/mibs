#
# PySNMP MIB module CISCO-SYS-INFO-LOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SYS-INFO-LOG-CAPABILITY
# Source digest sha256:a0ce7dd8621e679557e0f9f1447d5e20388803618dbda2209914de0442d2feab
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSysInfoLogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 321))
ciscoSysInfoLogCapability.setRevisions(('2005-08-24 00:00', '2003-08-01 00:00',))
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setLastUpdated('2005-08-24 00:00')
if mibBuilder.loadTexts: ciscoSysInfoLogCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysInfoLogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0101 = ciscoSysInfoLogCapCatOSV08R0101.setStatus('current')
ciscoSysInfoLogCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysInfoLogCapCatOSV08R0501 = ciscoSysInfoLogCapCatOSV08R0501.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYS-INFO-LOG-CAPABILITY", PYSNMP_MODULE_ID=ciscoSysInfoLogCapability, ciscoSysInfoLogCapCatOSV08R0101=ciscoSysInfoLogCapCatOSV08R0101, ciscoSysInfoLogCapCatOSV08R0501=ciscoSysInfoLogCapCatOSV08R0501, ciscoSysInfoLogCapability=ciscoSysInfoLogCapability)
