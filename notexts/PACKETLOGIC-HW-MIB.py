#
# PySNMP MIB module PACKETLOGIC-HW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:06:22 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, Bits, ObjectIdentity, Unsigned32, Integer32, IpAddress, ModuleIdentity, TimeTicks, iso, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "IpAddress", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
hw = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30))
hw.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: hw.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: hw.setOrganization('Procera Networks, Inc.')
mibBuilder.exportSymbols("PACKETLOGIC-HW-MIB", PYSNMP_MODULE_ID=hw, hw=hw)
