#
# PySNMP MIB module CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY
# Source digest sha256:8cac8f2d924dc29d443c7aa9642147ba3a8161524e37248eeec13eb727312caf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwAnnouncementCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 354))
cwAnnouncementCapability.setRevisions(('2001-10-11 00:00',))
if mibBuilder.loadTexts: cwAnnouncementCapability.setLastUpdated('2001-12-26 00:00')
if mibBuilder.loadTexts: cwAnnouncementCapability.setOrganization('Cisco Systems, Inc.')
cwAnnouncementCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 354, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAnnouncementCapabilityV3R00 = cwAnnouncementCapabilityV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-ANNOUNCEMENT-CAPABILITY", PYSNMP_MODULE_ID=cwAnnouncementCapability, cwAnnouncementCapability=cwAnnouncementCapability, cwAnnouncementCapabilityV3R00=cwAnnouncementCapabilityV3R00)
