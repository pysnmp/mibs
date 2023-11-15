#
# PySNMP MIB module SYNOLOGY-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-SYSTEM-MIB
# Produced by pysmi-1.1.10 at Wed Nov 15 02:43:01 2023
# On host fv-az661-425 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter32, Integer32, ObjectIdentity, enterprises, NotificationType, Gauge32, ModuleIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter32", "Integer32", "ObjectIdentity", "enterprises", "NotificationType", "Gauge32", "ModuleIdentity", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SYNOLOGY-SYSTEM-MIB", serialNumber=serialNumber, systemCompliance=systemCompliance, version=version, systemGroup=systemGroup, temperature=temperature, fan=fan, systemFanStatus=systemFanStatus, powerStatus=powerStatus, systemCompliances=systemCompliances, modelName=modelName, PYSNMP_MODULE_ID=synoSystem, cpuFanStatus=cpuFanStatus, systemConformance=systemConformance, systemStatus=systemStatus, systemGroups=systemGroups, synology=synology, upgradeAvailable=upgradeAvailable, dsmInfo=dsmInfo, synoSystem=synoSystem)
