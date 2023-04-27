#
# PySNMP MIB module CTRON-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DEVICE-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:16:10 2023
# On host fv-az247-870 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, ModuleIdentity, Bits, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, MibIdentifier, Counter32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32", "iso", "Unsigned32")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
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
mibBuilder.exportSymbols("CTRON-DEVICE-MIB", comDeviceTime=comDeviceTime, commonDev=commonDev, comDeviceIPAddress=comDeviceIPAddress, comDeviceDate=comDeviceDate)
