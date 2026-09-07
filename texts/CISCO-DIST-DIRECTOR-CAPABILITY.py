#
# PySNMP MIB module CISCO-DIST-DIRECTOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DIST-DIRECTOR-CAPABILITY
# Source digest sha256:5c025c57c577960f190eaad8953209078e22f1c6ba1988ec1d5b89054267f394
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDistDirCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 267))
ciscoDistDirCapability.setRevisions(('2002-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDistDirCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDistDirCapability.setLastUpdated('2002-04-23 00:00')
if mibBuilder.loadTexts: ciscoDistDirCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDistDirCapability.setContactInfo('\tCisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal:\t170 West Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\n\t\t   Tel:\t+1 800 553-NETS\n\n\t\tE-mail:\tcs-dd@cisco.com')
if mibBuilder.loadTexts: ciscoDistDirCapability.setDescription('Agent capabilities for CISCO-DIST-DIRECTOR-MIB')
ciscoDistDirCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 267, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setProductRelease('Cisco IOS 12.2(8)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoDistDirCapabilityV12R02.setDescription('Cisco Distributed Director MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIST-DIRECTOR-CAPABILITY", PYSNMP_MODULE_ID=ciscoDistDirCapability, ciscoDistDirCapability=ciscoDistDirCapability, ciscoDistDirCapabilityV12R02=ciscoDistDirCapabilityV12R02)
