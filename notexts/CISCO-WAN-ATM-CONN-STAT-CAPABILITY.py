#
# PySNMP MIB module CISCO-WAN-ATM-CONN-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-ATM-CONN-STAT-CAPABILITY
# Source digest sha256:abcbc51c6e6abd8c6b5131e47db9fdcccfccab9910a4f2bccf426f56699bdaaf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanAtmConnStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoWanAtmConnStatCapability.setRevisions(('2003-04-08 00:00', '2001-03-21 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setLastUpdated('2003-04-08 00:00')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setOrganization('Cisco Systems, Inc.')
cwaConnStatCapabilityAxsmV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setStatus('current')
cwAtmConnStatCapabilityAxsmeV2R0170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setProductRelease('MGX8850 Release 2.1.70')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setStatus('current')
cwAtmConnStatCapabilityPxm1eV2R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setStatus('current')
cwacsCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-STAT-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanAtmConnStatCapability, ciscoWanAtmConnStatCapability=ciscoWanAtmConnStatCapability, cwAtmConnStatCapabilityAxsmeV2R0170=cwAtmConnStatCapabilityAxsmeV2R0170, cwAtmConnStatCapabilityPxm1eV2R300=cwAtmConnStatCapabilityPxm1eV2R300, cwaConnStatCapabilityAxsmV21R60=cwaConnStatCapabilityAxsmV21R60, cwacsCapabilityAxsmxgV4R00=cwacsCapabilityAxsmxgV4R00)
