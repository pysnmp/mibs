#
# PySNMP MIB module RADLAN-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 16:52:01 2022
# On host fv-az126-328 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, iso, TimeTicks, Counter32, Counter64, ModuleIdentity, IpAddress, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "iso", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Gauge32")
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
mibBuilder.exportSymbols("RADLAN-SNMP-MIB", rlSNMPDomains=rlSNMPDomains, rlSNMPv3=rlSNMPv3, rlSnmpRequestMridTable=rlSnmpRequestMridTable, rlSNMP=rlSNMP, RlSnmpUDPMridAddress=RlSnmpUDPMridAddress, rlSnmpUDPMridDomain=rlSnmpUDPMridDomain, rlSnmpRequestManagedMrid=rlSnmpRequestManagedMrid, rlSnmpRequestMridStatus=rlSnmpRequestMridStatus, rlTargetParamsTestingLevel=rlTargetParamsTestingLevel, rlSnmpRequestMridEntry=rlSnmpRequestMridEntry, PYSNMP_MODULE_ID=rlSNMP, rlSnmpEngineID=rlSnmpEngineID, rlNotifyFilterTestingLevel=rlNotifyFilterTestingLevel)
