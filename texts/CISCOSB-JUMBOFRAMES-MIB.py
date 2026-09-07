#
# PySNMP MIB module CISCOSB-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-JUMBOFRAMES-MIB
# Source digest sha256:ad56bd5f8495ade2c920db4cf6ccc9601e3b9853a20fe577833de3a707de0c4b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlJumboFrames.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlJumboFrames.setContactInfo('Postal: 170 West Tasman Drive\n                San Jose , CA 95134-1706\n                USA\n\n                \n                Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlJumboFrames.setDescription('This private MIB module defines Jumbo Frames private MIBs.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setDescription('Show the current Jumbo Frames status')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setDescription('Set the Jumbo Frames status after reset')
mibBuilder.exportSymbols("CISCOSB-JUMBOFRAMES-MIB", PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFrames=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset)
