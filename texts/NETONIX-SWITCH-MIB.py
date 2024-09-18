#
# PySNMP MIB module NETONIX-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netonix/NETONIX-SWITCH-MIB
# Produced by pysmi-1.1.12 at Wed Sep 18 06:48:53 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
snmpMIBGroups, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpMIBGroups")
NotificationType, Bits, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, Integer32, iso, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "Integer32", "iso", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netonixSwitch = ModuleIdentity((1, 3, 6, 1, 4, 1, 46242))
netonixSwitch.setRevisions(('1998-03-23 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netonixSwitch.setRevisionsDescriptions(('The MIB Module for Netonix Switches.',))
if mibBuilder.loadTexts: netonixSwitch.setLastUpdated('9803231800Z')
if mibBuilder.loadTexts: netonixSwitch.setOrganization('Netonix')
if mibBuilder.loadTexts: netonixSwitch.setContactInfo('eric@netonix.com')
if mibBuilder.loadTexts: netonixSwitch.setDescription('The MIB Module for Netonix Switches.')
netonixSwitchGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 8)).setObjects(("NETONIX-SWITCH-MIB", "firmwareVersion"), ("NETONIX-SWITCH-MIB", "fanSpeed"), ("NETONIX-SWITCH-MIB", "tempDescription"), ("NETONIX-SWITCH-MIB", "temp"), ("NETONIX-SWITCH-MIB", "voltageDescription"), ("NETONIX-SWITCH-MIB", "voltage"), ("NETONIX-SWITCH-MIB", "poeStatus"), ("NETONIX-SWITCH-MIB", "totalPowerConsumption"), ("NETONIX-SWITCH-MIB", "dcdcInputCurrent"), ("NETONIX-SWITCH-MIB", "dcdcEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    netonixSwitchGroup = netonixSwitchGroup.setStatus('current')
if mibBuilder.loadTexts: netonixSwitchGroup.setDescription('A collection of objects providing basic instrumentation and control of an SNMPv2 entity.')
netonixSwitchConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 46242, 99))
netonixSwitchGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 46242, 99, 1))
netonixSwitchCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 46242, 99, 2))
netonixSwitchCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 46242, 99, 2, 1)).setObjects(("NETONIX-SWITCH-MIB", "netonixSwitchGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    netonixSwitchCompliance = netonixSwitchCompliance.setStatus('current')
if mibBuilder.loadTexts: netonixSwitchCompliance.setDescription('The compliance statement for switches which implement the Netonix Switch MIB.')
class VoltageTC(TextualConvention, Integer32):
    description = 'A voltage with 2 decimal places'
    status = 'current'
    displayHint = 'd-2'

class PowerTC(TextualConvention, Integer32):
    description = 'Power consumption in watts with 1 decimal place'
    status = 'current'
    displayHint = 'd-1'

class CurrentTC(TextualConvention, Integer32):
    description = 'Current in amps with 1 decimal place'
    status = 'current'
    displayHint = 'd-1'

firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 46242, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
if mibBuilder.loadTexts: firmwareVersion.setDescription('The version of the firmware running on the switch')
totalPowerConsumption = MibScalar((1, 3, 6, 1, 4, 1, 46242, 6), PowerTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPowerConsumption.setStatus('current')
if mibBuilder.loadTexts: totalPowerConsumption.setDescription('Total power being consumed by the switch, in Watts')
dcdcInputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 46242, 7), CurrentTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcdcInputCurrent.setStatus('current')
if mibBuilder.loadTexts: dcdcInputCurrent.setDescription('DCDC Input Current in amps')
dcdcEfficiency = MibScalar((1, 3, 6, 1, 4, 1, 46242, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcdcEfficiency.setStatus('current')
if mibBuilder.loadTexts: dcdcEfficiency.setDescription('DCDC power supply efficiency, percentage')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 2), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
if mibBuilder.loadTexts: fanTable.setDescription('Fan watching information.')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 2, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
if mibBuilder.loadTexts: fanEntry.setDescription('An entry containing a disk and its statistics.')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: fanIndex.setStatus('current')
if mibBuilder.loadTexts: fanIndex.setDescription('Integer reference number (row number) for the fan mib.')
fanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSpeed.setStatus('current')
if mibBuilder.loadTexts: fanSpeed.setDescription('Integer reference number (row number) for the fan mib.')
poeStatusTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 5), )
if mibBuilder.loadTexts: poeStatusTable.setStatus('current')
if mibBuilder.loadTexts: poeStatusTable.setDescription('PoE Status per port.')
poeStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 5, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "poeStatusIndex"))
if mibBuilder.loadTexts: poeStatusEntry.setStatus('current')
if mibBuilder.loadTexts: poeStatusEntry.setDescription('An entry containing poe status.')
poeStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: poeStatusIndex.setStatus('current')
if mibBuilder.loadTexts: poeStatusIndex.setDescription('Integer reference number (row number) for the poe status.')
poeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poeStatus.setStatus('current')
if mibBuilder.loadTexts: poeStatus.setDescription('poe status.')
tempTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 3), )
if mibBuilder.loadTexts: tempTable.setStatus('current')
if mibBuilder.loadTexts: tempTable.setDescription('Temperature watching information.')
tempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 3, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "tempIndex"))
if mibBuilder.loadTexts: tempEntry.setStatus('current')
if mibBuilder.loadTexts: tempEntry.setDescription('An entry containing a temperature sensor.')
tempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: tempIndex.setStatus('current')
if mibBuilder.loadTexts: tempIndex.setDescription('Integer reference number (row number) for the temp mib.')
tempDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempDescription.setStatus('current')
if mibBuilder.loadTexts: tempDescription.setDescription('Description of this temperature sensor')
temp = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temp.setStatus('current')
if mibBuilder.loadTexts: temp.setDescription('The current temperature for this sensor')
voltageTable = MibTable((1, 3, 6, 1, 4, 1, 46242, 4), )
if mibBuilder.loadTexts: voltageTable.setStatus('current')
if mibBuilder.loadTexts: voltageTable.setDescription('Voltage watching information.')
voltageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 46242, 4, 1), ).setIndexNames((0, "NETONIX-SWITCH-MIB", "voltageIndex"))
if mibBuilder.loadTexts: voltageEntry.setStatus('current')
if mibBuilder.loadTexts: voltageEntry.setDescription('An entry containing a voltage sensor.')
voltageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: voltageIndex.setStatus('current')
if mibBuilder.loadTexts: voltageIndex.setDescription('Integer reference number (row number) for the voltage mib.')
voltageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageDescription.setStatus('current')
if mibBuilder.loadTexts: voltageDescription.setDescription('Description of this voltage sensor')
voltage = MibTableColumn((1, 3, 6, 1, 4, 1, 46242, 4, 1, 3), VoltageTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage.setStatus('current')
if mibBuilder.loadTexts: voltage.setDescription('The current voltage for this sensor')
mibBuilder.exportSymbols("NETONIX-SWITCH-MIB", tempEntry=tempEntry, PYSNMP_MODULE_ID=netonixSwitch, temp=temp, netonixSwitchCompliance=netonixSwitchCompliance, netonixSwitchCompliances=netonixSwitchCompliances, dcdcEfficiency=dcdcEfficiency, poeStatusIndex=poeStatusIndex, totalPowerConsumption=totalPowerConsumption, poeStatusEntry=poeStatusEntry, dcdcInputCurrent=dcdcInputCurrent, netonixSwitch=netonixSwitch, voltageDescription=voltageDescription, voltageIndex=voltageIndex, netonixSwitchConformance=netonixSwitchConformance, fanTable=fanTable, voltage=voltage, tempIndex=tempIndex, VoltageTC=VoltageTC, CurrentTC=CurrentTC, netonixSwitchGroup=netonixSwitchGroup, tempDescription=tempDescription, poeStatus=poeStatus, voltageTable=voltageTable, poeStatusTable=poeStatusTable, firmwareVersion=firmwareVersion, netonixSwitchGroups=netonixSwitchGroups, fanEntry=fanEntry, voltageEntry=voltageEntry, PowerTC=PowerTC, fanSpeed=fanSpeed, fanIndex=fanIndex, tempTable=tempTable)
