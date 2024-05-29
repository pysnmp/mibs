#
# PySNMP MIB module CTRON-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DEVICE-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:21:52 2024
# On host fv-az1984-402 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32, iso, Counter64, Counter32, ObjectIdentity, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32", "iso", "Counter64", "Counter32", "ObjectIdentity", "IpAddress", "TimeTicks")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
commonDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1))
comDeviceIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: comDeviceIPAddress.setDescription('The Network address, in this case the IP address,\n                    of the device.  This object is required for use by\n                    the Local Management Interface.')
comDeviceTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(6, 6), ValueSizeConstraint(8, 8), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceTime.setStatus('mandatory')
if mibBuilder.loadTexts: comDeviceTime.setDescription('The current time of day, in 24 hour format, as\n                    measured by the device.  The representation shall\n                    use the standard HHMMSS format.')
comDeviceDate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceDate.setStatus('mandatory')
if mibBuilder.loadTexts: comDeviceDate.setDescription('The current date, as measured by the device.  The\n                    representation shall use the standard MMDDYYYY\n                    format.')
mibBuilder.exportSymbols("CTRON-DEVICE-MIB", comDeviceDate=comDeviceDate, comDeviceIPAddress=comDeviceIPAddress, commonDev=commonDev, comDeviceTime=comDeviceTime)
