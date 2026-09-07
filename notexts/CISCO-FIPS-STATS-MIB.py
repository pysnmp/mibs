#
# PySNMP MIB module CISCO-FIPS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FIPS-STATS-MIB
# Source digest sha256:f510e5c03bf3a49d48ae22562709319da62dd6926c3373fc79b97df84946a49a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFipsStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 999999))
ciscoFipsStatsMIB.setRevisions(('2003-03-10 00:00',))
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setLastUpdated('2003-03-10 00:00')
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setOrganization('Cisco Systems, Inc.')
ciscoFipsStatsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 0))
ciscoFipsStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1))
ciscoFipsStatsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2))
cfipsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1))
cfipsStatsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1))
cfipsPostStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("running", 1), ("passed", 2), ("failed", 3), ("notAvailable", 4))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfipsPostStatus.setStatus('current')
ciscoFipsStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1))
ciscoFipsStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2))
ciscoFipsStatsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "ciscoFipsStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBCompliance = ciscoFipsStatsMIBCompliance.setStatus('current')
ciscoFipsStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "cfipsPostStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBGroup = ciscoFipsStatsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FIPS-STATS-MIB", PYSNMP_MODULE_ID=ciscoFipsStatsMIB, cfipsPostStatus=cfipsPostStatus, cfipsStats=cfipsStats, cfipsStatsGlobal=cfipsStatsGlobal, ciscoFipsStatsMIB=ciscoFipsStatsMIB, ciscoFipsStatsMIBCompliance=ciscoFipsStatsMIBCompliance, ciscoFipsStatsMIBCompliances=ciscoFipsStatsMIBCompliances, ciscoFipsStatsMIBConform=ciscoFipsStatsMIBConform, ciscoFipsStatsMIBGroup=ciscoFipsStatsMIBGroup, ciscoFipsStatsMIBGroups=ciscoFipsStatsMIBGroups, ciscoFipsStatsMIBNotifs=ciscoFipsStatsMIBNotifs, ciscoFipsStatsMIBObjects=ciscoFipsStatsMIBObjects)
