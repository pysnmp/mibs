#
# PySNMP MIB module CTRON-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DEVICE-MIB
# Produced by pysmi-1.1.12 at Wed Sep 18 06:45:17 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter32, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter32", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Counter64")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
commonDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1))
comDeviceIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceIPAddress.setStatus('mandatory')
comDeviceTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(6, 6), ValueSizeConstraint(8, 8), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceTime.setStatus('mandatory')
comDeviceDate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceDate.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DEVICE-MIB", comDeviceDate=comDeviceDate, commonDev=commonDev, comDeviceTime=comDeviceTime, comDeviceIPAddress=comDeviceIPAddress)
