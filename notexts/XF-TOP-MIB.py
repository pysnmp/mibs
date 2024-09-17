#
# PySNMP MIB module XF-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-TOP-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:31:14 2024
# On host fv-az975-559 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, enterprises, ModuleIdentity, Gauge32, ObjectIdentity, Bits, Counter32, MibIdentifier, TimeTicks, Counter64, IpAddress, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "enterprises", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "iso")
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
mibBuilder.exportSymbols("XF-TOP-MIB", xfSdhAdm=xfSdhAdm, Xf24HrsSecondsGauge=Xf24HrsSecondsGauge, xfPlatform=xfPlatform, xfRps=xfRps, xfMediaSpecific=xfMediaSpecific, XfProductnumber=XfProductnumber, Xf15MinSeconds=Xf15MinSeconds, xfSysId=xfSysId, xfPT6010=xfPT6010, xfCN210=xfCN210, xfRadioLink=xfRadioLink, PYSNMP_MODULE_ID=miniLinkXF, ericsson=ericsson, xfSDH=xfSDH, xfIpSau=xfIpSau, xfAtmAggregationUnit=xfAtmAggregationUnit, XfProductRevision=XfProductRevision, xfEthernetBridge=xfEthernetBridge, xfServiceApplications=xfServiceApplications, xfMCR=xfMCR, Xf24HrsSeconds=Xf24HrsSeconds, xfCesService=xfCesService, Xf15MinSecondsGauge=Xf15MinSecondsGauge, miniLinkXF=miniLinkXF, xfPDH=xfPDH, xfCN500=xfCN500)
