#
# PySNMP MIB module NETONIX-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netonix/NETONIX-SWITCH-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:36:12 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
snmpMIBGroups, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpMIBGroups")
Unsigned32, TimeTicks, Counter32, iso, ObjectIdentity, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, enterprises, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Counter32", "iso", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "enterprises", "NotificationType", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netonixSwitch = ModuleIdentity((1, 3, 6, 1, 4, 1, 46242))
netonixSwitch.setRevisions(('1998-03-23 18:00',))
if mibBuilder.loadTexts: netonixSwitch.setLastUpdated('9803231800Z')
if mibBuilder.loadTexts: netonixSwitch.setOrganization('Netonix')
netonixSwitchGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 8)).setObjects(("NETONIX-SWITCH-MIB", "firmwareVersion"), ("NETONIX-SWITCH-MIB", "fanSpeed"), ("NETONIX-SWITCH-MIB", "tempDescription"), ("NETONIX-SWITCH-MIB", "temp"), ("NETONIX-SWITCH-MIB", "voltageDescription"), ("NETONIX-SWITCH-MIB", "voltage"), ("NETONIX-SWITCH-MIB", "poeStatus"), ("NETONIX-SWITCH-MIB", "totalPowerConsumption"), ("NETONIX-SWITCH-MIB", "dcdcInputCurrent"), ("NETONIX-SWITCH-MIB", "dcdcEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    netonixSwitchGroup = netonixSwitchGroup.setStatus('current')
netonixSwitchConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 46242, 99))
netonixSwitchGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 46242, 99, 1))
netonixSwitchCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 46242, 99, 2))
netonixSwitchCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 46242, 99, 2, 1)).setObjects(("NETONIX-SWITCH-MIB", "netonixSwitchGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    netonixSwitchCompliance = netonixSwitchCompliance.setStatus('current')
class VoltageTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class PowerTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class CurrentTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 46242, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
totalPowerConsumption = MibScalar((1, 3, 6, 1, 4, 1, 46242, 6), PowerTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPowerConsumption.setStatus('current')
dcdcInputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 46242, 7), CurrentTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcdcInputCurrent.setStatus('current')
dcdcEfficiency = MibScalar((1, 3, 6, 1, 4, 1, 46242, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcdcEfficiency.setStatus('current')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 2), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 2, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: fanIndex.setStatus('current')
fanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSpeed.setStatus('current')
poeStatusTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 5), )
if mibBuilder.loadTexts: poeStatusTable.setStatus('current')
poeStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 5, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "poeStatusIndex"))
if mibBuilder.loadTexts: poeStatusEntry.setStatus('current')
poeStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: poeStatusIndex.setStatus('current')
poeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poeStatus.setStatus('current')
tempTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 3), )
if mibBuilder.loadTexts: tempTable.setStatus('current')
tempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 3, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "tempIndex"))
if mibBuilder.loadTexts: tempEntry.setStatus('current')
tempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: tempIndex.setStatus('current')
tempDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempDescription.setStatus('current')
temp = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temp.setStatus('current')
voltageTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 4), )
if mibBuilder.loadTexts: voltageTable.setStatus('current')
voltageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 4, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "voltageIndex"))
if mibBuilder.loadTexts: voltageEntry.setStatus('current')
voltageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: voltageIndex.setStatus('current')
voltageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageDescription.setStatus('current')
voltage = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 4, 1, 3), VoltageTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage.setStatus('current')
mibBuilder.exportSymbols("NETONIX-SWITCH-MIB", temp=temp, PYSNMP_MODULE_ID=netonixSwitch, VoltageTC=VoltageTC, dcdcEfficiency=dcdcEfficiency, voltageTable=voltageTable, poeStatusIndex=poeStatusIndex, voltageIndex=voltageIndex, netonixSwitchConformance=netonixSwitchConformance, firmwareVersion=firmwareVersion, fanIndex=fanIndex, voltageEntry=voltageEntry, tempDescription=tempDescription, totalPowerConsumption=totalPowerConsumption, dcdcInputCurrent=dcdcInputCurrent, netonixSwitchGroup=netonixSwitchGroup, netonixSwitchCompliance=netonixSwitchCompliance, tempEntry=tempEntry, CurrentTC=CurrentTC, poeStatusTable=poeStatusTable, tempIndex=tempIndex, poeStatusEntry=poeStatusEntry, poeStatus=poeStatus, voltage=voltage, tempTable=tempTable, voltageDescription=voltageDescription, fanSpeed=fanSpeed, PowerTC=PowerTC, netonixSwitchGroups=netonixSwitchGroups, fanEntry=fanEntry, fanTable=fanTable, netonixSwitchCompliances=netonixSwitchCompliances, netonixSwitch=netonixSwitch)
