#
# PySNMP MIB module OMNITRON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/omnitron/OMNITRON-TC-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 10:20:33 2023
# On host fv-az627-713 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Counter32, ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "enterprises", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ostOmnitronTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7342, 11))
ostOmnitronTcMib.setRevisions(('2015-05-13 12:00', '2015-01-21 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ostOmnitronTcMib.setRevisionsDescriptions(('Added OstIpv6Addr, OstIpAddr\n                ', 'Initial version of v5.2 MIB.\n                   Added OstAccessibiltyType from the OMNITRON-ACL-MIB\n                ',))
if mibBuilder.loadTexts: ostOmnitronTcMib.setLastUpdated('201505131200Z')
if mibBuilder.loadTexts: ostOmnitronTcMib.setOrganization('Omnitron Systems Technology, Inc.')
if mibBuilder.loadTexts: ostOmnitronTcMib.setContactInfo('Omnitron Systems Technology, Inc.\n                  38 Tesla\n                  Irvine, CA 92618-4670\n                  USA\n\n             Tel: (949) 250 6510\n             Fax: (949) 250 6514\n          E-mail: info@omnitron-systems.com\n   International:  949 250 6510\n\n                  Technical Support and Customer Service\n             Tel: (800) 675 8410\n          E-mail: support@omnitron-systems.com\n   International:  949 250 6510')
if mibBuilder.loadTexts: ostOmnitronTcMib.setDescription('Omnitron TC MIB for use with v5.2 iConverter Management Modules\n             and NetOutlook\n\n             Copyright 2015 Omnitron Systems Technology, Inc.\n             All rights reserved\n            ')
omnitron = MibIdentifier((1, 3, 6, 1, 4, 1, 7342))
icAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 1))
class OstAccessibiltyType(TextualConvention, Integer32):
    description = 'Accessibilty type enumeration.\n\n         deny(1)       Access to the module is not allowed\n         permit(2)     Access to the module is allowed\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

class OstClassOfService(TextualConvention, Unsigned32):
    description = 'Class of service setting.  0=discard, 1=lowest class, 4=highest class'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class OstClockFreq(TextualConvention, Unsigned32):
    description = 'Clock frequency in hundreths of MHz.'
    status = 'current'
    displayHint = 'd-2'

class OstCosL2cpDstAddr(TextualConvention, Unsigned32):
    description = 'L2CP destination address enumeration.\n\n         Index | Destination Address | Name\n         ------+--------------------+---------\n             1 | 01-80-C2-00-00-00   | RSTP\n             2 | 01-80-C2-00-00-01   | Pause\n             3 | 01-80-C2-00-00-02   | LACP\n             4 | 01-80-C2-00-00-02   | Marker\n             5 | 01-80-C2-00-00-02   | Link OAM\n             6 | 01-80-C2-00-00-02   |\n             7 | 01-80-C2-00-00-03   | 802.1x\n             8 | 01-80-C2-00-00-04   | IEEE MAC\n             9 | 01-80-C2-00-00-05   |\n            10 | 01-80-C2-00-00-06   |\n            11 | 01-80-C2-00-00-07   | E-LMI\n            12 | 01-80-C2-00-00-08   | Pr Bridge\n            13 | 01-80-C2-00-00-09   |\n            14 | 01-80-C2-00-00-0A   |\n            15 | 01-80-C2-00-00-0B   |\n            16 | 01-80-C2-00-00-0C   |\n            17 | 01-80-C2-00-00-0D   | GVRP\n            18 | 01-80-C2-00-00-0E   | LLDP\n            19 | 01-80-C2-00-00-0F   |\n            20 | 01-80-C2-00-00-20   | GARP\n        '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 20)

class OstCosNameString(TextualConvention, OctetString):
    description = 'A class of service name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstCosNameStringOrNone(TextualConvention, OctetString):
    description = 'A class of service name or an empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 45)

