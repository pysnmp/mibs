#
# PySNMP MIB module XF-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-TOP-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 07:41:06 2023
# On host fv-az885-747 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, MibIdentifier, enterprises, Bits, Integer32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, iso, Gauge32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "enterprises", "Bits", "Integer32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "iso", "Gauge32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
miniLinkXF = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 81))
miniLinkXF.setRevisions(('2012-10-10 16:00', '2012-08-31 16:00', '2012-06-13 16:00', '2011-09-10 12:00', '2010-09-22 11:00', '2010-04-20 10:00', '2010-01-26 10:00', '2009-03-16 12:00', '2009-01-22 11:00', '2008-02-25 14:44', '2006-01-26 12:24', '2005-02-25 16:00', '2004-01-23 11:11', '2003-06-19 09:24', '2002-03-07 13:29', '2001-10-08 15:01', '2001-04-02 00:00',))
if mibBuilder.loadTexts: miniLinkXF.setLastUpdated('201210101600Z')
if mibBuilder.loadTexts: miniLinkXF.setOrganization('Ericsson')
class XfProductnumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '30t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class XfProductRevision(TextualConvention, OctetString):
    status = 'current'
    displayHint = '40t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class Xf24HrsSeconds(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 86400)

class Xf15MinSeconds(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 900)

class Xf24HrsSecondsGauge(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 86400)

class Xf15MinSecondsGauge(TextualConvention, Gauge32):
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
mibBuilder.exportSymbols("XF-TOP-MIB", XfProductRevision=XfProductRevision, Xf24HrsSecondsGauge=Xf24HrsSecondsGauge, xfMCR=xfMCR, xfPT6010=xfPT6010, xfCN500=xfCN500, xfSysId=xfSysId, XfProductnumber=XfProductnumber, ericsson=ericsson, xfPlatform=xfPlatform, xfMediaSpecific=xfMediaSpecific, xfServiceApplications=xfServiceApplications, xfAtmAggregationUnit=xfAtmAggregationUnit, xfRadioLink=xfRadioLink, Xf15MinSecondsGauge=Xf15MinSecondsGauge, xfIpSau=xfIpSau, miniLinkXF=miniLinkXF, xfSdhAdm=xfSdhAdm, PYSNMP_MODULE_ID=miniLinkXF, xfPDH=xfPDH, xfRps=xfRps, xfCN210=xfCN210, xfSDH=xfSDH, xfCesService=xfCesService, Xf15MinSeconds=Xf15MinSeconds, Xf24HrsSeconds=Xf24HrsSeconds, xfEthernetBridge=xfEthernetBridge)
