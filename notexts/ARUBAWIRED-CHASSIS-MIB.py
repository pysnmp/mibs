#
# PySNMP MIB module ARUBAWIRED-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ARUBAWIRED-CHASSIS-MIB
# Source digest sha256:1d5cf75b991fe9c060348b05ba233476a452d4de0811fbbcc5a0a4d053097e7a
# Produced by pysmi-2.3.0
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11))
arubaWiredChassisMIB.setRevisions(('2020-02-13 00:00', '2020-01-07 00:00',))
if mibBuilder.loadTexts: arubaWiredChassisMIB.setLastUpdated('2020-02-13 00:00')
if mibBuilder.loadTexts: arubaWiredChassisMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2))
arubaWiredTempSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3))
arubaWiredFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4))
arubaWiredFan = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5))
mibBuilder.exportSymbols("ARUBAWIRED-CHASSIS-MIB", PYSNMP_MODULE_ID=arubaWiredChassisMIB, arubaWiredChassisMIB=arubaWiredChassisMIB, arubaWiredFan=arubaWiredFan, arubaWiredFanTray=arubaWiredFanTray, arubaWiredPowerSupply=arubaWiredPowerSupply, arubaWiredTempSensor=arubaWiredTempSensor)
