#
# PySNMP MIB module STORMSHIELD-IPSEC-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 14:11:53 2024
# On host fv-az1456-954 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, ModuleIdentity, iso, MibIdentifier, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Counter64, Gauge32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "ModuleIdentity", "iso", "MibIdentifier", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "Integer32", "NotificationType")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("STORMSHIELD-IPSEC-STATS-MIB", snsIPSECStatsSADLarval=snsIPSECStatsSADLarval, PYSNMP_MODULE_ID=snsIPSECStats, snsIPSECStatsSAD=snsIPSECStatsSAD, snsIPSECStatsSADDead=snsIPSECStatsSADDead, snsIPSECStatsSPDIn=snsIPSECStatsSPDIn, snsIPSECStats=snsIPSECStats, snsIPSECStatsSADMature=snsIPSECStatsSADMature, snsIPSECStatsSPDOut=snsIPSECStatsSPDOut, snsIPSECStatsSADDying=snsIPSECStatsSADDying, snsIPSECStatsSPD=snsIPSECStatsSPD)
