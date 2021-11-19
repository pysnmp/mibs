#
# PySNMP MIB module CTRON-PORTMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PORTMAP-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 15:22:26 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ctPortMap, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPortMap")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, IpAddress, Counter64, Gauge32, Unsigned32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, MibIdentifier, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("CTRON-PORTMAP-MIB", portMapEntry=portMapEntry, portMapIndex=portMapIndex, portMap=portMap, portMapTable=portMapTable, portMapLastSeenSrcAddr=portMapLastSeenSrcAddr, portMapRepeater=portMapRepeater, portMapCapability=portMapCapability, portMapOperationalMode=portMapOperationalMode)
