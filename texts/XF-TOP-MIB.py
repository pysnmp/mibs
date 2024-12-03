#
# PySNMP MIB module XF-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-TOP-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:55:32 2024
# On host fv-az1117-982 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, TimeTicks, ModuleIdentity, Counter32, Counter64, Unsigned32, enterprises, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "enterprises", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
miniLinkXF = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 81))
miniLinkXF.setRevisions(('2012-10-10 16:00', '2012-08-31 16:00', '2012-06-13 16:00', '2011-09-10 12:00', '2010-09-22 11:00', '2010-04-20 10:00', '2010-01-26 10:00', '2009-03-16 12:00', '2009-01-22 11:00', '2008-02-25 14:44', '2006-01-26 12:24', '2005-02-25 16:00', '2004-01-23 11:11', '2003-06-19 09:24', '2002-03-07 13:29', '2001-10-08 15:01', '2001-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: miniLinkXF.setRevisionsDescriptions(('T : Fixed minor syntax warnings', 'S : Changed to legal revision', 'P : Added xfRps subtree.', 'O : Added xfCesService subtree.', 'N : Added xfPT6010 subtree for PT6010', 'M : Added xfCN500 subtree for compact node 500.', 'L : Added xfCN210 subtree for compact node 210.', 'K : corrected Xf24HrsSeconds to 86400.\n\t\t\t\t', 'J : Length of xfProductRevison increased\n\t\t\t\t    from 10 to 40.', 'H : Added xfSdhAdm', 'G added xfAtmAggregationUnit', 'F changed xfServiceApplications to\n\t\t\t\t  added xfIpSau', 'E Added xfRadioLink', 'D \n\t\t\t\tChanged the Xf15MinSeconds and\n\t\t\t\tXf24Seconds to start with 1', 'C \n\t\t\t\tAdded TC for Product\n\t\t\t\tnumber and revision\n\t\t\t\tAdded TCs for seconds counter 15min\n\t\t\t\tand 24hrs\n\t\t\t\tChanged contact info\n\t\t\t\t', 'B etoall: xfMCR instead xfRadio', 'Rev. A   etoall\n\t\t\t\tInitial version',))
if mibBuilder.loadTexts: miniLinkXF.setLastUpdated('201210101600Z')
if mibBuilder.loadTexts: miniLinkXF.setOrganization('Ericsson')
if mibBuilder.loadTexts: miniLinkXF.setContactInfo(' ')
if mibBuilder.loadTexts: miniLinkXF.setDescription('This MIB specifies the highest level OIDs for \n\t\t\t\tthe MINI-LINK Traffic Node product.\n\t\t\t\t')
class XfProductnumber(TextualConvention, OctetString):
    description = "A string indicating the product number\n\t\t\t\tlike 'RORJ605 001/1'. The string must be compliant to \n\t\t\t\tstandard Ericsson format for product numbers."
    status = 'current'
    displayHint = '30t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class XfProductRevision(TextualConvention, OctetString):
    description = "String indicating a product revision like 'R1A00'. \n\t\t\t\tThe string must comply to standard Ericsson product \n\t\t\t\trevision numbers.\n\t\t\t\t"
    status = 'current'
    displayHint = '40t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class Xf24HrsSeconds(TextualConvention, Integer32):
    description = 'General definition for perfomance threshold for 24 hours.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 86400)

class Xf15MinSeconds(TextualConvention, Integer32):
    description = 'General definition for perfomance threshold for 15 minutes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 900)

class Xf24HrsSecondsGauge(TextualConvention, Gauge32):
    description = 'General definition for counting the number of seconds \n\t\t\t\tin 24 hours.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 86400)

class Xf15MinSecondsGauge(TextualConvention, Gauge32):
    description = 'General definition for counting the number of seconds \n\t\t\t\tin 15 minutes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 900)

ericsson = MibIdentifier((1, 3, 6, 1, 4, 1, 193))
xfSysId = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 1))
xfPlatform = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 2))
xfMediaSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3))
xfPDH = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 1))
xfSDH = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 2))
xfMCR = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 3))
xfRadioLink = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4))
xfServiceApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 4))
xfEthernetBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 4, 1))
xfAtmAggregationUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 4, 2))
xfSdhAdm = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 4, 3))
xfCesService = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 4, 4))
xfRps = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 4, 5))
xfIpSau = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 5))
xfCN210 = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 6))
xfCN500 = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 7))
xfPT6010 = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 8))
mibBuilder.exportSymbols("XF-TOP-MIB", xfAtmAggregationUnit=xfAtmAggregationUnit, ericsson=ericsson, Xf15MinSeconds=Xf15MinSeconds, xfPDH=xfPDH, XfProductRevision=XfProductRevision, xfSdhAdm=xfSdhAdm, xfMCR=xfMCR, PYSNMP_MODULE_ID=miniLinkXF, xfPT6010=xfPT6010, Xf24HrsSecondsGauge=Xf24HrsSecondsGauge, xfMediaSpecific=xfMediaSpecific, xfCN500=xfCN500, xfIpSau=xfIpSau, xfSysId=xfSysId, xfSDH=xfSDH, xfRadioLink=xfRadioLink, xfCN210=xfCN210, xfServiceApplications=xfServiceApplications, xfPlatform=xfPlatform, miniLinkXF=miniLinkXF, xfRps=xfRps, Xf24HrsSeconds=Xf24HrsSeconds, XfProductnumber=XfProductnumber, Xf15MinSecondsGauge=Xf15MinSecondsGauge, xfEthernetBridge=xfEthernetBridge, xfCesService=xfCesService)
