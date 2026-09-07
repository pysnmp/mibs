#
# PySNMP MIB module CISCO-NETINT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NETINT-MIB
# Source digest sha256:e70977c7ffe141308378b4f25d39676e5c49b4a3b653dac34cbec40268d4f57b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetintMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 490))
ciscoNetintMIB.setRevisions(('2005-09-26 00:00',))
if mibBuilder.loadTexts: ciscoNetintMIB.setLastUpdated('2005-09-26 00:00')
if mibBuilder.loadTexts: ciscoNetintMIB.setOrganization('Cisco Systems, Inc.')
ciscoNetintMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 0))
ciscoNetintMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1))
ciscoNetintMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2))
cniThrottle = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1))
cniThrottleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cniThrottleTable.setStatus('current')
cniThrottleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cniThrottleEntry.setStatus('current')
cniThrottleCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cniThrottleCount.setStatus('current')
ciscoNetintMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1))
ciscoNetintMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2))
ciscoNetintMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1, 1)).setObjects(("CISCO-NETINT-MIB", "ciscoThrottleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintMIBCompliance = ciscoNetintMIBCompliance.setStatus('current')
ciscoThrottleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2, 1)).setObjects(("CISCO-NETINT-MIB", "cniThrottleCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoThrottleGroup = ciscoThrottleGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETINT-MIB", PYSNMP_MODULE_ID=ciscoNetintMIB, ciscoNetintMIB=ciscoNetintMIB, ciscoNetintMIBCompliance=ciscoNetintMIBCompliance, ciscoNetintMIBCompliances=ciscoNetintMIBCompliances, ciscoNetintMIBConformance=ciscoNetintMIBConformance, ciscoNetintMIBGroups=ciscoNetintMIBGroups, ciscoNetintMIBNotifs=ciscoNetintMIBNotifs, ciscoNetintMIBObjects=ciscoNetintMIBObjects, ciscoThrottleGroup=ciscoThrottleGroup, cniThrottle=cniThrottle, cniThrottleCount=cniThrottleCount, cniThrottleEntry=cniThrottleEntry, cniThrottleTable=cniThrottleTable)
