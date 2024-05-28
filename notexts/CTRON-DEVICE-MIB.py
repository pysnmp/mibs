#
# PySNMP MIB module CTRON-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DEVICE-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:35:53 2024
# On host fv-az973-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, IpAddress, NotificationType, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter32")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
commonDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1))
comDeviceIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceIPAddress.setStatus('mandatory')
comDeviceTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(6, 6), ValueSizeConstraint(8, 8), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceTime.setStatus('mandatory')
comDeviceDate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceDate.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DEVICE-MIB", comDeviceTime=comDeviceTime, commonDev=commonDev, comDeviceDate=comDeviceDate, comDeviceIPAddress=comDeviceIPAddress)
