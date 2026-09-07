#
# PySNMP MIB module CISCOSB-WeightedRandomTailDrop-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-WeightedRandomTailDrop-MIB
# Source digest sha256:9e1e2ae899da64d1070055b7238bde9076bf5368a7117a5f0cae8792a7f8c73c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlWeightedRandomTailDrop = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146))
rlWeightedRandomTailDrop.setRevisions(('2009-09-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setRevisionsDescriptions(('The private MIB module definition for Weighted Random Tail Drop MIB.',))
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setLastUpdated('2009-09-29 00:00')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setDescription('<description>')
rlWeightedRandomTailDropCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setDescription('Show the current Weighted Random Tail Drop status')
rlWeightedRandomTailDropStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setDescription('Set the Weighted Random Tail Drop status after reset')
mibBuilder.exportSymbols("CISCOSB-WeightedRandomTailDrop-MIB", PYSNMP_MODULE_ID=rlWeightedRandomTailDrop, rlWeightedRandomTailDrop=rlWeightedRandomTailDrop, rlWeightedRandomTailDropCurrentStatus=rlWeightedRandomTailDropCurrentStatus, rlWeightedRandomTailDropStatusAfterReset=rlWeightedRandomTailDropStatusAfterReset)
