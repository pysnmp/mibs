#
# PySNMP MIB module CISCO-OPTICAL-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-OPTICAL-MONITOR-CAPABILITY
# Source digest sha256:33305376e77b2b7a98e8afff64194e93993018601cc398da4ff029ec10d14b0d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
OpticalAlarmSeverityOrZero, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalAlarmSeverityOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoOpticalMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 528))
ciscoOpticalMonitorCapability.setRevisions(('2007-01-08 00:00',))
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setLastUpdated('2007-01-08 00:00')
if mibBuilder.loadTexts: ciscoOpticalMonitorCapability.setOrganization('Cisco Systems, Inc.')
ciscoOpticalMonCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 528, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOpticalMonCapCatOSV08R0601 = ciscoOpticalMonCapCatOSV08R0601.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-MONITOR-CAPABILITY", PYSNMP_MODULE_ID=ciscoOpticalMonitorCapability, ciscoOpticalMonCapCatOSV08R0601=ciscoOpticalMonCapCatOSV08R0601, ciscoOpticalMonitorCapability=ciscoOpticalMonitorCapability)
