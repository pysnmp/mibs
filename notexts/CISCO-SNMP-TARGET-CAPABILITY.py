#
# PySNMP MIB module CISCO-SNMP-TARGET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-TARGET-CAPABILITY
# Source digest sha256:1b8807eb2b634393509c630f6d9e94146e45b54480f91b26194a877075712d8f
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
ciscoSnmpTargetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 359))
ciscoSnmpTargetCapability.setRevisions(('2008-07-21 00:00', '2007-06-22 00:00', '2006-04-11 00:00', '2004-07-28 00:00', '2003-09-16 00:00',))
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setLastUpdated('2008-07-21 00:00')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpTargetCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setStatus('current')
ciscoSnmpTargetCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setProductRelease('Cisco VISM Release 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setStatus('current')
ciscoSnmpTargetCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setStatus('current')
ciscoSnmpTargetCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpTargetCapability, ciscoSnmpTargetCapACSWV03R000=ciscoSnmpTargetCapACSWV03R000, ciscoSnmpTargetCapCatOSV05R0501=ciscoSnmpTargetCapCatOSV05R0501, ciscoSnmpTargetCapVISM33=ciscoSnmpTargetCapVISM33, ciscoSnmpTargetCapability=ciscoSnmpTargetCapability, ciscoSnmpTargetCapc4710aceVA1R700=ciscoSnmpTargetCapc4710aceVA1R700)
