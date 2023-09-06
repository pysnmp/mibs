#
# PySNMP MIB module TELDAT-MON-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-CPU-MIB
# Produced by pysmi-1.1.8 at Wed Sep  6 13:59:08 2023
# On host fv-az254-698 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.12 (main, Jun  7 2023, 13:43:11) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Bits, Integer32, Unsigned32, TimeTicks, Gauge32, IpAddress, Counter64, MibIdentifier, ModuleIdentity, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Bits", "Integer32", "Unsigned32", "TimeTicks", "Gauge32", "IpAddress", "Counter64", "MibIdentifier", "ModuleIdentity", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
teldatCPUBusy1min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy1min.setStatus('mandatory')
teldatCPUBusy5min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy5min.setStatus('mandatory')
mibBuilder.exportSymbols("TELDAT-MON-CPU-MIB", teldatCPUGroups=teldatCPUGroups, teldatCPUBusyGroup=teldatCPUBusyGroup, teldatCPUMonMIB=teldatCPUMonMIB, teldatCPUMonMIBObjects=teldatCPUMonMIBObjects, teldatCPUMonMIBConformance=teldatCPUMonMIBConformance, teldatCPUBusy5min=teldatCPUBusy5min, teldatCPUBusy5sec=teldatCPUBusy5sec, teldatCPUBusy1min=teldatCPUBusy1min, teldatCPUMonMIBNotifs=teldatCPUMonMIBNotifs, teldatCPUMonMIBNotifPrefix=teldatCPUMonMIBNotifPrefix, teldatCPUCompliances=teldatCPUCompliances)
