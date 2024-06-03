#
# PySNMP MIB module MBG-SNMP-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-ROOT-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 10:59:49 2024
# On host fv-az1986-135 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, ModuleIdentity, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, TimeTicks, Gauge32, NotificationType, IpAddress, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "ModuleIdentity", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "TimeTicks", "Gauge32", "NotificationType", "IpAddress", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mbgSnmpRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597))
mbgSnmpRoot.setRevisions(('2012-01-25 07:45', '2011-10-14 06:30',))
if mibBuilder.loadTexts: mbgSnmpRoot.setLastUpdated('201201250745Z')
if mibBuilder.loadTexts: mbgSnmpRoot.setOrganization('Meinberg Radio Clocks GmbH & Co. KG')
class MeinbergSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

mibBuilder.exportSymbols("MBG-SNMP-ROOT-MIB", MeinbergSwitch=MeinbergSwitch, PYSNMP_MODULE_ID=mbgSnmpRoot, mbgSnmpRoot=mbgSnmpRoot)
