#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 15:45:58 2023
# On host fv-az551-95 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Integer32, IpAddress, ModuleIdentity, enterprises, Unsigned32, TimeTicks, Bits, NotificationType, snmpModules, Counter32, Gauge32, MibIdentifier, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "IpAddress", "ModuleIdentity", "enterprises", "Unsigned32", "TimeTicks", "Bits", "NotificationType", "snmpModules", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
onefs = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124))
if mibBuilder.loadTexts: onefs.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: onefs.setOrganization('COMPANY_NAME')
class TimeTicks64(TextualConvention, Counter64):
    status = 'current'
    subtypeSpec = Counter64.subtypeSpec + ValueRangeConstraint(0, 18446744073709551615)

mibBuilder.exportSymbols("ONEFS-MIB", onefs=onefs, PYSNMP_MODULE_ID=onefs, TimeTicks64=TimeTicks64)
