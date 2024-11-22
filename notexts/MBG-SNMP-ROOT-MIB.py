#
# PySNMP MIB module MBG-SNMP-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-ROOT-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:58:05 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, IpAddress, Gauge32, Counter64, TimeTicks, Unsigned32, Bits, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "Unsigned32", "Bits", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mbgSnmpRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597))
mbgSnmpRoot.setRevisions(('2012-01-25 07:45', '2011-10-14 06:30',))
if mibBuilder.loadTexts: mbgSnmpRoot.setLastUpdated('201201250745Z')
if mibBuilder.loadTexts: mbgSnmpRoot.setOrganization('Meinberg Radio Clocks GmbH & Co. KG')
class MeinbergSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

mibBuilder.exportSymbols("MBG-SNMP-ROOT-MIB", mbgSnmpRoot=mbgSnmpRoot, PYSNMP_MODULE_ID=mbgSnmpRoot, MeinbergSwitch=MeinbergSwitch)
