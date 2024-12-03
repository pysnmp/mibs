#
# PySNMP MIB module CTRON-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DEVICE-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:42:10 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, iso, TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ModuleIdentity, Gauge32, IpAddress, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ModuleIdentity", "Gauge32", "IpAddress", "Unsigned32", "Counter32")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-DEVICE-MIB", comDeviceDate=comDeviceDate, commonDev=commonDev, comDeviceIPAddress=comDeviceIPAddress, comDeviceTime=comDeviceTime)