class OstCosTrustType(TextualConvention, Integer32):
    description = 'CoS trust type enumeration.\n\n         Green traffic is marked with low drop precedence and yellow\n         traffic is marked with high drop precedence.\n\n         cosTrust(1)        Trust frame. The frames priority\n                            determines the egress class.\n\n         cosUsePri(2)       Use the priority ostCosPriority for the\n                            frame. The frame will egress with ostCosPriority\n                            priority and ostCosPrirority determines the\n                            egress class.\n\n         cosUseClass(3)     Use the class ostCosClass for the frame.\n                            The frame will egress with the frames\n                            priority and the ostCosClass egress class.\n\n         cosUsePriClass(4)  Use the priority ostCosPriority and class\n                            ostCosClass for the frame. The frames will\n                            egress with ostCosPri and ostCosClass egress\n                            class.\n\n         cosGreenYellow(5)  Use ostCosGreenPriority and ostCosGreenClass for\n                            green traffic. Use ostCosYellowPriority and\n                            ostCosYellowClass for yellow traffic.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cosTrust", 1), ("cosUsePri", 2), ("cosUseClass", 3), ("cosUsePriClass", 4), ("cosGreenYellow", 5))

class OstEgressSchedulingProfileIndexType(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies an Egress Scheduling Profile.\n\n        The valid values are 1 to X, where X is the maximum supported profile.\n        The maximum value for X for the GM4 is 4.\n       '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class OstEgressQueueIndexType(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies an Egress Queue.\n\n        The valid values are 1 to X, where X is the maximum supported profile.\n        The maximum value for X for the GM4 is 4.\n       '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class OstElpsProtectType(TextualConvention, Integer32):
    description = 'A value that represents the ELPS protection type.  The value can be one\n        of the following:\n\n        e1plus1UniNoAps(1)   1 unidirectional without APS communication\n        e1plus1UniAps(2)     1 unidirectional switching with APS communication\n        e1plus1BiAps(3)      1 bidirectional w/APS communication\n        e1to1(4)             1:1 bidirectional w/APS communication\n        notAvailable(5)      Protect Type is unknown or not available, value returned\n                                 for status read, not allowed to write\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("e1plus1UniNoAps", 1), ("e1plus1UniAps", 2), ("e1plus1BiAps", 3), ("e1to1", 4), ("notAvailable", 5))

class OstElpsRequestStates(TextualConvention, Integer32):
    description = 'A value that represents the current request/state of either the local or\n        remote (partner) ELPS instance.  The value can be one of the following:\n\n        noRequest(0)             No Request (NR), lowest priority\n        doNotRevert(1)           Do Not Revert (DNR)\n        revertRequest(2)         Revert request (RR)\n        exercise(4)              Exercise APS protocol (EXER)\n        waitToRestore(5)         Wait to restore (WTR)\n        manualSwitchWorking(6)   Manual swtich to working (MS-W)\n        manualSwitch(7)          Manual switch (MS)\n        signalDegrade(9)         Signal degrade (SD)\n        signalFailWorking(11)    Signal fail for working (SF)\n        forcedSwitch(13)         Forced switch (FS)\n        signalFailProtection(14) Signal fail for protection (SF-P)\n        lockoutProtection(15)    Lock of protection (LO), highest priority\n        notAvailable(16)         Status is unknown or not available, value returned\n                                 for status read, not allowed to write\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16))
    namedValues = NamedValues(("noRequest", 0), ("doNotRevert", 1), ("revertRequest", 2), ("exercise", 4), ("waitToRestore", 5), ("manualSwitchWorking", 6), ("manualSwitch", 7), ("signalDegrade", 9), ("signalFailWorking", 11), ("forcedSwitch", 13), ("signalFailProtection", 14), ("lockoutProtection", 15), ("notAvailable", 16))

class OstElpsSignalStates(TextualConvention, Integer32):
    description = 'A value that represents the requested or bridged signal for either\n        the local or remote (partner) ELPS instance.  The value can be one of\n        the following:\n\n        nullSignal(0)            Null signal. This indicates the signal that\n                                 the near-end requests be carried over the\n                                 protection path\n        normalSignal(1)          Normal traffic signal. This indicates the\n                                 signal that is bridged onto the protection\n                                 path.\n        notAvailable(2)          Protect Type is unknown or not available, value\n                                 returned for status read, not allowed to write\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nullSignal", 0), ("normalSignal", 1), ("notAvailable", 2))

class OstErpsLinkState(TextualConvention, Integer32):
    description = 'A value that represents the current port link state. This is a\n        function that indicates whether the current port is linked.\n        The value can be one of the following:\n\n        na(0)                    Not Applicable, port state is unknown\n        up(1)                    Port is linked and capable of passing traffic\n        down(2)                  Port is not linked and is not capable of\n                                 passing traffic\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class OstErpsPortState(TextualConvention, Integer32):
    description = 'A value that represents the current forwarding state of the port.\n        The value can be one of the following:\n\n        na(0)                    Not Applicable, port state is unknown\n        forward(1)               Port is in the forwarding state\n        blocked(2)               Port is in the blocked state\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("forward", 1), ("blocked", 2))

class OstErpsPortType(TextualConvention, Integer32):
    description = 'A value that represents the Ring Port type. The value can be one of the\n        following:\n\n        rp0(1)                   Ring Port 0\n        rp1(2)                   Ring Port 1\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rp0", 1), ("rp1", 2))

class OstErpsRingStates(TextualConvention, Integer32):
    reference = '[ITU-T G.8032] Table 10-1'
    description = 'A value that represents the current request/state of either the local or\n        remote (partner) ERPS instance.  The value can be one of the following:\n\n        noRequest(0)             No Request (NR), local, lowest priority\n        rapsNr(1)                Ring APS (R-APS) No Request (NR), remote\n        rapsNrRb(2)              Ring APS (R-APS) No Request (NR), RPL Blocked (RB), remote\n        wtbRunning(3)            Wait to Block (WTB) running, local\n        wtbExpires(4)            Wait to Block (WTB) expires, local\n        wtrRunning(5)            Wait to Restore (WTR) running, local\n        wtrExpires(6)            Wait to Restore (WTR) expires, local\n        manualSwitch(7)          Manual Switch (MS), local\n        rapsManualSwitch(8)      Ring APS (R-APS) Manual Switch (MS), remote\n        rapsSignalFail(9)        Ring APS (R-APS) Signal Fail (SF), remote\n        localClearSignalFail(10) Local clear Signal Fail (SF), local\n        localSignalFail(11)      Local Signal Fail (SF), local\n        rapsForcedSwitch(12)     Ring APS (R-APS) Forced Switch (FS), remote\n        forcedSwtich(13)         Forced Switch (FS), local\n        clear(14)                Clear, local\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("noRequest", 0), ("rapsNr", 1), ("rapsNrRb", 2), ("wtbRunning", 3), ("wtbExpires", 4), ("wtrRunning", 5), ("wtrExpires", 6), ("manualSwitch", 7), ("rapsManualSwitch", 8), ("rapsSignalFail", 9), ("localClearSignalFail", 10), ("localSignalFail", 11), ("rapsForcedSwitch", 12), ("forcedSwtich", 13), ("clear", 14))

class OstErpsRingStatus(TextualConvention, Integer32):
    reference = '[ITU-T G.8032] Table 10-2'
    description = 'A value that represents the current ring status. This is state machine node\n        state value for the ERPS instance.  The value can be one of the\n        following:\n\n        initializing(1)          State machine initialization\n        idle(2)                  Idle State (A)\n        protection(3)            Protection (B)\n        manualSwitch(4)          Manual Switch (C)\n        forcedSwitch(5)          Forced Switch (D)\n        pending(6)               Pending (E)\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initializing", 1), ("idle", 2), ("protection", 3), ("manualSwitch", 4), ("forcedSwitch", 5), ("pending", 6))

class OstErrorString(TextualConvention, OctetString):
    description = 'The SNMP error string for further definition of a SNMP error.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class OstEvcNameString(TextualConvention, OctetString):
    description = 'An EVC name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstEvcNameStringOrNone(TextualConvention, OctetString):
    description = 'An EVC name or an empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 45)

class OstFileNameString(TextualConvention, OctetString):
    description = 'A internal file name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstFingerprintString(TextualConvention, OctetString):
    description = 'The fingerprint value for SSH protocol.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class OstFloatValue(TextualConvention, OctetString):
    description = 'Floating point data type as represented in an octet string.\n        Legal values and precision are indicated by the appropriate object.\n        Only numbers and the decimal place are legal digit values.\n\n        Example values:\n           1000\n           1500.05\n           1545.25\n       '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class OstFrameCount64(TextualConvention, Counter64):
    description = 'Frame counter value.'
    status = 'current'
    displayHint = 'd'

class OstFrameSizeList(TextualConvention, OctetString):
    description = "\n        Denotes a list of one or more frame sizes.\n\n        1. Frame sizes have a value from 64 to 10240 bytes for the GM3, GM4,\n           and GM4-PoE. Frame sizes have a value from 64 to 10240 bytes for\n           the XM5.\n\n        2. Individual frame sizes are included when separated by a comma ','.\n\n        3. A range of frame sizes is included when separated by '..'.\n\n        4. A range of sizes ending in a colon and a value, i.e. start..end:value,\n           is the frame increment size for the next iteration (min value is 4)\n\n        5. Ranges must be organized min size to max size, i.e. min..max\n\n        6. Individual sizes can be mixed in any order\n\n        Example values:\n          64\n          64..1024:64\n          64,128,256,512,1024,1280,1518,10000\n       "
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class OstIndexIntegerNextFree(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a new index in a table.\n\n        The special value of 0 indicates that no more new entries can\n        be created in the relevant table.\n\n        When a MIB is used for configuration, an object with this\n        SYNTAX always contains a legal value (if non-zero) for an\n        index that is not currently used in the relevant table. The\n        Command Generator (Network Management Application) reads this\n        variable and uses the (non-zero) value read when creating a\n        new row with an SNMP SET.  When the SET is performed, the\n        Command Responder (agent) MUST determine whether the value is\n        indeed still unused; Two Network Management Applications may\n        attempt to create a row (configuration entry) simultaneously\n        and use the same value. If it is currently unused, the SET\n        succeeds and the Command Responder (agent) changes the value\n        of this object, according to an implementation-specific\n        algorithm.  If the value is in use, however, the SET fails.\n        The Network Management Application MUST then re-read this\n        variable to obtain a new usable value.\n\n        An OBJECT-TYPE definition using this SYNTAX MUST specify the\n        relevant table for which the object is providing this\n        functionality.\n       '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class OstIpPriorityList(TextualConvention, OctetString):
    description = 'Selects IP priority values.  Valid values are from 0 to 63.\n        Format:\n            X       selects a single PCP priority value\n            X..Y    selects a range of PCP priority values, X to Y\n            X,Y     selects PCP priority values seperated by a comma\n        Example values:\n         0\n         2..5\n         0,2..5\n       '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class OstIpv6Addr(TextualConvention, OctetString):
    description = 'This data type is used to model the IPv6 address. This is a\n        binary string of up to 8 octets in network byte-order.\n       '
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class OstIpAddr(TextualConvention, OctetString):
    description = "This data type is used to model both IPv4 and IPv6 addresses. It\n        is a hexadecimcal octet string with separators between number groups:\n        either '.' for IPv4 or ':' for IPv6. The IP type is derived based upon\n        the format of the string. Valid IP addreses:\n            '192.168.1.220'\n            'fe80:0000:0:0:1234:5678:abcd:efff'\n\n       "
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 39)

class OstMhfCreation(TextualConvention, Integer32):
    description = 'Indicates if the Management Entity can create MHFs.\n\n        The valid values are:\n                ostMHFdefault(2) MHFs can be created on this VID on any\n                        Bridge port through which this VID can pass.\n                ostMHFexplicit(3) MHFs can be created for this VID only on\n                        Bridge ports through which this VID can\n                        pass, and only if a MEP is created at some\n                        lower MD Level.\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ostMHFdefault", 1), ("ostMHFexplicit", 2))

class OstMipdMethodOfCreation(TextualConvention, Integer32):
    description = 'Indicates the method of how this Mip table entry was created\n        The valid values are:\n                ostExplicit(1) indicates the Mip was created explicitly\n                        through a command.\n                ostImplicitMa(2) indicates the Mip was created implicitly\n                        through the MA command.\n                ostImplicitMde(3) indicates the Mip was created implicitly\n                        through the CFM default Md table.\n                ostExplicitImplicitMa(4) indicates the Mip was created both\n                        implicitly and explicitly through the MA command.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ostExplicit", 1), ("ostImplicitMa", 2), ("ostImplicitMde", 3), ("ostExplicitImplicitMa", 4))

class OstModeType(TextualConvention, Integer32):
    description = 'The module Mode Type as AP, SP or neither.\n\n         normal(1)   Not specifically AP or SP\n         ap(2)       Access Provider\n         sp(3)       Service Provider\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("ap", 2), ("sp", 3))

class OstModuleSingleIndex(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies the chassis and slot in which the module is located.\n       Base 10 Format: CCSS where\n            CC is the chassis index, 1 to 99\n            SS is the slot index, 1 to 99'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(101, 9999)

class OstPcpPriorityList(TextualConvention, OctetString):
    description = 'Selects PCP priority values.  Valid values are from 0 to 7.\n        Format:\n            X       selects a single PCP priority value\n            X..Y    selects a range of PCP priority values, X to Y\n            X,Y     selects PCP priority values seperated by a comma\n        Example values:\n         0\n         2..5\n         0,2..5\n       '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class OstPortClockType(TextualConvention, Integer32):
    description = 'A value that indicates the TDM port recovery state/mode.\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("adaptiveIdle", 1), ("adaptiveAcqu", 2), ("adaptiveTrk1", 3), ("adaptiveTrk2", 4), ("holdOver", 5), ("coax", 6), ("internal", 7), ("line", 8))

class OstPortList(TextualConvention, OctetString):
    description = "Denotes a list of one or more ports, separated by comma characters, in the\n        form of an ASCII string, which is case insensitive.\n\n        Port  Description\n        ----  ------------------\n         1    Port 1\n         2    Port 2\n         3    Port 3\n         4    Port 4\n         5    Port 5\n         6    Port 6\n         7    Port 7\n         8    Port 8\n         9    Port 9\n         10   Port 10\n         11   Port 11\n         12   Port 12\n         13   Port 13\n         14   Port 14\n         15   Port 15\n         16   Port 16\n         17   Port 17\n         a    backplane port A\n         b    backplane port B\n         mgt1 management port 1\n         mgt2 management port 2\n         all  includes all ports\n\n        Example: '1,2,a,mgt1'\n        "
    status = 'current'
    displayHint = '255a'

class OstPortNumber(TextualConvention, Unsigned32):
    description = "This object selects the port number for the specific test\n        instance that is configured.\n\n        This value is dependent upon actual product accessed. The port number\n        for a specific port can be determined by selecting the module type\n        and then the port that is accessed. A value of '0' indicates that\n        no port is defined.\n\n        Module Type        P1   P2   P3   P4   P5   BP A  BP B  Mgt1  Mgt2\n        -----------------  ---  ---  ---  ---  ---  ----  ----  ----  ----\n        3-port plug-in     1    2    3    n/a  n/a  4     5     6     7\n        3-port standalone  1    2    3    n/a  n/a  n/a   n/a   6     7\n        2-port plug-in     1    2    n/a  n/a  n/a  3     4     5     6\n        2-port standalone  1    2    n/a  n/a  n/a  n/a   n/a   5     6\n        4-port             1    2    3    4    n/a  5     6     n/a   n/a\n        5-port             1    2    3    4    5    n/a   n/a   6     7\n\n        For the 7 port module: Port 1 - Port 7 are ports 1 - 7 are the front\n        facing ports, port 8 is the dedicated management port, port 9 is Mgt1\n        and port 10 is Mgt2.\n\n        For the 16 port module: Port 1 - Port 16 are the customer facing\n        ports, port 17 is the dedicated management port, port 18 is Mgt1 and\n        port 19 is Mgt2.\n\n        Other values are undefined.\n      "
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 99)

class OstPortSingleIndex(TextualConvention, Unsigned32):
    description = 'A value that uniquely identifies a module port, and the chassis and slot in\n       which the module is located.\n       Base 10 Format: CCSSPP where\n            CC is the chassis index, 1 to 99\n            SS is the slot index, 1 to 99\n            PP is the port index, 1 to 99'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(10101, 999999)

class OstPriority(TextualConvention, Unsigned32):
    description = 'Priority setting.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class OstProbeNameString(TextualConvention, OctetString):
    description = 'An EVC name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstProfileNameString(TextualConvention, OctetString):
    description = 'A test profile name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class OstTestResultType(TextualConvention, Integer32):
    description = 'A value that indicates the result of a test.  The value can be one of\n        the following:\n\n        pass(1)              Indicates the test has passed successfully\n        fail(2)              Indicates the test has failed\n        oversubscribe(3)     Indicates the test failed due to oversubscription\n                             of a resource\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pass", 1), ("fail", 2), ("oversubscribe", 3))

class OstTestStatusType(TextualConvention, Integer32):
    description = 'A value that indicates the status of the current test instance.  The\n        value can be one of the following:\n\n        testNotStarted(1)    Current test instance has not started yet,\n                             not fully configured, or waiting for loop-up\n        testInProcess(2)     Current test instance is currently running\n        testStopped(3)       Current test instance has been stopped after running\n                             for a period of time\n        testCompleted(4)     Current test instance has completed\n        testInitializing(5)  Current test is the process of starting, used to\n                             restart a test in process, completed, or stopped\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("testNotStarted", 1), ("testInProcess", 2), ("testStopped", 3), ("testCompleted", 4), ("testInitializing", 5))

class OstUnsigned64(TextualConvention, Counter64):
    description = 'A non-negative 64-bit bit integer, without counter semantics, between 0\n        and 2^64-1 inclusive (0 to 18446744073709551615 decimal).\n\n        It can have a MAX-ACCESS of read-only or read-write.\n\n        SYNTAX is Counter64 for the encoding rules only.\n       '
    status = 'current'
    displayHint = 'd'

class OstUserNameString(TextualConvention, OctetString):
    description = 'A string that is used to identify a specific user.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class OstVlanId(TextualConvention, Integer32):
    description = 'The VLAN-ID that uniquely identifies a VLAN.  This\n        is the 12-bit VLAN-ID used in the VLAN Tag header.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class OstVlanIdList(TextualConvention, OctetString):
    description = "Denotes a list of one or more VLAN IDs.\n       VLAN IDs have a value of 0 to 4095.\n       Individual VLAN IDs are included when separated by a comma ','.\n       A range of VLAN IDs is included when separated by '..'.\n       An asterisk indicates untagged data.\n       'rest' selects remaining VLAN IDs.\n       'all' selects all VLAN IDs.\n       Example values:\n         100,110\n         100..110\n         100,110,200..210\n         100,110,200..210,500..510\n       "
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 110)

