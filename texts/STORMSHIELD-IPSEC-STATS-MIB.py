#
# PySNMP MIB module STORMSHIELD-IPSEC-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 28 03:03:19 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, iso, Bits, Unsigned32, ModuleIdentity, Gauge32, NotificationType, Counter64, TimeTicks, ObjectIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "iso", "Bits", "Unsigned32", "ModuleIdentity", "Gauge32", "NotificationType", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsIPSECStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 13))
snsIPSECStats.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsIPSECStats.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsIPSECStats.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsIPSECStats.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsIPSECStats.setContactInfo('Customer Support\n\n        22 rue du Gouverneur General Eboue\n        92130 Issy-les-Moulineaux\n        FRANCE\n\n        Tel: +33 (0)9 69 32 96 29\n        E-mail: support@stormshield.eu\n        http://www.stormshield.eu')
if mibBuilder.loadTexts: snsIPSECStats.setDescription('stormshield IPSEC Statistics')
snsIPSECStatsSPD = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1))
snsIPSECStatsSAD = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2))
snsIPSECStatsSPDIn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSPDIn.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSPDIn.setDescription('Number of incomming security policies')
snsIPSECStatsSPDOut = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSPDOut.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSPDOut.setDescription('Number of outgoing security policies')
snsIPSECStatsSADLarval = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADLarval.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADLarval.setDescription('Number of security associations in establishment')
snsIPSECStatsSADMature = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADMature.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADMature.setDescription('Number established security associations')
snsIPSECStatsSADDying = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADDying.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADDying.setDescription('Number of security associations in end of life')
snsIPSECStatsSADDead = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADDead.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADDead.setDescription('Number of dead security associations')
mibBuilder.exportSymbols("STORMSHIELD-IPSEC-STATS-MIB", snsIPSECStatsSADLarval=snsIPSECStatsSADLarval, snsIPSECStatsSADMature=snsIPSECStatsSADMature, snsIPSECStats=snsIPSECStats, snsIPSECStatsSPD=snsIPSECStatsSPD, snsIPSECStatsSADDead=snsIPSECStatsSADDead, snsIPSECStatsSAD=snsIPSECStatsSAD, snsIPSECStatsSPDIn=snsIPSECStatsSPDIn, snsIPSECStatsSPDOut=snsIPSECStatsSPDOut, snsIPSECStatsSADDying=snsIPSECStatsSADDying, PYSNMP_MODULE_ID=snsIPSECStats)
