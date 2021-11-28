#
# PySNMP MIB module PACKETLOGIC-HW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 21:17:54 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, iso, MibIdentifier, Gauge32, NotificationType, Bits, Counter32, ModuleIdentity, TimeTicks, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "iso", "MibIdentifier", "Gauge32", "NotificationType", "Bits", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
hw = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30))
hw.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: hw.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: hw.setOrganization('Procera Networks, Inc.')
mibBuilder.exportSymbols("PACKETLOGIC-HW-MIB", PYSNMP_MODULE_ID=hw, hw=hw)
