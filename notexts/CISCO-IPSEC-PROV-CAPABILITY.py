#
# PySNMP MIB module CISCO-IPSEC-PROV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPSEC-PROV-CAPABILITY
# Source digest sha256:a3ca1a7b40844d594ca231800a43cdd9a940c1503911277086d4b0ff3c34cfcc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPsecProvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 486))
ciscoIPsecProvCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setLastUpdated('2006-02-02 00:00')
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setOrganization('Cisco Systems, Inc.')
cIPsecProvCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 486, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecProvCapSanOSV30R1MDS9000 = cIPsecProvCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecProvCapSanOSV30R1MDS9000 = cIPsecProvCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSEC-PROV-CAPABILITY", PYSNMP_MODULE_ID=ciscoIPsecProvCapability, cIPsecProvCapSanOSV30R1MDS9000=cIPsecProvCapSanOSV30R1MDS9000, ciscoIPsecProvCapability=ciscoIPsecProvCapability)
