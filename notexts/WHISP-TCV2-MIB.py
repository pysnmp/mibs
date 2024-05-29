#
# PySNMP MIB module WHISP-TCV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/WHISP-TCV2-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:52:11 2024
# On host fv-az1206-254 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Bits, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, iso, TimeTicks, Counter32, Counter64, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Bits", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "iso", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
whispModules, = mibBuilder.importSymbols("WHISP-GLOBAL-REG-MIB", "whispModules")
whispTextualConventionsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 3))
if mibBuilder.loadTexts: whispTextualConventionsModule.setLastUpdated('200304170000Z')
if mibBuilder.loadTexts: whispTextualConventionsModule.setOrganization('Motorola')
class WhispMACAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class WhispLUID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class EventString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2048a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

mibBuilder.exportSymbols("WHISP-TCV2-MIB", PYSNMP_MODULE_ID=whispTextualConventionsModule, WhispMACAddress=WhispMACAddress, whispTextualConventionsModule=whispTextualConventionsModule, EventString=EventString, WhispLUID=WhispLUID)
