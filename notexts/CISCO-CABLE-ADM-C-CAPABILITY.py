#
# PySNMP MIB module CISCO-CABLE-ADM-C-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CABLE-ADM-C-CAPABILITY
# Source digest sha256:65632a172f51af52ab1df981bac1644d9f675402d9cc83874b3c1da4c9f61ebd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableAdmCtrlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 427))
ciscoCableAdmCtrlCapability.setRevisions(('2004-12-11 00:00',))
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setLastUpdated('2004-12-11 00:00')
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setOrganization('Cisco Systems, Inc.')
ciscoCableAdmCtrlCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 427, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableAdmCtrlCapabilityV12R00 = ciscoCableAdmCtrlCapabilityV12R00.setProductRelease('Cisco IOS 12.3BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableAdmCtrlCapabilityV12R00 = ciscoCableAdmCtrlCapabilityV12R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-CABLE-ADM-C-CAPABILITY", PYSNMP_MODULE_ID=ciscoCableAdmCtrlCapability, ciscoCableAdmCtrlCapability=ciscoCableAdmCtrlCapability, ciscoCableAdmCtrlCapabilityV12R00=ciscoCableAdmCtrlCapabilityV12R00)
