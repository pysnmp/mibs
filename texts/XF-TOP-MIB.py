#
# PySNMP MIB module XF-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-TOP-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:42:15 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, iso, Unsigned32, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "Unsigned32", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("XF-TOP-MIB", xfSdhAdm=xfSdhAdm, xfRadioLink=xfRadioLink, xfServiceApplications=xfServiceApplications, Xf15MinSeconds=Xf15MinSeconds, xfAtmAggregationUnit=xfAtmAggregationUnit, xfEthernetBridge=xfEthernetBridge, XfProductRevision=XfProductRevision, Xf24HrsSeconds=Xf24HrsSeconds, xfCN210=xfCN210, xfRps=xfRps, xfMCR=xfMCR, xfPDH=xfPDH, xfCesService=xfCesService, ericsson=ericsson, xfSysId=xfSysId, xfMediaSpecific=xfMediaSpecific, PYSNMP_MODULE_ID=miniLinkXF, xfIpSau=xfIpSau, Xf24HrsSecondsGauge=Xf24HrsSecondsGauge, XfProductnumber=XfProductnumber, xfPT6010=xfPT6010, xfPlatform=xfPlatform, xfCN500=xfCN500, Xf15MinSecondsGauge=Xf15MinSecondsGauge, miniLinkXF=miniLinkXF, xfSDH=xfSDH)
