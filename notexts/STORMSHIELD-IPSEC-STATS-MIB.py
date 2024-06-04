#
# PySNMP MIB module STORMSHIELD-IPSEC-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 10:14:50 2024
# On host fv-az801-864 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Integer32, Counter64, Gauge32, IpAddress, MibIdentifier, Bits, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("STORMSHIELD-IPSEC-STATS-MIB", snsIPSECStatsSADDead=snsIPSECStatsSADDead, PYSNMP_MODULE_ID=snsIPSECStats, snsIPSECStatsSPDOut=snsIPSECStatsSPDOut, snsIPSECStatsSADDying=snsIPSECStatsSADDying, snsIPSECStatsSPDIn=snsIPSECStatsSPDIn, snsIPSECStats=snsIPSECStats, snsIPSECStatsSAD=snsIPSECStatsSAD, snsIPSECStatsSADMature=snsIPSECStatsSADMature, snsIPSECStatsSPD=snsIPSECStatsSPD, snsIPSECStatsSADLarval=snsIPSECStatsSADLarval)
