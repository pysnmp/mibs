#
# PySNMP MIB module ALTIGA-GENERAL-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALTIGA-GENERAL-STATS-MIB
# Source digest sha256:be63ccbb80ee1e3b66b539166ced41a9c1fe0544e48e0297b41ea7534994fd77
# Produced by pysmi-2.3.0
#
alGeneralMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alGeneralMibModule")
alGeneralGroup, alStatsGeneral = mibBuilder.importSymbols("ALTIGA-MIB", "alGeneralGroup", "alStatsGeneral")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaGeneralStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2))
altigaGeneralStatsMibModule.setRevisions(('2002-09-11 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setLastUpdated('2002-09-11 13:00')
if mibBuilder.loadTexts: altigaGeneralStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsGeneralGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1))
alGeneralTime = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTime.setStatus('current')
alGeneralGaugeCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeCpuUtil.setStatus('current')
alGeneralGaugeActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeActiveSessions.setStatus('current')
alGeneralGaugeThroughput = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralGaugeThroughput.setStatus('current')
alGeneralTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alGeneralTimeZone.setStatus('current')
altigaGeneralStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1))
altigaGeneralStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1))
altigaGeneralStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1, 1)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "altigaGeneralStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsMibCompliance = altigaGeneralStatsMibCompliance.setStatus('current')
altigaGeneralStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 25, 2)).setObjects(("ALTIGA-GENERAL-STATS-MIB", "alGeneralTime"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeCpuUtil"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeActiveSessions"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeThroughput"), ("ALTIGA-GENERAL-STATS-MIB", "alGeneralTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaGeneralStatsGroup = altigaGeneralStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-GENERAL-STATS-MIB", PYSNMP_MODULE_ID=altigaGeneralStatsMibModule, alGeneralGaugeActiveSessions=alGeneralGaugeActiveSessions, alGeneralGaugeCpuUtil=alGeneralGaugeCpuUtil, alGeneralGaugeThroughput=alGeneralGaugeThroughput, alGeneralTime=alGeneralTime, alGeneralTimeZone=alGeneralTimeZone, alStatsGeneralGlobal=alStatsGeneralGlobal, altigaGeneralStatsGroup=altigaGeneralStatsGroup, altigaGeneralStatsMibCompliance=altigaGeneralStatsMibCompliance, altigaGeneralStatsMibCompliances=altigaGeneralStatsMibCompliances, altigaGeneralStatsMibConformance=altigaGeneralStatsMibConformance, altigaGeneralStatsMibModule=altigaGeneralStatsMibModule)
