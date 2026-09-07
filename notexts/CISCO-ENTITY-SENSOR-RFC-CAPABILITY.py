#
# PySNMP MIB module CISCO-ENTITY-SENSOR-RFC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-SENSOR-RFC-CAPABILITY
# Source digest sha256:3f11c41ae0c5f38cef0825a4d60a83af64a38d3f7de6cb02f134effeb914c527
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntitySensorRfcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 430))
ciscoEntitySensorRfcCapability.setRevisions(('2008-02-08 00:00', '2006-05-31 00:00', '2005-01-31 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setLastUpdated('2008-02-08 00:00')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setOrganization('Cisco Systems, Inc.')
cEntSensorRfcCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setStatus('current')
cEntSensorRfcCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setStatus('current')
cEntSensorRfcCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-RFC-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntitySensorRfcCapability, cEntSensorRfcCapACSWV03R000=cEntSensorRfcCapACSWV03R000, cEntSensorRfcCapCatOSV08R0501=cEntSensorRfcCapCatOSV08R0501, cEntSensorRfcCapc4710aceVA1R70=cEntSensorRfcCapc4710aceVA1R70, ciscoEntitySensorRfcCapability=ciscoEntitySensorRfcCapability)
