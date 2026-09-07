#
# PySNMP MIB module TGT-ADDRESS-MASK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source TGT-ADDRESS-MASK-MIB
# Source digest sha256:756f93b19ef5ac18ff1188fe8e74c5a475cf9be64156ddbc3266302b7c2a7116
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TAddress", "TextualConvention")
snmpResearch = MibIdentifier((1, 3, 6, 1, 4, 1, 99))
snmpResearchMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 99, 12))
tgtAddressMaskMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 99, 12, 36))
if mibBuilder.loadTexts: tgtAddressMaskMIB.setLastUpdated('1998-01-16 00:00')
if mibBuilder.loadTexts: tgtAddressMaskMIB.setOrganization('SNMP Research, Inc.')
tgtAddressMaskObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 99, 12, 36, 1))
tgtAddressMaskConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 99, 12, 36, 3))
tgtAddressMaskTable = MibTable((1, 3, 6, 1, 4, 1, 99, 12, 36, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: tgtAddressMaskTable.setStatus('current')
tgtAddressMaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 99, 12, 36, 1, 1, 1), ).setMaxAccess("notaccessible")
snmpTargetAddrEntry.registerAugmentions(("TGT-ADDRESS-MASK-MIB", "tgtAddressMaskEntry"))
tgtAddressMaskEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: tgtAddressMaskEntry.setStatus('current')
tgtAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 99, 12, 36, 1, 1, 1, 1), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tgtAddressMask.setStatus('current')
mibBuilder.exportSymbols("TGT-ADDRESS-MASK-MIB", PYSNMP_MODULE_ID=tgtAddressMaskMIB, snmpResearch=snmpResearch, snmpResearchMIBs=snmpResearchMIBs, tgtAddressMask=tgtAddressMask, tgtAddressMaskConformance=tgtAddressMaskConformance, tgtAddressMaskEntry=tgtAddressMaskEntry, tgtAddressMaskMIB=tgtAddressMaskMIB, tgtAddressMaskObjects=tgtAddressMaskObjects, tgtAddressMaskTable=tgtAddressMaskTable)
