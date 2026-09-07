#
# PySNMP MIB module LINKSYS-WeightedRandomTailDrop-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-WeightedRandomTailDrop-MIB
# Source digest sha256:d0f4d08566a629b2a6f06a6194de40ef9703baea3ae79933f4066bd5cbb8a388
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlWeightedRandomTailDrop = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 146))
rlWeightedRandomTailDrop.setRevisions(('2009-09-29 00:00',))
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setLastUpdated('2009-09-29 00:00')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setOrganization('Linksys LLC.')
rlWeightedRandomTailDropCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 146, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setStatus('current')
rlWeightedRandomTailDropStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 146, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-WeightedRandomTailDrop-MIB", PYSNMP_MODULE_ID=rlWeightedRandomTailDrop, rlWeightedRandomTailDrop=rlWeightedRandomTailDrop, rlWeightedRandomTailDropCurrentStatus=rlWeightedRandomTailDropCurrentStatus, rlWeightedRandomTailDropStatusAfterReset=rlWeightedRandomTailDropStatusAfterReset)
