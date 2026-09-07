#
# PySNMP MIB module CISCO-RTTMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RTTMON-CAPABILITY
# Source digest sha256:9fdedd82430601d3297ac583b0f3ae7dfe520345bf0f505187b4b062e03d5e0b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRttMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 62))
ciscoRttMonCapability.setRevisions(('2006-03-02 00:00', '2005-12-14 00:00', '2005-06-09 00:00', '2005-05-01 00:00', '2004-05-31 00:00',))
if mibBuilder.loadTexts: ciscoRttMonCapability.setLastUpdated('2006-03-02 00:00')
if mibBuilder.loadTexts: ciscoRttMonCapability.setOrganization('Cisco Systems, Inc.')
ciscoRttMonCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setProductRelease('Cisco IOS 12.3(6th)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapabilityRev1 = ciscoRttMonCapabilityRev1.setStatus('current')
ciscoRttMonCapV12R0402ndT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setProductRelease('Cisco IOS 12.4(2nd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0402ndT = ciscoRttMonCapV12R0402ndT.setStatus('current')
ciscoRttMonCapV12R0206thSX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setProductRelease('Cisco IOS 12.2(6th)SX')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0206thSX = ciscoRttMonCapV12R0206thSX.setStatus('current')
ciscoRttMonCapV12R0403rdT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setProductRelease('Cisco IOS 12.4(3rd)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0403rdT = ciscoRttMonCapV12R0403rdT.setStatus('current')
ciscoRttMonCapCRS1V3R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setProductRelease('Cisco IOS XR release 3.3 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapCRS1V3R3 = ciscoRttMonCapCRS1V3R3.setStatus('current')
ciscoRttMonCapV12R0201SRB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 62, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRttMonCapV12R0201SRB = ciscoRttMonCapV12R0201SRB.setStatus('current')
mibBuilder.exportSymbols("CISCO-RTTMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoRttMonCapability, ciscoRttMonCapCRS1V3R3=ciscoRttMonCapCRS1V3R3, ciscoRttMonCapV12R0201SRB=ciscoRttMonCapV12R0201SRB, ciscoRttMonCapV12R0206thSX=ciscoRttMonCapV12R0206thSX, ciscoRttMonCapV12R0402ndT=ciscoRttMonCapV12R0402ndT, ciscoRttMonCapV12R0403rdT=ciscoRttMonCapV12R0403rdT, ciscoRttMonCapability=ciscoRttMonCapability, ciscoRttMonCapabilityRev1=ciscoRttMonCapabilityRev1)
