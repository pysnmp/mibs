#
# PySNMP MIB module NBS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-STATS-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:11:39 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Counter32, NotificationType, Gauge32, MibIdentifier, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsStatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 233))
if mibBuilder.loadTexts: nbsStatsMib.setLastUpdated('201303130000Z')
if mibBuilder.loadTexts: nbsStatsMib.setOrganization('NBS')
nbsStatInfoGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 233, 1))
if mibBuilder.loadTexts: nbsStatInfoGrp.setStatus('current')
nbsStatInfoTable = MibTable((1, 3, 6, 1, 4, 1, 629, 233, 1, 10), )
if mibBuilder.loadTexts: nbsStatInfoTable.setStatus('current')
nbsStatInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1), ).setIndexNames((0, "NBS-STATS-MIB", "nbsStatInfoIndex"))
if mibBuilder.loadTexts: nbsStatInfoEntry.setStatus('current')
nbsStatInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsStatInfoIndex.setStatus('current')
nbsStatInfoCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoCounters.setStatus('current')
nbsStatInfoPmData = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoPmData.setStatus('current')
mibBuilder.exportSymbols("NBS-STATS-MIB", nbsStatInfoTable=nbsStatInfoTable, nbsStatInfoIndex=nbsStatInfoIndex, nbsStatInfoGrp=nbsStatInfoGrp, PYSNMP_MODULE_ID=nbsStatsMib, nbsStatInfoCounters=nbsStatInfoCounters, nbsStatsMib=nbsStatsMib, nbsStatInfoPmData=nbsStatInfoPmData, nbsStatInfoEntry=nbsStatInfoEntry)
