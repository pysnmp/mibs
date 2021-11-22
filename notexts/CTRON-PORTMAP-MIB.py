#
# PySNMP MIB module CTRON-PORTMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PORTMAP-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:38:13 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ctPortMap, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPortMap")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, ModuleIdentity, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Gauge32, Counter64, MibIdentifier, TimeTicks, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "iso", "Unsigned32")
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
mibBuilder.exportSymbols("CTRON-PORTMAP-MIB", portMapRepeater=portMapRepeater, portMapTable=portMapTable, portMapOperationalMode=portMapOperationalMode, portMap=portMap, portMapIndex=portMapIndex, portMapLastSeenSrcAddr=portMapLastSeenSrcAddr, portMapEntry=portMapEntry, portMapCapability=portMapCapability)
