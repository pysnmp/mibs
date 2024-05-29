#
# PySNMP MIB module SYNOLOGY-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed May 29 06:51:27 2024
# On host fv-az1776-875 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter32, Counter64, NotificationType, IpAddress, MibIdentifier, iso, ObjectIdentity, ModuleIdentity, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "Counter64", "NotificationType", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "ModuleIdentity", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 1))
synoSystem.setRevisions(('2013-09-11 00:00',))
if mibBuilder.loadTexts: synoSystem.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoSystem.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
powerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('current')
fan = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 4))
systemFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemFanStatus.setStatus('current')
cpuFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuFanStatus.setStatus('current')
dsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 5))
modelName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modelName.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
version = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
upgradeAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgradeAvailable.setStatus('current')
systemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6))
systemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6, 1))
systemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6, 2))
systemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 1, 6, 1, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemCompliance = systemCompliance.setStatus('current')
systemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 1, 6, 2, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemStatus"), ("SYNOLOGY-SYSTEM-MIB", "temperature"), ("SYNOLOGY-SYSTEM-MIB", "powerStatus"), ("SYNOLOGY-SYSTEM-MIB", "systemFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "cpuFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "modelName"), ("SYNOLOGY-SYSTEM-MIB", "serialNumber"), ("SYNOLOGY-SYSTEM-MIB", "version"), ("SYNOLOGY-SYSTEM-MIB", "upgradeAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemGroup = systemGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-SYSTEM-MIB", systemGroup=systemGroup, serialNumber=serialNumber, systemGroups=systemGroups, synology=synology, modelName=modelName, systemConformance=systemConformance, upgradeAvailable=upgradeAvailable, powerStatus=powerStatus, fan=fan, temperature=temperature, systemCompliance=systemCompliance, synoSystem=synoSystem, systemCompliances=systemCompliances, PYSNMP_MODULE_ID=synoSystem, cpuFanStatus=cpuFanStatus, systemStatus=systemStatus, systemFanStatus=systemFanStatus, version=version, dsmInfo=dsmInfo)
