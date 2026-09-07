#
# PySNMP MIB module OLD-CISCO-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source OLD-CISCO-CPU-MIB
# Source digest sha256:b1beba5cc7d1806b6225af66e2edd05bc90cdedf7c4f68a7f0719e557082f7f2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lcpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 1))
busyPer = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyPer.setStatus('mandatory')
avgBusy1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy1.setStatus('mandatory')
avgBusy5 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy5.setStatus('mandatory')
idleCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 59), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleCount.setStatus('mandatory')
idleWired = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleWired.setStatus('mandatory')
mibBuilder.exportSymbols("OLD-CISCO-CPU-MIB", avgBusy1=avgBusy1, avgBusy5=avgBusy5, busyPer=busyPer, idleCount=idleCount, idleWired=idleWired, lcpu=lcpu)
