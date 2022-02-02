#
# PySNMP MIB module WHISP-TCV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/WHISP-TCV2-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 19:24:17 2022
# On host fv-az33-564 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, Integer32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, iso, Gauge32, Counter64, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Integer32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "iso", "Gauge32", "Counter64", "ModuleIdentity", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("WHISP-TCV2-MIB", WhispMACAddress=WhispMACAddress, EventString=EventString, whispTextualConventionsModule=whispTextualConventionsModule, WhispLUID=WhispLUID, PYSNMP_MODULE_ID=whispTextualConventionsModule)
