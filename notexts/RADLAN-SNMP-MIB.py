#
# PySNMP MIB module RADLAN-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMP-MIB
# Produced by pysmi-1.1.8 at Thu Dec 15 08:33:17 2022
# On host fv-az193-683 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, Bits, Unsigned32, NotificationType, iso, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "NotificationType", "iso", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlSNMP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 98))
rlSNMP.setRevisions(('1904-10-20 00:00',))
if mibBuilder.loadTexts: rlSNMP.setLastUpdated('0410200000Z')
if mibBuilder.loadTexts: rlSNMP.setOrganization('Radlan Computer Communications Ltd.')
rlSNMPv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 98, 1))
rlTargetParamsTestingLevel = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTargetParamsTestingLevel.setStatus('current')
rlNotifyFilterTestingLevel = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlNotifyFilterTestingLevel.setStatus('current')
rlSnmpEngineID = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 32)).clone(hexValue="0000000001")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnmpEngineID.setStatus('current')
rlSNMPDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 98, 2))
rlSnmpUDPMridDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 89, 98, 2, 1))
if mibBuilder.loadTexts: rlSnmpUDPMridDomain.setStatus('current')
class RlSnmpUDPMridAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

rlSnmpRequestMridTable = MibTable((1, 3, 6, 1, 4, 1, 89, 98, 3), )
if mibBuilder.loadTexts: rlSnmpRequestMridTable.setStatus('current')
rlSnmpRequestMridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 98, 3, 1), ).setIndexNames((0, "RADLAN-SNMP-MIB", "rlSnmpRequestManagedMrid"))
if mibBuilder.loadTexts: rlSnmpRequestMridEntry.setStatus('current')
rlSnmpRequestManagedMrid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpRequestManagedMrid.setStatus('current')
rlSnmpRequestMridStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnmpRequestMridStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SNMP-MIB", RlSnmpUDPMridAddress=RlSnmpUDPMridAddress, rlSnmpRequestMridStatus=rlSnmpRequestMridStatus, rlSNMPv3=rlSNMPv3, rlSnmpRequestMridEntry=rlSnmpRequestMridEntry, PYSNMP_MODULE_ID=rlSNMP, rlNotifyFilterTestingLevel=rlNotifyFilterTestingLevel, rlSnmpRequestManagedMrid=rlSnmpRequestManagedMrid, rlSnmpEngineID=rlSnmpEngineID, rlSNMP=rlSNMP, rlSnmpUDPMridDomain=rlSnmpUDPMridDomain, rlSnmpRequestMridTable=rlSnmpRequestMridTable, rlTargetParamsTestingLevel=rlTargetParamsTestingLevel, rlSNMPDomains=rlSNMPDomains)
