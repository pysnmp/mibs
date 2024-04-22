#
# PySNMP MIB module AVIAT-TEXTCONVENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-TEXTCONVENTION-MIB
# Produced by pysmi-1.1.12 at Mon Apr 22 02:09:50 2024
# On host fv-az569-486 platform Linux version 6.5.0-1018-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, iso, Integer32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, MibIdentifier, Bits, Counter64, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "iso", "Integer32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "ObjectIdentity")
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

mibBuilder.exportSymbols("AVIAT-TEXTCONVENTION-MIB", aviatTextConventionModule=aviatTextConventionModule, AviatPowerLevel=AviatPowerLevel, AviatTableIndexInteger=AviatTableIndexInteger, AviatDecibel=AviatDecibel, AviatFunctionTimer=AviatFunctionTimer, PYSNMP_MODULE_ID=aviatTextConventionModule, AviatPluginModuleType=AviatPluginModuleType, AviatYangIdentityRef=AviatYangIdentityRef, AviatL1LinkAggregationType=AviatL1LinkAggregationType, AviatModulationType=AviatModulationType, AviatTimeOfDay=AviatTimeOfDay, AviatEnabledStatus=AviatEnabledStatus, AviatLoggingProtocolType=AviatLoggingProtocolType, AviatRfuSideBandType=AviatRfuSideBandType, AviatProtectionType=AviatProtectionType)
