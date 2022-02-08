#
# PySNMP MIB module ACD-TID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-TID-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:02:59 2022
# On host fv-az126-754 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, Counter32, MibIdentifier, NotificationType, Unsigned32, ModuleIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "ModuleIdentity", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acdTid = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 14))
acdTid.setRevisions(('2011-11-11 01:00',))
if mibBuilder.loadTexts: acdTid.setLastUpdated('201111110100Z')
if mibBuilder.loadTexts: acdTid.setOrganization('Accedian Networks, Inc.')
acdTidNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 0))
acdTidMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1))
acdTidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2))
acdTidGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1))
acdTidInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2))
class AcdTidType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("configuration", 1), ("status", 2))

acdTidCfgLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidCfgLastChangeTid.setStatus('current')
acdTidStatusLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidStatusLastChangeTid.setStatus('current')
acdTidInfoTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1), )
if mibBuilder.loadTexts: acdTidInfoTable.setStatus('current')
acdTidInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1), ).setIndexNames((0, "ACD-TID-MIB", "acdTidInfoIndex"))
if mibBuilder.loadTexts: acdTidInfoEntry.setStatus('current')
acdTidInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdTidInfoIndex.setStatus('current')
acdTidInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoOID.setStatus('current')
acdTidInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 3), AcdTidType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoType.setStatus('current')
acdTidInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoDescr.setStatus('current')
acdTidInfoLastChangeTid = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoLastChangeTid.setStatus('current')
acdTidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1))
acdTidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2))
acdTidGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 1)).setObjects(("ACD-TID-MIB", "acdTidCfgLastChangeTid"), ("ACD-TID-MIB", "acdTidStatusLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidGeneralGroup = acdTidGeneralGroup.setStatus('current')
acdTidTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 2)).setObjects(("ACD-TID-MIB", "acdTidInfoOID"), ("ACD-TID-MIB", "acdTidInfoType"), ("ACD-TID-MIB", "acdTidInfoDescr"), ("ACD-TID-MIB", "acdTidInfoLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidTableGroup = acdTidTableGroup.setStatus('current')
acdTidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1, 1)).setObjects(("ACD-TID-MIB", "acdTidGeneralGroup"), ("ACD-TID-MIB", "acdTidTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidCompliance = acdTidCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-TID-MIB", acdTid=acdTid, acdTidGroups=acdTidGroups, acdTidConformance=acdTidConformance, PYSNMP_MODULE_ID=acdTid, acdTidCompliances=acdTidCompliances, acdTidInfoIndex=acdTidInfoIndex, acdTidInfo=acdTidInfo, acdTidStatusLastChangeTid=acdTidStatusLastChangeTid, acdTidInfoType=acdTidInfoType, acdTidInfoLastChangeTid=acdTidInfoLastChangeTid, acdTidInfoDescr=acdTidInfoDescr, acdTidMIBObjects=acdTidMIBObjects, acdTidCfgLastChangeTid=acdTidCfgLastChangeTid, acdTidInfoTable=acdTidInfoTable, acdTidInfoOID=acdTidInfoOID, acdTidGeneralGroup=acdTidGeneralGroup, acdTidInfoEntry=acdTidInfoEntry, acdTidNotifications=acdTidNotifications, acdTidCompliance=acdTidCompliance, AcdTidType=AcdTidType, acdTidGeneral=acdTidGeneral, acdTidTableGroup=acdTidTableGroup)
