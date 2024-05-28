#
# PySNMP MIB module AVIAT-TEXTCONVENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-TEXTCONVENTION-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:03:37 2024
# On host fv-az1490-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Integer32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Counter32, Unsigned32, IpAddress, Gauge32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Integer32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "Gauge32", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatTextConventionModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 1))
aviatTextConventionModule.setRevisions(('2017-03-28 23:39', '2015-07-29 08:45', '2015-01-05 09:10', '2014-08-26 23:29', '2014-01-21 01:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aviatTextConventionModule.setRevisionsDescriptions(('Added modulation2048qam and modulation4096qam modulations\n                 for WTM4000.', 'Added RFU side band type textual convention.', 'Added monitoredHotStandby protection type textual convention.', 'Added the textual convention AviatL1LinkAggregationType to\n                 discern whether a layer 1 link aggregation group uses the\n                 Aviat L1LA mode or PLA mode.', 'Initial Version.',))
if mibBuilder.loadTexts: aviatTextConventionModule.setLastUpdated('201703282339Z')
if mibBuilder.loadTexts: aviatTextConventionModule.setOrganization('Aviat Networks')
if mibBuilder.loadTexts: aviatTextConventionModule.setContactInfo('Aviat Networks\n                         Customer Service\n\n                         Postal: 5200 Great America Parkway\n                                 Santa Clara\n                                 California 95054\n                                 United States of America\n\n                         Tel: 408 567 7000\n\n                         E-mail: mibsupport@aviatnet.com')
if mibBuilder.loadTexts: aviatTextConventionModule.setDescription('This module defines the textual conventions used throughout\n                 the DMC Aviat Enterprise MIB. The definitions in this module\n                 are for general purpose use. Textual conventions that are for\n                 specific MIB functionality are defined in the respective MIB\n                 modules.')
class AviatFunctionTimer(TextualConvention, Integer32):
    description = 'This specifies the status of the Function Related\n                         Timer described as follows:\n\n                              0               The function is off\n                             -1               The function is permanently on\n                                              (until it is manually switched\n                                              off or the unit is powered off)\n                             positive value   The number of seconds until the\n                                              function is automatically\n                                              switched Off'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class AviatModulationType(TextualConvention, Integer32):
    description = 'These are the types of modulation techniques.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("modulationNone", 1), ("modulationQpsk", 2), ("modulation16qam", 3), ("modulation32qam", 4), ("modulation64qam", 5), ("modulation128qam", 6), ("modulation256qam", 7), ("modulation512qam", 8), ("modulation1024qam", 9), ("modulation256qamHG", 10), ("modulation512qamHG", 11), ("modulation1024qamHG", 12), ("modulation2048qam", 13), ("modulation4096qam", 14))

class AviatPowerLevel(TextualConvention, Integer32):
    description = 'The power in 0.1dBm steps.'
    status = 'current'
    displayHint = 'd-1'

class AviatDecibel(TextualConvention, Integer32):
    description = 'Ratio in 0.1dB steps.'
    status = 'current'
    displayHint = 'd-1'

class AviatProtectionType(TextualConvention, Integer32):
    description = 'The protection modes for a protected pair.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("nonProtected", 1), ("hotStandby", 2), ("spaceDiversity", 3), ("frequencyDiversity", 4), ("monitoredHotStandby", 5))

class AviatPluginModuleType(TextualConvention, Integer32):
    description = 'These are the types of plugin modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 41, 61, 62, 81, 82))
    namedValues = NamedValues(("pluginModuleNone", 1), ("pluginModuleUnsupported", 2), ("pluginModulePOEx2", 41), ("pluginModulePWR", 61), ("pluginModulePWRAUX", 62), ("pluginModuleRACx1", 81), ("pluginModuleRACx2", 82))

class AviatLoggingProtocolType(TextualConvention, Integer32):
    description = 'These are the types of network protocols for remote\n                         logging.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("protocolUdp", 1), ("protocolTcp", 2), ("protocolTls", 3))

class AviatTimeOfDay(TextualConvention, OctetString):
    description = 'A time in any given day. This is in localtime.\n\n                         field  octets  contents                  range\n                         =====  ======  ========                  =====\n                           1       1    hour                      0..23\n                           2       2    minutes                   0..59\n                           3       3    seconds                   0..60\n                                        (use 60 for leap-second)\n                           4       4    deci-seconds              0..9'
    status = 'current'
    displayHint = '1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class AviatEnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for generic use.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class AviatTableIndexInteger(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a table index. If 0\n                         then it is invalid.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AviatL1LinkAggregationType(TextualConvention, Integer32):
    description = 'The aggregation type for a L1 link aggregation group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("l1la", 1), ("pla", 2))

class AviatRfuSideBandType(TextualConvention, Integer32):
    description = 'The side band type for an RFU.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("highBand", 1), ("lowBand", 2), ("fullBand", 3))

class AviatYangIdentityRef(TextualConvention, OctetString):
    description = 'A reference to a Yang identity, consisting of the namespace and identity id.\n             These are represented as a string delimited with a colon, \n             i.e. namespace:identity'
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("AVIAT-TEXTCONVENTION-MIB", PYSNMP_MODULE_ID=aviatTextConventionModule, AviatPowerLevel=AviatPowerLevel, AviatRfuSideBandType=AviatRfuSideBandType, AviatDecibel=AviatDecibel, AviatTimeOfDay=AviatTimeOfDay, aviatTextConventionModule=aviatTextConventionModule, AviatFunctionTimer=AviatFunctionTimer, AviatYangIdentityRef=AviatYangIdentityRef, AviatPluginModuleType=AviatPluginModuleType, AviatEnabledStatus=AviatEnabledStatus, AviatTableIndexInteger=AviatTableIndexInteger, AviatProtectionType=AviatProtectionType, AviatLoggingProtocolType=AviatLoggingProtocolType, AviatL1LinkAggregationType=AviatL1LinkAggregationType, AviatModulationType=AviatModulationType)
