#
# PySNMP MIB module ACOS-GSLB-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ACOS-GSLB-STATISTICS-MIB
# Source digest sha256:0943d074fa4a4be5a76aae952f05aa4ccd2583214c31fa164bcc9739a941a78c
# Produced by pysmi-2.3.0
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
gslbStatisticsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422))
if mibBuilder.loadTexts: gslbStatisticsModule.setLastUpdated('2007-05-07 13:27')
if mibBuilder.loadTexts: gslbStatisticsModule.setOrganization('A10 Networks, Inc.')
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1))
statisticsOperTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: statisticsOperTable.setStatus('current')
statisticsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ACOS-GSLB-STATISTICS-MIB", "statisticsOperSlotId"))
if mibBuilder.loadTexts: statisticsOperEntry.setStatus('current')
statisticsOperSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statisticsOperSlotId.setStatus('current')
statisticsOperCurrSslCtx = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 422, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statisticsOperCurrSslCtx.setStatus('current')
mibBuilder.exportSymbols("ACOS-GSLB-STATISTICS-MIB", PYSNMP_MODULE_ID=gslbStatisticsModule, gslbStatisticsModule=gslbStatisticsModule, statistics=statistics, statisticsOperCurrSslCtx=statisticsOperCurrSslCtx, statisticsOperEntry=statisticsOperEntry, statisticsOperSlotId=statisticsOperSlotId, statisticsOperTable=statisticsOperTable)
