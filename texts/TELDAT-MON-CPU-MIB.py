#
# PySNMP MIB module TELDAT-MON-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-CPU-MIB
# Produced by pysmi-1.1.8 at Thu Feb  9 13:33:37 2023
# On host fv-az255-593 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, Integer32, NotificationType, Counter32, Unsigned32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Integer32", "NotificationType", "Counter32", "Unsigned32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "ModuleIdentity")
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
if mibBuilder.loadTexts: teldatCPUBusy5sec.setDescription('The overall CPU busy percentage in the last 5 second period.')
teldatCPUBusy1min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy1min.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy1min.setDescription('The overall CPU busy percentage in the last 1 minute period.')
teldatCPUBusy5min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy5min.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy5min.setDescription('The overall CPU busy percentage in the last 5 minute period.')
mibBuilder.exportSymbols("TELDAT-MON-CPU-MIB", teldatCPUGroups=teldatCPUGroups, teldatCPUMonMIBNotifs=teldatCPUMonMIBNotifs, teldatCPUBusy1min=teldatCPUBusy1min, teldatCPUMonMIB=teldatCPUMonMIB, teldatCPUMonMIBConformance=teldatCPUMonMIBConformance, teldatCPUMonMIBNotifPrefix=teldatCPUMonMIBNotifPrefix, teldatCPUBusy5min=teldatCPUBusy5min, teldatCPUMonMIBObjects=teldatCPUMonMIBObjects, teldatCPUBusy5sec=teldatCPUBusy5sec, teldatCPUCompliances=teldatCPUCompliances, teldatCPUBusyGroup=teldatCPUBusyGroup)
