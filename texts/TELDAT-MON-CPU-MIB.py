#
# PySNMP MIB module TELDAT-MON-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-CPU-MIB
# Produced by pysmi-1.1.12 at Thu May 30 02:21:51 2024
# On host fv-az775-912 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64, IpAddress, Bits, ModuleIdentity, Counter32, ObjectIdentity, Gauge32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64", "IpAddress", "Bits", "ModuleIdentity", "Counter32", "ObjectIdentity", "Gauge32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
telProdNpMonitSistema, = mibBuilder.importSymbols("TELDAT-SW-STRUCTURE-MIB", "telProdNpMonitSistema")
teldatCPUMonMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2))
teldatCPUMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1))
teldatCPUMonMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 2))
teldatCPUMonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 2, 0))
teldatCPUMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3))
teldatCPUCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3, 1))
teldatCPUGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3, 2))
teldatCPUBusyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1))
teldatCPUBusy5sec = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy5sec.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy5sec.setDescription('The overall CPU busy percentage in the last 5 second period.')
teldatCPUBusy1min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy1min.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy1min.setDescription('The overall CPU busy percentage in the last 1 minute period.')
teldatCPUBusy5min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy5min.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy5min.setDescription('The overall CPU busy percentage in the last 5 minute period.')
mibBuilder.exportSymbols("TELDAT-MON-CPU-MIB", teldatCPUMonMIBConformance=teldatCPUMonMIBConformance, teldatCPUBusy5sec=teldatCPUBusy5sec, teldatCPUBusyGroup=teldatCPUBusyGroup, teldatCPUBusy1min=teldatCPUBusy1min, teldatCPUMonMIBObjects=teldatCPUMonMIBObjects, teldatCPUBusy5min=teldatCPUBusy5min, teldatCPUMonMIBNotifs=teldatCPUMonMIBNotifs, teldatCPUMonMIBNotifPrefix=teldatCPUMonMIBNotifPrefix, teldatCPUMonMIB=teldatCPUMonMIB, teldatCPUGroups=teldatCPUGroups, teldatCPUCompliances=teldatCPUCompliances)
