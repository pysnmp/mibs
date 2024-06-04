#
# PySNMP MIB module TAIT-INFRA93-94SERIES-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-TC-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 13:38:14 2024
# On host fv-az573-215 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Unsigned32, Counter32, MibIdentifier, NotificationType, Gauge32, ObjectIdentity, TimeTicks, Integer32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
infra93_94MibModule, = mibBuilder.importSymbols("TAIT-INFRA93-94SERIES-COMMON-MIB", "infra93-94MibModule")
infra93_94TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1)).setLabel("infra93-94TC")
infra93_94TC.setRevisions(('2018-08-31 00:00', '2018-05-22 00:26', '2017-11-28 00:00', '2017-07-28 00:00', '2016-03-21 00:00', '2015-05-15 12:00', '2014-10-30 15:00', '2014-01-14 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: infra93_94TC.setRevisionsDescriptions(('Version 1.13.00 - Added generic textual conventions for gate state property (open/closed) and an option property that can be enabled/disabled', 'Version 1.12.00 - Removed dmr specific textual conventions textual convention', 'Version 1.11.00 - The textual convention for ChannelGroupStatus cleaned up', 'Version 1.10.00 - The textual conventions for ChannelGroupStatus, Milliseconds, TimingControlType added\n                                   - The textual conventions for ChannelGroupStatus updated to include single-base-station status and description', 'Version 1.09.00 - Added Condition, VoltageV, CurrentmA from TB9400 specific textual conventions', 'Version 1.08.00 - Modified range of alarmState to include unavailable (0)', 'Version 1.01.03 - Description text reviewed', 'Version 1.01.02',))
if mibBuilder.loadTexts: infra93_94TC.setLastUpdated('201808310000Z')
if mibBuilder.loadTexts: infra93_94TC.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: infra93_94TC.setContactInfo('Tait Communications\n                   245 Wooldridge Road\n                   PO Box 1645\n                   Christchurch\n                   New Zealand\n\n           phone:  +64 3358 3399\n           email:  support@taitradio.com')
if mibBuilder.loadTexts: infra93_94TC.setDescription('Textual conventions used in the Tait-infrastructure-93-94-series MIBs')
class BaseStationMode(TextualConvention, Integer32):
    description = 'Base Station Run Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("offline", 0), ("online", 1), ("unknown", 2))

class Condition(TextualConvention, Integer32):
    description = 'Condition'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bad", 0), ("good", 1), ("notFitted", 2))

class CurrentmA(TextualConvention, Unsigned32):
    description = 'The increment size is 1 mA. Displayed unit is A'
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AlarmState(TextualConvention, Integer32):
    description = 'Base Station Alarm status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unavailable", 0), ("cleared", 1), ("raised", 2), ("disabled", 3))

class FrequencyHz(TextualConvention, Unsigned32):
    description = 'The increment size is 1 Hz. Displayed unit is MHz'
    status = 'current'
    displayHint = 'd-6'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PowerW(TextualConvention, Unsigned32):
    description = 'The increment size is 1 W'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TransmitterStatus(TextualConvention, Integer32):
    description = 'Base Station Transmitter status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("unconfigured", 1), ("untuned", 2), ("idle", 3), ("transmitting", 4), ("calibrating", 5), ("fault", 6))

class VoltageV(TextualConvention, Integer32):
    description = 'The increment size is 0.01 V. Displayed unit is V'
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class Milliseconds(TextualConvention, Unsigned32):
    description = 'The increment size is 1 ms'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class ChannelGroupStatus(TextualConvention, Integer32):
    description = 'It describes the role that base-station is playing in a channelgroup. The possible values are -\n                   no license(0): The base station does not have a feature license permitting it to be part of a channel group.\n                   offline(1): The base station is offline. It is not operational.\n                   Isolated(2): The base station is operating as best-efforts repeater. This type of voting should not occur in trunked networks.\n                   satellite(3): The base station has acknowledged another channel group member as the central voter. It plays a supporting role to the central voter.\n                   central voter(4): The base station is operating as the central voter for the channel group. All incoming voice streams are sent to it for voting. Only one channel group member can be the central voter at any one time.\n                   single base station(5): The base station is operating as a single basestation with channelgroup disabled.\n                   backup central(6): The base station is capable of operating as master but is currently a satellite to a better master'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noLicense", 0), ("offline", 1), ("isolated", 2), ("satellite", 3), ("centralVoter", 4), ("singleBaseStation", 5), ("backupCentral", 6))

class TimingControlType(TextualConvention, Integer32):
    description = 'TimingControlType'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("selfRegulating", 1))

class GateState(TextualConvention, Integer32):
    description = 'The state of a gate'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("closed", 0), ("open", 1))

class OptionState(TextualConvention, Integer32):
    description = 'The state of an option'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-TC-MIB", GateState=GateState, ChannelGroupStatus=ChannelGroupStatus, infra93_94TC=infra93_94TC, Condition=Condition, FrequencyHz=FrequencyHz, TransmitterStatus=TransmitterStatus, PowerW=PowerW, CurrentmA=CurrentmA, AlarmState=AlarmState, Milliseconds=Milliseconds, TimingControlType=TimingControlType, OptionState=OptionState, PYSNMP_MODULE_ID=infra93_94TC, BaseStationMode=BaseStationMode, VoltageV=VoltageV)
