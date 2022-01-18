#
# PySNMP MIB module MBG-SNMP-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-ROOT-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:51:59 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Counter32, Unsigned32, enterprises, ModuleIdentity, ObjectIdentity, Counter64, NotificationType, Bits, IpAddress, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter32", "Unsigned32", "enterprises", "ModuleIdentity", "ObjectIdentity", "Counter64", "NotificationType", "Bits", "IpAddress", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mbgSnmpRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597))
mbgSnmpRoot.setRevisions(('2012-01-25 07:45', '2011-10-14 06:30',))
if mibBuilder.loadTexts: mbgSnmpRoot.setLastUpdated('201201250745Z')
if mibBuilder.loadTexts: mbgSnmpRoot.setOrganization('Meinberg Radio Clocks GmbH & Co. KG')
class MeinbergSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

mibBuilder.exportSymbols("MBG-SNMP-ROOT-MIB", MeinbergSwitch=MeinbergSwitch, mbgSnmpRoot=mbgSnmpRoot, PYSNMP_MODULE_ID=mbgSnmpRoot)
