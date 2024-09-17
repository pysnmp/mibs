#
# PySNMP MIB module BTI8xx-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-TC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 09:57:47 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
bti8xx, = mibBuilder.importSymbols("BTI8xx-MIB", "bti8xx")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
PerfIntervalCount, PerfCurrentCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount", "PerfTotalCount")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, MibIdentifier, IpAddress, Unsigned32, Counter32, Bits, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "MibIdentifier", "IpAddress", "Unsigned32", "Counter32", "Bits", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "ObjectIdentity", "Gauge32")
TextualConvention, RowStatus, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "TruthValue", "DisplayString")
privateManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100))
privateManagement.setRevisions(('2015-11-20 12:00', '2015-02-25 15:00', '2014-10-29 12:00', '2013-12-27 12:00',))
if mibBuilder.loadTexts: privateManagement.setLastUpdated('201511201200Z')
if mibBuilder.loadTexts: privateManagement.setOrganization('Actus Networks Ltd.')
class TcI1588ClkStratum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 7, 128, 248, 254, 255))
    namedValues = NamedValues(("none", 0), ("force", 1), ("stratum1", 6), ("stratum2", 7), ("bestClockStratumthatcanbeSlave", 128), ("stratum3", 248), ("stratum4", 254), ("defaultStratum", 255))

class TcI1588ClkAccuracy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 254))
    namedValues = NamedValues(("t25ns", 32), ("t100ns", 33), ("t250ns", 34), ("t1us", 35), ("t2dot5us", 36), ("t10us", 37), ("t25us", 38), ("t100us", 39), ("t250us", 40), ("t1ms", 41), ("t2dot5ms", 42), ("t10ms", 43), ("t25ms", 44), ("t100ms", 45), ("t250ms", 46), ("t1s", 47), ("t10s", 48), ("t10sExcess", 49), ("tUnknown", 254))

class TcI1588LogPeriod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("period0", 1), ("period1", 2), ("period2", 4), ("period3", 8), ("period4", 16), ("period5", 32), ("period6", 64))

class EnableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class RuleAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

class PortOp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("eq", 0), ("neq", 1), ("gt", 2), ("lt", 3), ("range", 4), ("invalid", 5))

class PrecedenceValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )
class DSCPValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

configManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1))
performanceManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 3))
faultManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 4))
privateManagementConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 9))
privateManagementTC = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10))
systemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1))
mainSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2))
fruInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1))
errorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2))
privateManagementGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 9, 1))
privateManagementCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 9, 2))
portIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 84)))
if mibBuilder.loadTexts: portIndex.setStatus('current')
ethPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: ethPortIndex.setStatus('current')
ethopIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: ethopIndex.setStatus('current')
powerIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: powerIndex.setStatus('current')
uniIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: uniIndex.setStatus('current')
evcIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: evcIndex.setStatus('current')
cosIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: cosIndex.setStatus('current')
bwCfgIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: bwCfgIndex.setStatus('current')
bwpDirection = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2))))
if mibBuilder.loadTexts: bwpDirection.setStatus('current')
l2cpIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: l2cpIndex.setStatus('current')
mpIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: mpIndex.setStatus('current')
sessionResponderEntryId = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: sessionResponderEntryId.setStatus('current')
testSessionFarEndEntryId = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: testSessionFarEndEntryId.setStatus('current')
sessionIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: sessionIndex.setStatus('current')
fsIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: fsIndex.setStatus('current')
fruBaseInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1))
fruBaseInfoTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: fruBaseInfoTable.setStatus('current')
fruBaseInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "BTI8xx-TC-MIB", "fruBaseInfoIndex"))
if mibBuilder.loadTexts: fruBaseInfoEntry.setStatus('current')
fruBaseInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoIndex.setStatus('current')
fruBaseInfoLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoLocation.setStatus('current')
fruBaseInfopackSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfopackSWVersion.setStatus('current')
fruBaseInfopackShortName = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfopackShortName.setStatus('current')
fruBaseInfopackName = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfopackName.setStatus('current')
fruBaseInfoPECCode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoPECCode.setStatus('current')
fruBaseInfoCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoCLEI.setStatus('current')
fruBaseInfoserialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoserialNumber.setStatus('current')
fruBaseInforevision = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInforevision.setStatus('current')
fruBaseInfomanufacturingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfomanufacturingDate.setStatus('current')
fruBaseInfomanufacturingLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfomanufacturingLoc.setStatus('current')
fruBaseInfotestedDate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfotestedDate.setStatus('current')
fruBaseInfotestedLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfotestedLoc.setStatus('current')
fruBaseInfobaseMacaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfobaseMacaddress.setStatus('current')
fruBaseInfonumberOfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfonumberOfMacAddress.setStatus('current')
fruBaseInfoUSI = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoUSI.setStatus('current')
fruBaseInfoIssuedNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoIssuedNumber.setStatus('current')
errorInfoCode = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorInfoCode.setStatus('current')
errorInfoDesc = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorInfoDesc.setStatus('current')
errorInfoClear = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: errorInfoClear.setStatus('current')
mibBuilder.exportSymbols("BTI8xx-TC-MIB", EnableType=EnableType, ethPortIndex=ethPortIndex, fruBaseInfoIssuedNumber=fruBaseInfoIssuedNumber, errorInfo=errorInfo, mpIndex=mpIndex, TcI1588ClkAccuracy=TcI1588ClkAccuracy, privateManagementTC=privateManagementTC, fruBaseInfomanufacturingDate=fruBaseInfomanufacturingDate, TcI1588LogPeriod=TcI1588LogPeriod, sessionResponderEntryId=sessionResponderEntryId, fruBaseInfoPECCode=fruBaseInfoPECCode, TcI1588ClkStratum=TcI1588ClkStratum, fruBaseInfo=fruBaseInfo, fruBaseInfotestedDate=fruBaseInfotestedDate, errorInfoDesc=errorInfoDesc, powerIndex=powerIndex, fruBaseInfonumberOfMacAddress=fruBaseInfonumberOfMacAddress, errorInfoCode=errorInfoCode, PYSNMP_MODULE_ID=privateManagement, fruBaseInfoTable=fruBaseInfoTable, CounterClear=CounterClear, mainSystem=mainSystem, sessionIndex=sessionIndex, errorInfoClear=errorInfoClear, fruBaseInforevision=fruBaseInforevision, fruBaseInfopackSWVersion=fruBaseInfopackSWVersion, fruBaseInfoLocation=fruBaseInfoLocation, fruBaseInfotestedLoc=fruBaseInfotestedLoc, fruBaseInfoEntry=fruBaseInfoEntry, portIndex=portIndex, cosIndex=cosIndex, evcIndex=evcIndex, fruBaseInfoCLEI=fruBaseInfoCLEI, l2cpIndex=l2cpIndex, PrecedenceValue=PrecedenceValue, privateManagement=privateManagement, fruBaseInfoserialNumber=fruBaseInfoserialNumber, uniIndex=uniIndex, performanceManagement=performanceManagement, fsIndex=fsIndex, fruBaseInfopackShortName=fruBaseInfopackShortName, fruBaseInfobaseMacaddress=fruBaseInfobaseMacaddress, PortOp=PortOp, systemInfo=systemInfo, fruBaseInfomanufacturingLoc=fruBaseInfomanufacturingLoc, bwpDirection=bwpDirection, privateManagementCompliances=privateManagementCompliances, faultManagement=faultManagement, bwCfgIndex=bwCfgIndex, ethopIndex=ethopIndex, testSessionFarEndEntryId=testSessionFarEndEntryId, privateManagementConformance=privateManagementConformance, fruBaseInfopackName=fruBaseInfopackName, privateManagementGroups=privateManagementGroups, fruBaseInfoIndex=fruBaseInfoIndex, RuleAction=RuleAction, fruInfo=fruInfo, fruBaseInfoUSI=fruBaseInfoUSI, DSCPValue=DSCPValue, configManagement=configManagement)
