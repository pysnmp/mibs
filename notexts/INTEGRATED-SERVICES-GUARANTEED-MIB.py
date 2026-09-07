#
# PySNMP MIB module INTEGRATED-SERVICES-GUARANTEED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source INTEGRATED-SERVICES-GUARANTEED-MIB
# Source digest sha256:8f1aa5c4098b09a190f970ef8231a389d11f7f10845b0031823fdc3111bf72ea
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
intSrv, = mibBuilder.importSymbols("INTEGRATED-SERVICES-MIB", "intSrv")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 5))
if mibBuilder.loadTexts: intSrvGuaranteed.setLastUpdated('1995-11-03 05:00')
if mibBuilder.loadTexts: intSrvGuaranteed.setOrganization('IETF Integrated Services Working Group')
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 1))
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 5, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: intSrvGuaranteedIfTable.setStatus('current')
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvGuaranteedIfEntry.setStatus('current')
intSrvGuaranteedIfBacklog = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfBacklog.setStatus('current')
intSrvGuaranteedIfDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfDelay.setStatus('current')
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfSlack.setStatus('current')
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfStatus.setStatus('current')
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 2))
intSrvGuaranteedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 5, 3, 2, 1)).setObjects(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedCompliance = intSrvGuaranteedCompliance.setStatus('current')
intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 5, 3, 1, 2)).setObjects(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfBacklog"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfDelay"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedIfAttribGroup = intSrvGuaranteedIfAttribGroup.setStatus('current')
mibBuilder.exportSymbols("INTEGRATED-SERVICES-GUARANTEED-MIB", PYSNMP_MODULE_ID=intSrvGuaranteed, intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup, intSrvGuaranteedIfBacklog=intSrvGuaranteedIfBacklog, intSrvGuaranteedIfDelay=intSrvGuaranteedIfDelay, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, intSrvGuaranteedObjects=intSrvGuaranteedObjects)
