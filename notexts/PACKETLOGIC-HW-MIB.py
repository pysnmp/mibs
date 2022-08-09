#
# PySNMP MIB module PACKETLOGIC-HW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:50:34 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Gauge32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ObjectIdentity, IpAddress, MibIdentifier, Unsigned32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Gauge32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ObjectIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "ModuleIdentity", "NotificationType")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
hw = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30))
hw.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: hw.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: hw.setOrganization('Procera Networks, Inc.')
mibBuilder.exportSymbols("PACKETLOGIC-HW-MIB", PYSNMP_MODULE_ID=hw, hw=hw)
