#
# PySNMP MIB module AVIAT-TEXTCONVENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-TEXTCONVENTION-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:07 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, iso, TimeTicks, Bits, Counter32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "iso", "TimeTicks", "Bits", "Counter32", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatTextConventionModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 1))
aviatTextConventionModule.setRevisions(('2017-03-28 23:39', '2015-07-29 08:45', '2015-01-05 09:10', '2014-08-26 23:29', '2014-01-21 01:57',))
if mibBuilder.loadTexts: aviatTextConventionModule.setLastUpdated('201703282339Z')
if mibBuilder.loadTexts: aviatTextConventionModule.setOrganization('Aviat Networks')
class AviatFunctionTimer(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class AviatModulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("modulationNone", 1), ("modulationQpsk", 2), ("modulation16qam", 3), ("modulation32qam", 4), ("modulation64qam", 5), ("modulation128qam", 6), ("modulation256qam", 7), ("modulation512qam", 8), ("modulation1024qam", 9), ("modulation256qamHG", 10), ("modulation512qamHG", 11), ("modulation1024qamHG", 12), ("modulation2048qam", 13), ("modulation4096qam", 14))

class AviatPowerLevel(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class AviatDecibel(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class AviatProtectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("nonProtected", 1), ("hotStandby", 2), ("spaceDiversity", 3), ("frequencyDiversity", 4), ("monitoredHotStandby", 5))

class AviatPluginModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 41, 61, 62, 81, 82))
    namedValues = NamedValues(("pluginModuleNone", 1), ("pluginModuleUnsupported", 2), ("pluginModulePOEx2", 41), ("pluginModulePWR", 61), ("pluginModulePWRAUX", 62), ("pluginModuleRACx1", 81), ("pluginModuleRACx2", 82))

class AviatLoggingProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("protocolUdp", 1), ("protocolTcp", 2), ("protocolTls", 3))

class AviatTimeOfDay(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class AviatEnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class AviatTableIndexInteger(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AviatL1LinkAggregationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("l1la", 1), ("pla", 2))

class AviatRfuSideBandType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("highBand", 1), ("lowBand", 2), ("fullBand", 3))

class AviatYangIdentityRef(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("AVIAT-TEXTCONVENTION-MIB", AviatLoggingProtocolType=AviatLoggingProtocolType, AviatFunctionTimer=AviatFunctionTimer, AviatDecibel=AviatDecibel, PYSNMP_MODULE_ID=aviatTextConventionModule, AviatYangIdentityRef=AviatYangIdentityRef, AviatPluginModuleType=AviatPluginModuleType, aviatTextConventionModule=aviatTextConventionModule, AviatRfuSideBandType=AviatRfuSideBandType, AviatL1LinkAggregationType=AviatL1LinkAggregationType, AviatTimeOfDay=AviatTimeOfDay, AviatModulationType=AviatModulationType, AviatEnabledStatus=AviatEnabledStatus, AviatProtectionType=AviatProtectionType, AviatPowerLevel=AviatPowerLevel, AviatTableIndexInteger=AviatTableIndexInteger)
