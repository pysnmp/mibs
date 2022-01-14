#
# PySNMP MIB module PW-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/PW-TC-STD-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:32:30 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Counter32, MibIdentifier, Integer32, IpAddress, NotificationType, ObjectIdentity, mib_2, ModuleIdentity, Gauge32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "ObjectIdentity", "mib-2", "ModuleIdentity", "Gauge32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pwTcStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 188))
pwTcStdMIB.setRevisions(('2009-04-21 00:00',))
if mibBuilder.loadTexts: pwTcStdMIB.setLastUpdated('200904210000Z')
if mibBuilder.loadTexts: pwTcStdMIB.setOrganization('Pseudowire Edge-to-Edge Emulation (PWE3) Working Group')
class PwGroupID(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PwIDType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PwIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class PwIndexOrZeroType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PwOperStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("dormant", 4), ("notPresent", 5), ("lowerLayerDown", 6))

class PwAttachmentIdentifierType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwGenIdType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 254)

class PwCwStatusTC(TextualConvention, Integer32):
    reference = "Martini, et al., 'Pseudowire Setup and Maintenance Using the Label Distribution Protocol', [RFC4447]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalReceivedBit", 4), ("cwPresent", 5), ("cwNotPresent", 6), ("notYetKnown", 7))

class PwStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("servicePwRxFault", 1), ("servicePwTxFault", 2), ("psnPwRxFault", 3), ("psnPwTxFault", 4))

class PwFragSize(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PwFragStatus(TextualConvention, Bits):
    reference = "Malis, A. and M. Townsley, 'Pseudowire Emulation Edge-to- Edge (PWE3) Fragmentation and Reassembly', [RFC4623]."
    status = 'current'
    namedValues = NamedValues(("noFrag", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragEnabled", 4))

class PwCfgIndexOrzero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("PW-TC-STD-MIB", PwFragSize=PwFragSize, PwFragStatus=PwFragStatus, PwAttachmentIdentifierType=PwAttachmentIdentifierType, PwCwStatusTC=PwCwStatusTC, PwGenIdType=PwGenIdType, PwGroupID=PwGroupID, PwIDType=PwIDType, PwCfgIndexOrzero=PwCfgIndexOrzero, PwIndexType=PwIndexType, pwTcStdMIB=pwTcStdMIB, PwStatus=PwStatus, PYSNMP_MODULE_ID=pwTcStdMIB, PwOperStatusTC=PwOperStatusTC, PwIndexOrZeroType=PwIndexOrZeroType)
