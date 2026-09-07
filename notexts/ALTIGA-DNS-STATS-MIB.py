#
# PySNMP MIB module ALTIGA-DNS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALTIGA-DNS-STATS-MIB
# Source digest sha256:44f94eae0ec6bae9962b43b2f6ca61c09a38bf5513e30e27f0e37f3aee3c48a0
# Produced by pysmi-2.3.0
#
alDnsMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alDnsMibModule")
alDnsGroup, alStatsDns = mibBuilder.importSymbols("ALTIGA-MIB", "alDnsGroup", "alStatsDns")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaDnsStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2))
altigaDnsStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setLastUpdated('2002-09-05 13:00')
if mibBuilder.loadTexts: altigaDnsStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsDnsResolverGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1))
alDnsStatsAttemptedQueries = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsAttemptedQueries.setStatus('current')
alDnsStatsSuccessfulResponses = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsSuccessfulResponses.setStatus('current')
alDnsStatsTimeoutFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsTimeoutFailures.setStatus('current')
alDnsStatsUnreachableServerFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsUnreachableServerFailures.setStatus('current')
alDnsStatsMiscFailures = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDnsStatsMiscFailures.setStatus('current')
altigaDnsStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1))
altigaDnsStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1))
altigaDnsStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1, 1)).setObjects(("ALTIGA-DNS-STATS-MIB", "altigaDnsStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsMibCompliance = altigaDnsStatsMibCompliance.setStatus('current')
altigaDnsStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 18, 2)).setObjects(("ALTIGA-DNS-STATS-MIB", "alDnsStatsAttemptedQueries"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsSuccessfulResponses"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsTimeoutFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsUnreachableServerFailures"), ("ALTIGA-DNS-STATS-MIB", "alDnsStatsMiscFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaDnsStatsGroup = altigaDnsStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-DNS-STATS-MIB", PYSNMP_MODULE_ID=altigaDnsStatsMibModule, alDnsStatsAttemptedQueries=alDnsStatsAttemptedQueries, alDnsStatsMiscFailures=alDnsStatsMiscFailures, alDnsStatsSuccessfulResponses=alDnsStatsSuccessfulResponses, alDnsStatsTimeoutFailures=alDnsStatsTimeoutFailures, alDnsStatsUnreachableServerFailures=alDnsStatsUnreachableServerFailures, alStatsDnsResolverGlobal=alStatsDnsResolverGlobal, altigaDnsStatsGroup=altigaDnsStatsGroup, altigaDnsStatsMibCompliance=altigaDnsStatsMibCompliance, altigaDnsStatsMibCompliances=altigaDnsStatsMibCompliances, altigaDnsStatsMibConformance=altigaDnsStatsMibConformance, altigaDnsStatsMibModule=altigaDnsStatsMibModule)
