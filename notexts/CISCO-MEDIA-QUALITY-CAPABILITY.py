#
# PySNMP MIB module CISCO-MEDIA-QUALITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MEDIA-QUALITY-CAPABILITY
# Source digest sha256:440d25ca5bd4db6e1175c4ef4a0c588de9004291e29bb5949bdc5b3a210f65ff
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMediaQualityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 604))
ciscoMediaQualityCapability.setRevisions(('2011-09-23 00:00', '2011-04-15 00:00',))
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setLastUpdated('2011-09-23 00:00')
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setOrganization('Cisco Systems, Inc.')
ciscoMediaQualityCapabilityV152R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setStatus('current')
ciscoMediaQualityCapabilityV152R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c28xx,c3825,c3845,c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEDIA-QUALITY-CAPABILITY", PYSNMP_MODULE_ID=ciscoMediaQualityCapability, ciscoMediaQualityCapability=ciscoMediaQualityCapability, ciscoMediaQualityCapabilityV152R01=ciscoMediaQualityCapabilityV152R01, ciscoMediaQualityCapabilityV152R02=ciscoMediaQualityCapabilityV152R02)
