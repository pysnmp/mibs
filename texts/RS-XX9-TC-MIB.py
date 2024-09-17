#
# PySNMP MIB module RS-XX9-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/RS-XX9-TC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:02:04 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
rsXx9MibModule, = mibBuilder.importSymbols("RS-XX9-SMI-MIB", "rsXx9MibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, IpAddress, ModuleIdentity, iso, NotificationType, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsXx9TcMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 1, 216, 1))
rsXx9TcMibModule.setRevisions(('2016-01-22 14:00', '2015-09-24 08:00', '2015-05-21 12:00', '2013-02-15 11:11', '2012-05-09 10:00', '2011-08-16 08:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsXx9TcMibModule.setRevisionsDescriptions(('add backupTx to Xx9RedundancyMode\n                add phu903 to Xx9AmplifierTyoe', 'add hdRadio to Xx9ModulationMode', 'add pmu905 to Xx9AmplifierType', 'modulation modes DAB, DTMB, FM\n                amplifier type PHR901', 'Initial revision', 'Preliminary version.',))
if mibBuilder.loadTexts: rsXx9TcMibModule.setLastUpdated('201601221400Z')
if mibBuilder.loadTexts: rsXx9TcMibModule.setOrganization('Rohde&Schwarz GmbH & Co. KG')
if mibBuilder.loadTexts: rsXx9TcMibModule.setContactInfo('Rohde & Schwarz GmbH & Co. KG\n                Broadcasting Division\n                \n                Muehldorfstrasse 15\n                81671 Munich\n                Germany\n                \n                customersupport@rohde-schwarz.com')
if mibBuilder.loadTexts: rsXx9TcMibModule.setDescription('This MIB defines textual conventions used in all XX9 MIBs.\n                \n                The following MIBs are related to this:\n                - RS-COMMON-MIB         - mandatory for this MIB.\n                - RS-XX9-SMI-MIB        - mandatory for this MIB.')
class EnableOption(TextualConvention, Integer32):
    description = 'Enabling of a device option.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unconfigured", 1), ("disabled", 2), ("enabled", 3))

class IndexAB(TextualConvention, Integer32):
    description = 'This is used for distinguishing module A (exciterA, outputstageA)\n                or B (exciterB, outputstageB) in tables.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("a", 1), ("b", 2))

class IndexProgram(TextualConvention, Integer32):
    description = 'This is used for N+1 systems to indicate a program sent out (logical view).\n                ProgramRes(1000) is the reserve program, program1(1) to program8(8) are the main programs.\n                In difference to the physical view, programRes(1000) has no special parameters available.\n                Furthermore it has no priority.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 1000))
    namedValues = NamedValues(("program1", 1), ("program2", 2), ("program3", 3), ("program4", 4), ("program5", 5), ("program6", 6), ("program7", 7), ("program8", 8), ("programRes", 1000))

class IndexTransmitter(TextualConvention, Integer32):
    description = 'This is used for N+1 systems to indicate a transmitter (physical view).\n                TransmitterB(1000) is the reserve transmitter,\n                transmitterA1(1) to transmitterA8(8) are the main transmitters.\n                In difference to the logical view,\n                transmitterB(1000) has special parameters available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 1000))
    namedValues = NamedValues(("transmitterA1", 1), ("transmitterA2", 2), ("transmitterA3", 3), ("transmitterA4", 4), ("transmitterA5", 5), ("transmitterA6", 6), ("transmitterA7", 7), ("transmitterA8", 8), ("transmitterB", 1000))

class NotificationClass(TextualConvention, Integer32):
    description = "This is a classification of the highest impact a notification may have\n                (the actual impact depends on the notificattion state)\n                info(3) - are notifications which only inform about changes, e.g. 'local/remote'\n                  or 'reboot of the control unit'. They don't affect the transmission.\n                warning(2) - are minor problems which do not influence transmission itself,\n                  but may cause a bigger problem when no action is taken, e.g.\n                  'RF Loop Program'. Warnings may appear and disappear without the need\n                  of acknowledgment.\n                fault(1) - have a direct impact on the transmission, e.g.\n                  'failure power supply'. Faults never disappear without acknowledgment.\n                \n                E.g. the commonNtpSync notification from the RS-XX9-COMMON-MIB is classified as warning(2).\n                If the state of this notification is fault(3) it is actually a warning,\n                otherwise the warning is cancelled."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fault", 1), ("warning", 2), ("info", 3))

class NotificationMask(TextualConvention, Integer32):
    description = 'Enables / Disables a notification.\n                enable(1)  --> The notification will be sent in case the NotificationState changes\n                disable(2) --> The notification will not be sent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class NotificationPriority(TextualConvention, Unsigned32):
    description = 'The priority of a notification.\n                Users can freely set this value in range 0..255.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class NotificationState(TextualConvention, Integer32):
    description = 'The current state of a notification entity:\n                off(2)     --> entity is not in service or inactive\n                fault(3)   --> entity is faulty\n                warning(4) --> entity is in a warning state\n                ok(5)      --> entity is on resp. ok'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 1), ("off", 2), ("fault", 3), ("warning", 4), ("ok", 5))

class SwitchOnOff(TextualConvention, Integer32):
    description = 'This is for all on/off-switches.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class Trigger(TextualConvention, Integer32):
    description = 'Trigger for starting a certain action.\n                idle(1)    --> ready, do nothing\n                trigger(2) --> do now\n                \n                A GET will always return idle(1). \n                A SET idle(1) will return NO_ERROR without doing anything.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("trigger", 2))

class Xx9AmplifierType(TextualConvention, Integer32):
    description = 'Type of amplifiers for a transmitter.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 21))
    namedValues = NamedValues(("unconfigured", 1), ("phu901", 2), ("pmu901", 3), ("phu902", 4), ("phv902", 5), ("pmv901", 6), ("pmu905", 7), ("phu903", 8), ("phr901", 21))

class Xx9ModulationMode(TextualConvention, Integer32):
    description = 'Modulation mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 22, 23))
    namedValues = NamedValues(("unconfigured", 1), ("none", 2), ("dvbT2", 3), ("dvbT", 4), ("isdbT", 5), ("atsc", 6), ("atv", 7), ("dab", 8), ("dtmb", 9), ("fm", 21), ("hdRadioHybrid", 22), ("hdRadioFullDigital", 23))

class Xx9RedundancyMode(TextualConvention, Integer32):
    description = 'Redundancy mode of a single transmitter.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 1), ("singleDrive", 2), ("dualDrive", 3), ("backupDrive", 4), ("activePa", 5), ("backupTx", 6))

class Xx9SystemType(TextualConvention, Integer32):
    description = 'transmitter(2) - single transmitter\n                multiTx(3)     - multi Tx system with several transmitters\n                nPlus1(4)      - several transmitters in N+1 reserve configuration'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unconfigured", 1), ("transmitter", 2), ("multiTx", 3), ("nPlus1", 4))

mibBuilder.exportSymbols("RS-XX9-TC-MIB", Trigger=Trigger, NotificationPriority=NotificationPriority, NotificationState=NotificationState, PYSNMP_MODULE_ID=rsXx9TcMibModule, IndexTransmitter=IndexTransmitter, NotificationMask=NotificationMask, Xx9RedundancyMode=Xx9RedundancyMode, SwitchOnOff=SwitchOnOff, Xx9AmplifierType=Xx9AmplifierType, Xx9SystemType=Xx9SystemType, EnableOption=EnableOption, Xx9ModulationMode=Xx9ModulationMode, IndexAB=IndexAB, rsXx9TcMibModule=rsXx9TcMibModule, IndexProgram=IndexProgram, NotificationClass=NotificationClass)
