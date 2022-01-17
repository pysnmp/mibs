#
# PySNMP MIB module CTRON-PORTMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PORTMAP-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 19:23:26 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ctPortMap, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPortMap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, TimeTicks, ModuleIdentity, Integer32, iso, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Bits, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "iso", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Bits", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-PORTMAP-MIB", portMapCapability=portMapCapability, portMapIndex=portMapIndex, portMapOperationalMode=portMapOperationalMode, portMapTable=portMapTable, portMap=portMap, portMapRepeater=portMapRepeater, portMapLastSeenSrcAddr=portMapLastSeenSrcAddr, portMapEntry=portMapEntry)
