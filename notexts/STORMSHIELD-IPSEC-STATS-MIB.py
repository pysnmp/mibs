#
# PySNMP MIB module STORMSHIELD-IPSEC-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.1.12 at Tue May 28 14:04:09 2024
# On host fv-az529-55 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter64, Counter32, iso, IpAddress, Integer32, TimeTicks, ObjectIdentity, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter64", "Counter32", "iso", "IpAddress", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsIPSECStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 13))
snsIPSECStats.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsIPSECStats.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsIPSECStats.setOrganization('Stormshield')
snsIPSECStatsSPD = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1))
snsIPSECStatsSAD = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2))
snsIPSECStatsSPDIn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSPDIn.setStatus('current')
snsIPSECStatsSPDOut = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSPDOut.setStatus('current')
snsIPSECStatsSADLarval = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADLarval.setStatus('current')
snsIPSECStatsSADMature = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADMature.setStatus('current')
snsIPSECStatsSADDying = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADDying.setStatus('current')
snsIPSECStatsSADDead = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADDead.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-IPSEC-STATS-MIB", snsIPSECStats=snsIPSECStats, snsIPSECStatsSADDying=snsIPSECStatsSADDying, snsIPSECStatsSADMature=snsIPSECStatsSADMature, snsIPSECStatsSADLarval=snsIPSECStatsSADLarval, PYSNMP_MODULE_ID=snsIPSECStats, snsIPSECStatsSAD=snsIPSECStatsSAD, snsIPSECStatsSPDOut=snsIPSECStatsSPDOut, snsIPSECStatsSPDIn=snsIPSECStatsSPDIn, snsIPSECStatsSADDead=snsIPSECStatsSADDead, snsIPSECStatsSPD=snsIPSECStatsSPD)
