#
# PySNMP MIB module CISCO-LINK-ERROR-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LINK-ERROR-MONITOR-CAPABILITY
# Source digest sha256:9c4b5f265749019f8feb9bd94dc00fc9ad1e4292701ee3162e7b584c7d7890ed
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLinkErrorMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 414))
ciscoLinkErrorMonitorCapability.setRevisions(('2004-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setLastUpdated('2004-08-05 00:00')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setDescription('This MIB module describes the capability \n                 of CISCO-LINK-ERROR-MONITOR-MIB.')
clemCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 414, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: clemCapCatOSV08R0401.setDescription('CISCO-LINK-ERROR-MONITOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LINK-ERROR-MONITOR-CAPABILITY", PYSNMP_MODULE_ID=ciscoLinkErrorMonitorCapability, ciscoLinkErrorMonitorCapability=ciscoLinkErrorMonitorCapability, clemCapCatOSV08R0401=clemCapCatOSV08R0401)
