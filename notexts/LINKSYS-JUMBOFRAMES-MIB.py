#
# PySNMP MIB module LINKSYS-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-JUMBOFRAMES-MIB
# Source digest sha256:7ba308fc9b7e6b09f0c50fbf5d33b48aabe9c46c325e00b37fd83275297af2d7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Linksys LLC.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-JUMBOFRAMES-MIB", PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFrames=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset)
