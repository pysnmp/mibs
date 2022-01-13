#
# PySNMP MIB module INT-SERV-GUARANTEED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/INT-SERV-GUARANTEED-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 22:39:59 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
intSrv, = mibBuilder.importSymbols("INT-SERV-MIB", "intSrv")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, NotificationType, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, IpAddress, TimeTicks, Integer32, ObjectIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "NotificationType", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "IpAddress", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "Counter32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 4))
if mibBuilder.loadTexts: intSrvGuaranteed.setLastUpdated('9511030500Z')
if mibBuilder.loadTexts: intSrvGuaranteed.setOrganization('IETF Integrated Services Working Group')
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 4, 1, 1), )
if mibBuilder.loadTexts: intSrvGuaranteedIfTable.setStatus('current')
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvGuaranteedIfEntry.setStatus('current')
intSrvGuaranteedIfC = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfC.setStatus('current')
intSrvGuaranteedIfD = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfD.setStatus('current')
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfSlack.setStatus('current')
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfStatus.setStatus('current')
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3, 2))
intSrvGuaranteedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 3, 2, 1)).setObjects(("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedCompliance = intSrvGuaranteedCompliance.setStatus('current')
intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 3, 1, 2)).setObjects(("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfC"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfD"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedIfAttribGroup = intSrvGuaranteedIfAttribGroup.setStatus('current')
mibBuilder.exportSymbols("INT-SERV-GUARANTEED-MIB", intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedIfC=intSrvGuaranteedIfC, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedIfD=intSrvGuaranteedIfD, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedGroups=intSrvGuaranteedGroups, PYSNMP_MODULE_ID=intSrvGuaranteed)