mibBuilder.exportSymbols("OMNITRON-TC-MIB", OstElpsRequestStates=OstElpsRequestStates, OstCosNameStringOrNone=OstCosNameStringOrNone, OstFrameCount64=OstFrameCount64, ostOmnitronTcMib=ostOmnitronTcMib, OstIpAddr=OstIpAddr, OstCosNameString=OstCosNameString, OstErpsPortState=OstErpsPortState, omnitron=omnitron, OstMhfCreation=OstMhfCreation, OstAccessibiltyType=OstAccessibiltyType, OstEvcNameStringOrNone=OstEvcNameStringOrNone, OstErpsLinkState=OstErpsLinkState, OstErpsRingStatus=OstErpsRingStatus, OstEvcNameString=OstEvcNameString, OstElpsSignalStates=OstElpsSignalStates, OstPortClockType=OstPortClockType, OstProfileNameString=OstProfileNameString, OstPcpPriorityList=OstPcpPriorityList, OstCosL2cpDstAddr=OstCosL2cpDstAddr, OstFingerprintString=OstFingerprintString, OstIpPriorityList=OstIpPriorityList, OstUserNameString=OstUserNameString, OstVlanIdList=OstVlanIdList, OstClassOfService=OstClassOfService, OstModuleSingleIndex=OstModuleSingleIndex, OstProbeNameString=OstProbeNameString, OstFileNameString=OstFileNameString, OstPriority=OstPriority, OstCosTrustType=OstCosTrustType, icAgent=icAgent, OstIpv6Addr=OstIpv6Addr, OstErpsRingStates=OstErpsRingStates, OstMipdMethodOfCreation=OstMipdMethodOfCreation, OstTestStatusType=OstTestStatusType, OstErpsPortType=OstErpsPortType, OstPortSingleIndex=OstPortSingleIndex, OstPortList=OstPortList, OstVlanId=OstVlanId, PYSNMP_MODULE_ID=ostOmnitronTcMib, OstElpsProtectType=OstElpsProtectType, OstErrorString=OstErrorString, OstEgressSchedulingProfileIndexType=OstEgressSchedulingProfileIndexType, OstFrameSizeList=OstFrameSizeList, OstFloatValue=OstFloatValue, OstIndexIntegerNextFree=OstIndexIntegerNextFree, OstClockFreq=OstClockFreq, OstUnsigned64=OstUnsigned64, OstModeType=OstModeType, OstPortNumber=OstPortNumber, OstTestResultType=OstTestResultType, OstEgressQueueIndexType=OstEgressQueueIndexType)
