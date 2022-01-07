#
# PySNMP MIB module INT-SERV-GUARANTEED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/INT-SERV-GUARANTEED-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:53:09 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
intSrv, = mibBuilder.importSymbols("INT-SERV-MIB", "intSrv")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Unsigned32, iso, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, MibIdentifier, ModuleIdentity, Counter64, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "iso", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "TimeTicks")
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
mibBuilder.exportSymbols("INT-SERV-GUARANTEED-MIB", intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedIfC=intSrvGuaranteedIfC, PYSNMP_MODULE_ID=intSrvGuaranteed, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedIfD=intSrvGuaranteedIfD, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup)
