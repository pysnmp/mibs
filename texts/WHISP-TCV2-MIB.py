#
# PySNMP MIB module WHISP-TCV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/WHISP-TCV2-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:50:49 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, IpAddress, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Gauge32, NotificationType, ObjectIdentity, Unsigned32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "IpAddress", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Gauge32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
whispModules, = mibBuilder.importSymbols("WHISP-GLOBAL-REG-MIB", "whispModules")
whispTextualConventionsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 3))
if mibBuilder.loadTexts: whispTextualConventionsModule.setLastUpdated('200304170000Z')
if mibBuilder.loadTexts: whispTextualConventionsModule.setOrganization('Motorola')
if mibBuilder.loadTexts: whispTextualConventionsModule.setContactInfo('Canopy Technical Support\n\t\temail: technical-support@canopywireless.com')
if mibBuilder.loadTexts: whispTextualConventionsModule.setDescription('This module contains textual conventions for the Canopy\n                product line.')
class WhispMACAddress(TextualConvention, OctetString):
    description = 'This a WHiSP MAC address or ESN type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class WhispLUID(TextualConvention, Integer32):
    description = 'The 12 LUID (Local Unit Identification) assigned to each Canopy\n                Subscriber Modem (SM).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class EventString(TextualConvention, OctetString):
    description = 'The string used to display event log.'
    status = 'current'
    displayHint = '2048a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

mibBuilder.exportSymbols("WHISP-TCV2-MIB", WhispLUID=WhispLUID, EventString=EventString, whispTextualConventionsModule=whispTextualConventionsModule, PYSNMP_MODULE_ID=whispTextualConventionsModule, WhispMACAddress=WhispMACAddress)
