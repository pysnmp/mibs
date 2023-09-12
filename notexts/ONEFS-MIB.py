#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:25:26 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, iso, ObjectIdentity, TimeTicks, IpAddress, snmpModules, enterprises, Unsigned32, MibIdentifier, Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "ObjectIdentity", "TimeTicks", "IpAddress", "snmpModules", "enterprises", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
onefs = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124))
if mibBuilder.loadTexts: onefs.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: onefs.setOrganization('COMPANY_NAME')
class TimeTicks64(TextualConvention, Counter64):
    status = 'current'
    subtypeSpec = Counter64.subtypeSpec + ValueRangeConstraint(0, 18446744073709551615)

mibBuilder.exportSymbols("ONEFS-MIB", TimeTicks64=TimeTicks64, onefs=onefs, PYSNMP_MODULE_ID=onefs)
