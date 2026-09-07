#
# PySNMP MIB module CISCO-PFC-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PFC-EXT-CAPABILITY
# Source digest sha256:7380e6f0d9cec5766f67c89262f79378c9fffbd8cda105221c8decbf2cb90dff
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPfcExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 626))
ciscoPfcExtCapability.setRevisions(('2014-08-11 00:00',))
if mibBuilder.loadTexts: ciscoPfcExtCapability.setLastUpdated('2014-08-11 00:00')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setOrganization('Cisco Systems, Inc.')
cpeCapNxOSV06R0002U0201PN3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 626, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus \n                        3000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setStatus('current')
mibBuilder.exportSymbols("CISCO-PFC-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoPfcExtCapability, ciscoPfcExtCapability=ciscoPfcExtCapability, cpeCapNxOSV06R0002U0201PN3k=cpeCapNxOSV06R0002U0201PN3k)
