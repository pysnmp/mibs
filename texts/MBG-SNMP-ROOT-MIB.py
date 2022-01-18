#
# PySNMP MIB module MBG-SNMP-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-ROOT-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 13:46:56 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, iso, Integer32, Bits, NotificationType, enterprises, Counter32, Gauge32, Unsigned32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "iso", "Integer32", "Bits", "NotificationType", "enterprises", "Counter32", "Gauge32", "Unsigned32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mbgSnmpRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597))
mbgSnmpRoot.setRevisions(('2012-01-25 07:45', '2011-10-14 06:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mbgSnmpRoot.setRevisionsDescriptions((' Rev 1.01  25 January 2012 7:45 UTC Philipp Rahns\n          Changed MIB module name', ' Rev 1.00  14 October 2011 6:30 UTC Philipp Rahns\n          Initial revision',))
if mibBuilder.loadTexts: mbgSnmpRoot.setLastUpdated('201201250745Z')
if mibBuilder.loadTexts: mbgSnmpRoot.setOrganization('Meinberg Radio Clocks GmbH & Co. KG')
if mibBuilder.loadTexts: mbgSnmpRoot.setContactInfo('postal:   Meinberg Funkuhren\n                    Lange Wand 9\n                    31812 Bad Pyrmont\n                    Germany\n\n          email:    info@meinberg.de\n            web:    http://www.meinberg.de\n            tel:    +49 (0) 52 81 / 93 09 - 0\n            fax:    +49 (0) 52 81 / 93 09 - 30')
if mibBuilder.loadTexts: mbgSnmpRoot.setDescription(' Meinberg SNMP Management Information Root Base ')
class MeinbergSwitch(TextualConvention, Integer32):
    description = 'indicating whether something is actived or not => like a switch'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

mibBuilder.exportSymbols("MBG-SNMP-ROOT-MIB", PYSNMP_MODULE_ID=mbgSnmpRoot, MeinbergSwitch=MeinbergSwitch, mbgSnmpRoot=mbgSnmpRoot)
