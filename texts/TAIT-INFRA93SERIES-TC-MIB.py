#
# PySNMP MIB module TAIT-INFRA93SERIES-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93SERIES-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 23:32:56 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Integer32, Counter64, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Integer32", "Counter64", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
infra93_94TC, = mibBuilder.importSymbols("TAIT-INFRA93-94SERIES-TC-MIB", "infra93-94TC")
infra93TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1, 1))
infra93TC.setRevisions(('2019-05-29 00:26', '2018-05-22 00:26', '2017-07-28 00:00', '2016-11-18 00:00', '2016-07-01 00:00', '2014-10-30 15:00', '2014-04-14 00:00', '2014-01-26 00:00', '2014-01-14 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: infra93TC.setRevisionsDescriptions(('1.23.00 - Minor text edit', '1.16.00 - moved dmr specific textual conventions from common to dmr mib', '1.15.00 - added TransmitterSyncStatus and ReceiverSyncStatus', '1.14.00 - added MPT Fallback Node Status', '1.13.00 - Updated DCS formatting description', '1.05.01 - Description text reviewed', '1.05.00 - Added values for use during coverage testing', '1.04.00 - Moved textual convention module identity OID to start at 1', '1.03.02 - Initial version prior to change log entries',))
if mibBuilder.loadTexts: infra93TC.setLastUpdated('201905290026Z')
if mibBuilder.loadTexts: infra93TC.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: infra93TC.setContactInfo('Tait Communications\n                   245 Wooldridge Road\n                   PO Box 1645\n                   Christchurch\n                   New Zealand\n\n           phone:  +64 3358 3399\n           email:  support@taitradio.com')
if mibBuilder.loadTexts: infra93TC.setDescription('Textual conventions to be used in the Tait-infrastructure-93-series MIBs')
class Ratio(TextualConvention, Integer32):
    description = 'The increment size is 0.1 1. Displayed unit is N/A'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-256, 255)

class LeveldBm(TextualConvention, Integer32):
    description = 'The increment size is 0.01 dBm. Displayed unit is dBm'
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class SINADLevel(TextualConvention, Unsigned32):
    description = 'The increment size is 1 dB.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class Temperature(TextualConvention, Integer32):
    description = 'The increment size is 1 degree C'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class FrequencydHz(TextualConvention, Unsigned32):
    description = 'The increment size is 0.1 Hz. Displayed unit is Hz'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class DcsCode(TextualConvention, Unsigned32):
    description = 'DCS code. Displayed value should be octal.'
    status = 'current'
    displayHint = 'o'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubAudibleType(TextualConvention, Integer32):
    description = 'Type of sub-audible signaling'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("ctcss", 1), ("dcs", 2))

class TxFrequencyResponse(TextualConvention, Integer32):
    description = 'Type of Tx frequency response'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pre-emph-speech", 1), ("flat-speech", 2))

class RxFrequencyResponse(TextualConvention, Integer32):
    description = 'Type of Rx frequency response'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("de-emph-speech", 1))

class OperationalMode(TextualConvention, Integer32):
    description = 'Base Station operational mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("analogConventional", 1), ("dmrConventional", 2), ("dmrTrunking", 3), ("mptTrunking", 4))

class MPTControlProtocolStatus(TextualConvention, Integer32):
    description = 'MPT Control protocol states'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unconnected", 0), ("idle", 1), ("control", 2), ("traffic", 3), ("conventional", 4))

class FallbackNodeStatus(TextualConvention, Integer32):
    description = 'Fallback status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("settling", 3), ("disabled", 4))

class ColourCode(TextualConvention, Unsigned32):
    description = 'Colour Code'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TransmitterSyncStatus(TextualConvention, Integer32):
    description = 'Transmitter Synchronisation status on TB9300'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("no-license", 0), ("non-simulcast-operation", 1), ("frequency-reference-bad-or-absent", 2), ("never-had-1pps", 3), ("never-had-ntp", 4), ("missing-1pps-or-ntp", 5), ("synchronized", 6), ("non-channelgroup-operation", 7))

class ReceiverSyncStatus(TextualConvention, Integer32):
    description = 'Receiver Synchronisation status on TB9300'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("no-license", 0), ("non-channelgroup-operation", 1), ("synchronized", 2), ("never-had-1pps", 3), ("never-had-ntp", 4), ("missing-1pps-or-ntp", 5))

class ControlProtocolStatus(TextualConvention, Integer32):
    description = 'Control protocol states'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unconnected", 0), ("deprecatedUnconnected", 1), ("standby", 2), ("dmrAligned", 3), ("dmrOffset", 4), ("dmr2SlotData", 5), ("dmrHibernate", 6), ("analogue", 7), ("testMode", 8), ("dmrTier2Aligned", 9))

class LogicalChannelState(TextualConvention, Integer32):
    description = 'Network Connection Logical channel state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("inactive", 0), ("idle", 1), ("traffic", 2), ("control", 3), ("test", 4), ("poll", 5), ("invalid", 255))

class StandaloneNodeStatus(TextualConvention, Integer32):
    description = 'Fallback node status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6))
    namedValues = NamedValues(("offline", 0), ("standby", 1), ("active", 2), ("disabled", 4), ("running", 5), ("master", 6))

mibBuilder.exportSymbols("TAIT-INFRA93SERIES-TC-MIB", FallbackNodeStatus=FallbackNodeStatus, TxFrequencyResponse=TxFrequencyResponse, LogicalChannelState=LogicalChannelState, MPTControlProtocolStatus=MPTControlProtocolStatus, SINADLevel=SINADLevel, infra93TC=infra93TC, ReceiverSyncStatus=ReceiverSyncStatus, PYSNMP_MODULE_ID=infra93TC, SubAudibleType=SubAudibleType, Ratio=Ratio, RxFrequencyResponse=RxFrequencyResponse, ColourCode=ColourCode, ControlProtocolStatus=ControlProtocolStatus, Temperature=Temperature, StandaloneNodeStatus=StandaloneNodeStatus, LeveldBm=LeveldBm, FrequencydHz=FrequencydHz, DcsCode=DcsCode, OperationalMode=OperationalMode, TransmitterSyncStatus=TransmitterSyncStatus)
