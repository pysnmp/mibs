#
# PySNMP MIB module MBG-SNMP-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-ROOT-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:11:28 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, IpAddress, enterprises, ModuleIdentity, Counter32, Unsigned32, Gauge32, Bits, MibIdentifier, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "IpAddress", "enterprises", "ModuleIdentity", "Counter32", "Unsigned32", "Gauge32", "Bits", "MibIdentifier", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("MBG-SNMP-ROOT-MIB", MeinbergSwitch=MeinbergSwitch, mbgSnmpRoot=mbgSnmpRoot, PYSNMP_MODULE_ID=mbgSnmpRoot)
