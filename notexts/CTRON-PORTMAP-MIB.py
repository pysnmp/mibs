#
# PySNMP MIB module CTRON-PORTMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PORTMAP-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:18:07 2024
# On host fv-az530-683 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ctPortMap, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPortMap")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, Gauge32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "Gauge32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
portMap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1))
portMapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1), )
if mibBuilder.loadTexts: portMapTable.setStatus('mandatory')
portMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1), ).setIndexNames((0, "CTRON-PORTMAP-MIB", "portMapIndex"))
if mibBuilder.loadTexts: portMapEntry.setStatus('mandatory')
portMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapIndex.setStatus('mandatory')
portMapRepeater = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapRepeater.setStatus('mandatory')
portMapCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapCapability.setStatus('mandatory')
portMapOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMapOperationalMode.setStatus('mandatory')
portMapLastSeenSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMapLastSeenSrcAddr.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-PORTMAP-MIB", portMapTable=portMapTable, portMapCapability=portMapCapability, portMapOperationalMode=portMapOperationalMode, portMapLastSeenSrcAddr=portMapLastSeenSrcAddr, portMap=portMap, portMapRepeater=portMapRepeater, portMapEntry=portMapEntry, portMapIndex=portMapIndex)
