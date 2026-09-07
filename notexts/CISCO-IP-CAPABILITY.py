#
# PySNMP MIB module CISCO-IP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IP-CAPABILITY
# Source digest sha256:f1c6bd1f0874e39a58527b1a0c7e25347eb325e47447191262f4a81f9927bd29
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 445))
ciscoIpCapability.setRevisions(('2010-09-30 00:00', '2008-08-11 00:00', '2007-11-05 00:00', '2006-11-03 00:00', '2006-05-27 00:00', '2006-02-17 00:00', '2005-07-25 00:00',))
if mibBuilder.loadTexts: ciscoIpCapability.setLastUpdated('2010-09-30 00:00')
if mibBuilder.loadTexts: ciscoIpCapability.setOrganization('Cisco Systems, Inc.')
cIpCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapV320CRS1 = cIpCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapV320CRS1 = cIpCapV320CRS1.setStatus('current')
cIpCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapACSWV03R000 = cIpCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapACSWV03R000 = cIpCapACSWV03R000.setStatus('current')
cIpCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTSV100 = cIpCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTSV100 = cIpCapCTSV100.setStatus('current')
cIpCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTMV1000 = cIpCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapCTMV1000 = cIpCapCTMV1000.setStatus('current')
cIpCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapc4710aceVA1R700 = cIpCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpCapc4710aceVA1R700 = cIpCapc4710aceVA1R700.setStatus('current')
ciscoIpCapabilityV12R2SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 445, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpCapabilityV12R2SE = ciscoIpCapabilityV12R2SE.setProductRelease('Cisco IOS 12.2SE Catalyst 2k/3k Series.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpCapabilityV12R2SE = ciscoIpCapabilityV12R2SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpCapability, cIpCapACSWV03R000=cIpCapACSWV03R000, cIpCapCTMV1000=cIpCapCTMV1000, cIpCapCTSV100=cIpCapCTSV100, cIpCapV320CRS1=cIpCapV320CRS1, cIpCapc4710aceVA1R700=cIpCapc4710aceVA1R700, ciscoIpCapability=ciscoIpCapability, ciscoIpCapabilityV12R2SE=ciscoIpCapabilityV12R2SE)
