#
# PySNMP MIB module STORMSHIELD-IPSEC-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:28:29 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, NotificationType, Integer32, TimeTicks, iso, IpAddress, Unsigned32, Counter32, MibIdentifier, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "NotificationType", "Integer32", "TimeTicks", "iso", "IpAddress", "Unsigned32", "Counter32", "MibIdentifier", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
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
mibBuilder.exportSymbols("STORMSHIELD-IPSEC-STATS-MIB", snsIPSECStatsSPDIn=snsIPSECStatsSPDIn, PYSNMP_MODULE_ID=snsIPSECStats, snsIPSECStatsSADDead=snsIPSECStatsSADDead, snsIPSECStatsSADMature=snsIPSECStatsSADMature, snsIPSECStatsSPD=snsIPSECStatsSPD, snsIPSECStatsSAD=snsIPSECStatsSAD, snsIPSECStatsSADDying=snsIPSECStatsSADDying, snsIPSECStatsSADLarval=snsIPSECStatsSADLarval, snsIPSECStatsSPDOut=snsIPSECStatsSPDOut, snsIPSECStats=snsIPSECStats)
