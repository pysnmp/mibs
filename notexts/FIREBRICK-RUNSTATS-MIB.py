#
# PySNMP MIB module FIREBRICK-RUNSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source FIREBRICK-RUNSTATS-MIB
# Source digest sha256:062bbe4e1b4a938ee4934e089f775eba00e2f0edf10e8a201fd250365b81dd4d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
firebrickNewStyle, = mibBuilder.importSymbols("FIREBRICK-MIB", "firebrickNewStyle")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fbRunMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693, 100, 3))
fbRunMib.setRevisions(('2020-06-17 00:00',))
if mibBuilder.loadTexts: fbRunMib.setLastUpdated('2020-06-17 00:00')
if mibBuilder.loadTexts: fbRunMib.setOrganization('Andrews & Arnold Limited')
fbRunStatsTable = MibTable((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: fbRunStatsTable.setStatus('current')
fbRunStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "FIREBRICK-RUNSTATS-MIB", "fbRunCore"))
if mibBuilder.loadTexts: fbRunStatsEntry.setStatus('current')
fbRunCore = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 2), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: fbRunCore.setStatus('current')
fbRunBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 24693, 100, 3, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbRunBuffers.setStatus('current')
mibBuilder.exportSymbols("FIREBRICK-RUNSTATS-MIB", PYSNMP_MODULE_ID=fbRunMib, fbRunBuffers=fbRunBuffers, fbRunCore=fbRunCore, fbRunMib=fbRunMib, fbRunStatsEntry=fbRunStatsEntry, fbRunStatsTable=fbRunStatsTable)
