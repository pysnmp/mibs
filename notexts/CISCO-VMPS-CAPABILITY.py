#
# PySNMP MIB module CISCO-VMPS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VMPS-CAPABILITY
# Source digest sha256:894d4a9c88394fd96005a9648c0f0fff1c6bdf05760b221e09af878cf0ac3223
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
ciscoVmpsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 365))
ciscoVmpsCapability.setRevisions(('2004-04-07 00:00', '2004-03-12 00:00', '2003-10-31 00:00',))
if mibBuilder.loadTexts: ciscoVmpsCapability.setLastUpdated('2004-04-07 00:00')
if mibBuilder.loadTexts: ciscoVmpsCapability.setOrganization('Cisco Systems, Inc.')
ciscoVmpsCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setStatus('current')
ciscoVmpsCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setStatus('current')
ciscoVmpsCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setStatus('current')
mibBuilder.exportSymbols("CISCO-VMPS-CAPABILITY", PYSNMP_MODULE_ID=ciscoVmpsCapability, ciscoVmpsCapCatOSV08R0101=ciscoVmpsCapCatOSV08R0101, ciscoVmpsCapCatOSV08R0301=ciscoVmpsCapCatOSV08R0301, ciscoVmpsCapCatOSV08R0401=ciscoVmpsCapCatOSV08R0401, ciscoVmpsCapability=ciscoVmpsCapability)
