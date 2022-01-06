#
# PySNMP MIB module PT-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-PM-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 20:12:53 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Gauge32, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, ModuleIdentity, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ptPM = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 5))
ptPM.setRevisions(('2018-08-29 12:30', '2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: ptPM.setLastUpdated('201808291230Z')
if mibBuilder.loadTexts: ptPM.setOrganization('Ericsson')
ptPMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2))
ptPMTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1), )
if mibBuilder.loadTexts: ptPMTable.setStatus('current')
ptPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1), ).setIndexNames((0, "PT-PM-MIB", "queueIndex"))
if mibBuilder.loadTexts: ptPMEntry.setStatus('current')
queueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: queueIndex.setStatus('current')
forwardingPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardingPacket.setStatus('current')
forwardingOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardingOctets.setStatus('current')
discardPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discardPackets.setStatus('current')
discardOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discardOctets.setStatus('current')
inputPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputPackets.setStatus('current')
inputOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputOctets.setStatus('current')
ptPMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1))
ptPMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2))
ptPMFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1, 1)).setObjects(("PT-PM-MIB", "ptPMCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptPMFullCompliance = ptPMFullCompliance.setStatus('current')
ptPMCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2, 1)).setObjects(("PT-PM-MIB", "forwardingPacket"), ("PT-PM-MIB", "forwardingOctets"), ("PT-PM-MIB", "discardPackets"), ("PT-PM-MIB", "discardOctets"), ("PT-PM-MIB", "inputPackets"), ("PT-PM-MIB", "inputOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptPMCompleteGroup = ptPMCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-PM-MIB", ptPM=ptPM, queueIndex=queueIndex, forwardingOctets=forwardingOctets, discardOctets=discardOctets, ptPMFullCompliance=ptPMFullCompliance, PYSNMP_MODULE_ID=ptPM, ptPMConformance=ptPMConformance, ptPMCompliances=ptPMCompliances, ptPMGroups=ptPMGroups, forwardingPacket=forwardingPacket, discardPackets=discardPackets, ptPMCompleteGroup=ptPMCompleteGroup, inputOctets=inputOctets, inputPackets=inputPackets, ptPMEntry=ptPMEntry, ptPMTable=ptPMTable)
