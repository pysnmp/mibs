#
# PySNMP MIB module BTI8xx-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-TC-MIB
# Produced by pysmi-1.1.12 at Sat Jul  6 01:06:11 2024
# On host fv-az1532-138 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
bti8xx, = mibBuilder.importSymbols("BTI8xx-MIB", "bti8xx")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, iso, Counter64, Bits, MibIdentifier, Integer32, Gauge32, NotificationType, Counter32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter64", "Bits", "MibIdentifier", "Integer32", "Gauge32", "NotificationType", "Counter32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks")
TruthValue, DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
privateManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100))
privateManagement.setRevisions(('2015-11-20 12:00', '2015-02-25 15:00', '2014-10-29 12:00', '2013-12-27 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: privateManagement.setRevisionsDescriptions(('\n        *1. Change the Syntax(for silver creek tool).\n          1.1. DisplayString -> OCTET STRING\n            fruBaseInfoLocation\n            fruBaseInfopackSWVersion\n            fruBaseInfopackShortName\n            fruBaseInfopackName\n            fruBaseInfoPECCode\n            fruBaseInfoCLEI\n            fruBaseInfoserialNumber\n            fruBaseInfomanufacturingDate\n            fruBaseInfomanufacturingLoc\n            fruBaseInfotestedDate\n            fruBaseInfotestedLoc\n            fruBaseInfobaseMacaddress\n            fruBaseInfoUSI\n\n          1.2. Delete syntax value rnage\n            errorInfoDesc\n        ', '\n        *1. Change the access to errorInfo\n          errorInfoCode\n           > R/W -> R/O\n          errorInfoDesc\n           > R/W -> R/O\n        ', '\n        *1. Change the sytax size\n          DisplayString(SIZE(0..256)) -> DisplayString(SIZE(0..255))\n        ', 'Initial version of MIB.',))
if mibBuilder.loadTexts: privateManagement.setLastUpdated('201511201200Z')
if mibBuilder.loadTexts: privateManagement.setOrganization('Actus Networks Ltd.')
if mibBuilder.loadTexts: privateManagement.setContactInfo('\n                  Support:  +82-2-26535666\n                  R&D:      +82-2-26535666\n                  Fax:      +82-2-26534662\n                  Email:    ymkim@actusnetworks.com\n\n                 ')
if mibBuilder.loadTexts: privateManagement.setDescription('This is a top-level MIB for bti whose purpose is to lay out\n                  the top-level objects in the OID hierarchy from which \n                  BTI MIB OIDs descend.')
class TcI1588ClkStratum(TextualConvention, Integer32):
    description = 'Indicates the clk stratum of grand master on i1588 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 7, 128, 248, 254, 255))
    namedValues = NamedValues(("none", 0), ("force", 1), ("stratum1", 6), ("stratum2", 7), ("bestClockStratumthatcanbeSlave", 128), ("stratum3", 248), ("stratum4", 254), ("defaultStratum", 255))

class TcI1588ClkAccuracy(TextualConvention, Integer32):
    description = 'Indicates the clk accuracy of grand master on i1588 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 254))
    namedValues = NamedValues(("t25ns", 32), ("t100ns", 33), ("t250ns", 34), ("t1us", 35), ("t2dot5us", 36), ("t10us", 37), ("t25us", 38), ("t100us", 39), ("t250us", 40), ("t1ms", 41), ("t2dot5ms", 42), ("t10ms", 43), ("t25ms", 44), ("t100ms", 45), ("t250ms", 46), ("t1s", 47), ("t10s", 48), ("t10sExcess", 49), ("tUnknown", 254))

class TcI1588LogPeriod(TextualConvention, Integer32):
    description = 'Indicates the log period of Announce/Sync/delayReq on i1588 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("period0", 1), ("period1", 2), ("period2", 4), ("period3", 8), ("period4", 16), ("period5", 32), ("period6", 64))

class EnableType(TextualConvention, Integer32):
    description = 'The direction of policy  on at interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class RuleAction(TextualConvention, Integer32):
    description = "The value of rule's action.\n             permit: The packet matching the rule will be permitted to forward.\n             deny: The packet matching the rule will be denied.\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class CounterClear(TextualConvention, Integer32):
    description = "cleared: Reset the value of the rule's counter.\n             nouse: 'nouse' will be returned when getting.\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

class PortOp(TextualConvention, Integer32):
    description = 'The operation type of TCP and UDP.\n             lt : Less than given port number.\n             eq : Equal to given port number.\n             gt : Greater than given port number.\n             neq : Not equal to given port number.\n             range : Between two port numbers.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("eq", 0), ("neq", 1), ("gt", 2), ("lt", 3), ("range", 4), ("invalid", 5))

class PrecedenceValue(TextualConvention, Integer32):
    description = "The value of IP-packet's precedence.\n            <0-7>           Value of precedence\n            routine         Specify routine precedence(0)\n            priority        Specify priority precedence(1)\n            immediate       Specify immediate precedence(2)\n            flash           Specify flash precedence(3)\n            flash-override  Specify flash-override precedence(4)\n            critical        Specify critical precedence(5)\n            internet        Specify internetwork control precedence(6)\n            network         Specify network control precedence(7)        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )
class DSCPValue(TextualConvention, Integer32):
    description = 'The value of DSCP.\n             <0-64>  Value of DSCP\n             af11    Specify Assured Forwarding 11 service(10)\n             af12    Specify Assured Forwarding 12 service(12)\n             af13    Specify Assured Forwarding 13 service(14)\n             af21    Specify Assured Forwarding 21 service(18)\n             af22    Specify Assured Forwarding 22 service(20)\n             af23    Specify Assured Forwarding 23 service(22)\n             af31    Specify Assured Forwarding 31 service(26)\n             af32    Specify Assured Forwarding 32 service(28)\n             af33    Specify Assured Forwarding 33 service(30)\n             af41    Specify Assured Forwarding 41 service(34)\n             af42    Specify Assured Forwarding 42 service(36)\n             af43    Specify Assured Forwarding 43 service(38)\n             be      Specify Best Effort service(0)\n             cs1     Specify Class Selector 1 service(8)\n             cs2     Specify Class Selector 2 service(16)\n             cs3     Specify Class Selector 3 service(24)\n             cs4     Specify Class Selector 4 service(32)\n             cs5     Specify Class Selector 5 service(40)\n             cs6     Specify Class Selector 6 service(48)\n             cs7     Specify Class Selector 7 service(56)\n             ef      Specify Expedited Forwarding service(46)\n             nouse   Do not use this filter(64)\n        '
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
if mibBuilder.loadTexts: portIndex.setDescription('The index value that uniquely identifies uplink(NNI) port in Main,\n      TDM port in DS1E1 & OC3 crad and user traffic(UNI) port in FE card.\n      Main  : 1 ~ 4.\n      FE    : 1 ~ 8.\n      DS1E1 : 1 ~ 16.\n      OC3   : 1 ~ 84.\n\t\t\t\t1[1-1-1-1] ~ 7[1-1-7-1], 8[1-1-1-2] ~ 28[1-1-7-4]\n\t\t\t\t29[1-2-1-1] ~ 56[1-2-7-4], 57[1-3-1-1] ~ 84[1-3-7-4]')
ethPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: ethPortIndex.setStatus('current')
if mibBuilder.loadTexts: ethPortIndex.setDescription('The index value that uniquely identifies uplink(NNI) port in Main\n\t\tand user traffic(UNI) port in FE card.\n\t\tMain  : 1 ~ 4.\n\t\tFE    : 1 ~ 8.')
ethopIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: ethopIndex.setStatus('current')
if mibBuilder.loadTexts: ethopIndex.setDescription('The index value that uniquely identifies ETHoP for 8FE Card.')
powerIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: powerIndex.setStatus('current')
if mibBuilder.loadTexts: powerIndex.setDescription('The index value of power card.')
uniIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: uniIndex.setStatus('current')
if mibBuilder.loadTexts: uniIndex.setDescription('The index value of Uni Index.')
evcIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: evcIndex.setStatus('current')
if mibBuilder.loadTexts: evcIndex.setDescription('The index value of Evc Index.')
cosIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: cosIndex.setStatus('current')
if mibBuilder.loadTexts: cosIndex.setDescription('The index value of Cos Index.')
bwCfgIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: bwCfgIndex.setStatus('current')
if mibBuilder.loadTexts: bwCfgIndex.setDescription('The index value of BW Profile Config Type Index.\n\t\t\t1.Ingress\n\t\t\t2.Egress\n\t\t')
bwpDirection = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2))))
if mibBuilder.loadTexts: bwpDirection.setStatus('current')
if mibBuilder.loadTexts: bwpDirection.setDescription('The index value of BW Profile Config Type Index.\n\t\t\t1.Ingress\n\t\t\t2.Egress\n\t\t')
l2cpIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: l2cpIndex.setStatus('current')
if mibBuilder.loadTexts: l2cpIndex.setDescription('Index value of mefL2CPProfileTable ')
mpIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: mpIndex.setStatus('current')
if mibBuilder.loadTexts: mpIndex.setDescription('Index value of oamPM Table ')
sessionResponderEntryId = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: sessionResponderEntryId.setStatus('current')
if mibBuilder.loadTexts: sessionResponderEntryId.setDescription('Index value of oamPM Table ')
testSessionFarEndEntryId = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: testSessionFarEndEntryId.setStatus('current')
if mibBuilder.loadTexts: testSessionFarEndEntryId.setDescription('Index value of oamPM Table ')
sessionIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: sessionIndex.setStatus('current')
if mibBuilder.loadTexts: sessionIndex.setDescription('Index value of RFC2544 Session Index')
fsIndex = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: fsIndex.setStatus('current')
if mibBuilder.loadTexts: fsIndex.setDescription('Index value of RFC2544 Frame Size Index')
fruBaseInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1))
fruBaseInfoTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: fruBaseInfoTable.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoTable.setDescription('   ')
fruBaseInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "BTI8xx-TC-MIB", "fruBaseInfoIndex"))
if mibBuilder.loadTexts: fruBaseInfoEntry.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoEntry.setDescription('')
fruBaseInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoIndex.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoIndex.setDescription('This field is the TableIndex of the Table')
fruBaseInfoLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoLocation.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoLocation.setDescription('This field is the Description of the Device')
fruBaseInfopackSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfopackSWVersion.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfopackSWVersion.setDescription('This field is the software version of the pack')
fruBaseInfopackShortName = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfopackShortName.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfopackShortName.setDescription('This field is the abbreviated name of a pack that is displayed to the customer.')
fruBaseInfopackName = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfopackName.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfopackName.setDescription('This field is the full text name of a pack that is displayed to the customer.')
fruBaseInfoPECCode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoPECCode.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoPECCode.setDescription('\n        This field is the Product Engineering Code text of a pack.\n        This is used by the SCP SW to determine what type of pack is installed\n        ')
fruBaseInfoCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoCLEI.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoCLEI.setDescription('\n        This filed is the alpha numeric CLEI (Common Language Equipment Identifier).\n        The CLEI is a unique alpha numeric string that is managed by Telcordia.\n        ')
fruBaseInfoserialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoserialNumber.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoserialNumber.setDescription('This field is the Serial Number of the pack')
fruBaseInforevision = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInforevision.setStatus('current')
if mibBuilder.loadTexts: fruBaseInforevision.setDescription('This field is the numeric version number of the pack.')
fruBaseInfomanufacturingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfomanufacturingDate.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfomanufacturingDate.setDescription('This field is the string representation of the date the pack was manufactured')
fruBaseInfomanufacturingLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfomanufacturingLoc.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfomanufacturingLoc.setDescription('This field is the string representation of the location that the pack was manufactured.')
fruBaseInfotestedDate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfotestedDate.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfotestedDate.setDescription('This field is the string representation of the date the pack was tested.')
fruBaseInfotestedLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfotestedLoc.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfotestedLoc.setDescription('This field is the string representation of the location that the pack was tested.')
fruBaseInfobaseMacaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfobaseMacaddress.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfobaseMacaddress.setDescription('This field is the base MAC address.')
fruBaseInfonumberOfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfonumberOfMacAddress.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfonumberOfMacAddress.setDescription('This field is the number of MAC address sequentially after the BASE_MACADDR.')
fruBaseInfoUSI = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoUSI.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoUSI.setDescription('Unique Serial Identifier(USI).')
fruBaseInfoIssuedNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruBaseInfoIssuedNumber.setStatus('current')
if mibBuilder.loadTexts: fruBaseInfoIssuedNumber.setDescription('This field is the number of H/W Issue.')
errorInfoCode = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorInfoCode.setStatus('current')
if mibBuilder.loadTexts: errorInfoCode.setDescription('The BTI-specific error code for the set request failure.')
errorInfoDesc = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorInfoDesc.setStatus('current')
if mibBuilder.loadTexts: errorInfoDesc.setDescription('A textual description string that explains the reason\n\t\tfor the failed set request.')
errorInfoClear = MibScalar((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: errorInfoClear.setStatus('current')
if mibBuilder.loadTexts: errorInfoClear.setDescription('Error Info Description clear')
mibBuilder.exportSymbols("BTI8xx-TC-MIB", fruBaseInfopackSWVersion=fruBaseInfopackSWVersion, PYSNMP_MODULE_ID=privateManagement, uniIndex=uniIndex, fruBaseInfoserialNumber=fruBaseInfoserialNumber, errorInfoClear=errorInfoClear, performanceManagement=performanceManagement, cosIndex=cosIndex, privateManagement=privateManagement, RuleAction=RuleAction, fruBaseInfoLocation=fruBaseInfoLocation, TcI1588LogPeriod=TcI1588LogPeriod, ethopIndex=ethopIndex, fruBaseInfoIndex=fruBaseInfoIndex, fruBaseInfoIssuedNumber=fruBaseInfoIssuedNumber, bwpDirection=bwpDirection, fruBaseInfoPECCode=fruBaseInfoPECCode, PortOp=PortOp, fruBaseInfoCLEI=fruBaseInfoCLEI, TcI1588ClkAccuracy=TcI1588ClkAccuracy, fruBaseInfotestedLoc=fruBaseInfotestedLoc, fruBaseInfo=fruBaseInfo, errorInfoCode=errorInfoCode, faultManagement=faultManagement, systemInfo=systemInfo, l2cpIndex=l2cpIndex, fruBaseInfopackShortName=fruBaseInfopackShortName, DSCPValue=DSCPValue, fsIndex=fsIndex, EnableType=EnableType, fruBaseInfoTable=fruBaseInfoTable, fruBaseInfoEntry=fruBaseInfoEntry, fruBaseInfobaseMacaddress=fruBaseInfobaseMacaddress, CounterClear=CounterClear, TcI1588ClkStratum=TcI1588ClkStratum, fruBaseInfoUSI=fruBaseInfoUSI, evcIndex=evcIndex, fruBaseInfopackName=fruBaseInfopackName, testSessionFarEndEntryId=testSessionFarEndEntryId, fruBaseInfomanufacturingDate=fruBaseInfomanufacturingDate, portIndex=portIndex, mpIndex=mpIndex, sessionResponderEntryId=sessionResponderEntryId, fruBaseInfomanufacturingLoc=fruBaseInfomanufacturingLoc, configManagement=configManagement, fruBaseInforevision=fruBaseInforevision, privateManagementTC=privateManagementTC, fruBaseInfotestedDate=fruBaseInfotestedDate, privateManagementConformance=privateManagementConformance, privateManagementGroups=privateManagementGroups, privateManagementCompliances=privateManagementCompliances, fruBaseInfonumberOfMacAddress=fruBaseInfonumberOfMacAddress, mainSystem=mainSystem, bwCfgIndex=bwCfgIndex, ethPortIndex=ethPortIndex, errorInfoDesc=errorInfoDesc, sessionIndex=sessionIndex, PrecedenceValue=PrecedenceValue, fruInfo=fruInfo, errorInfo=errorInfo, powerIndex=powerIndex)
