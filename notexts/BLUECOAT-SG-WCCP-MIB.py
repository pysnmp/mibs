#
# PySNMP MIB module BLUECOAT-SG-WCCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-WCCP-MIB
# Produced by pysmi-1.1.3 at Sat Nov 20 17:18:57 2021
# On host fv-az121-977 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Counter64, MibIdentifier, Bits, ObjectIdentity, NotificationType, Counter32, Unsigned32, iso, IpAddress, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Counter64", "MibIdentifier", "Bits", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "iso", "IpAddress", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
deviceWccpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 5))
deviceWccpMIB.setRevisions(('2008-01-23 03:00', '2007-11-05 03:00', '2002-08-28 03:00',))
if mibBuilder.loadTexts: deviceWccpMIB.setLastUpdated('200801230300Z')
if mibBuilder.loadTexts: deviceWccpMIB.setOrganization('Blue Coat Systems, Inc.')
class WccpServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standard", 1), ("dynamic", 2), ("unknown", 3))

class WccpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("version1", 1), ("version2", 2), ("unknown", 3))

deviceWccpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 5, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpEnabled.setStatus('current')
deviceWccpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2))
deviceWccpValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1))
deviceWccpValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1), )
if mibBuilder.loadTexts: deviceWccpValueTable.setStatus('current')
deviceWccpValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-WCCP-MIB", "deviceWccpIndex"))
if mibBuilder.loadTexts: deviceWccpValueEntry.setStatus('current')
deviceWccpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceWccpIndex.setStatus('current')
deviceWccpServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceID.setStatus('current')
deviceWccpServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 3), WccpServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceType.setStatus('current')
deviceWccpServiceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 4), WccpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceVersion.setStatus('current')
deviceWccpPacketsRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpPacketsRedir.setStatus('current')
deviceWccpPacketsLowRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpPacketsLowRedir.setStatus('current')
deviceWccpBytesRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 7), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpBytesRedir.setStatus('current')
deviceWccpBytesLowRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 8), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpBytesLowRedir.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-WCCP-MIB", deviceWccpBytesRedir=deviceWccpBytesRedir, WccpServiceType=WccpServiceType, deviceWccpMIBObjects=deviceWccpMIBObjects, deviceWccpServiceType=deviceWccpServiceType, deviceWccpServiceVersion=deviceWccpServiceVersion, deviceWccpIndex=deviceWccpIndex, deviceWccpPacketsRedir=deviceWccpPacketsRedir, deviceWccpServiceID=deviceWccpServiceID, deviceWccpValueTable=deviceWccpValueTable, deviceWccpPacketsLowRedir=deviceWccpPacketsLowRedir, deviceWccpValueEntry=deviceWccpValueEntry, deviceWccpEnabled=deviceWccpEnabled, PYSNMP_MODULE_ID=deviceWccpMIB, deviceWccpBytesLowRedir=deviceWccpBytesLowRedir, deviceWccpValues=deviceWccpValues, deviceWccpMIB=deviceWccpMIB, WccpVersion=WccpVersion)
