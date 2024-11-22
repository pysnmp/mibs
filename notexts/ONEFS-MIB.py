#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:59:21 2024
# On host fv-az1245-338 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, NotificationType, ObjectIdentity, TimeTicks, Gauge32, Integer32, ModuleIdentity, Unsigned32, snmpModules, Bits, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "NotificationType", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "ModuleIdentity", "Unsigned32", "snmpModules", "Bits", "IpAddress", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
onefs = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124))
if mibBuilder.loadTexts: onefs.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: onefs.setOrganization('COMPANY_NAME')
class TimeTicks64(TextualConvention, Counter64):
    status = 'current'
    subtypeSpec = Counter64.subtypeSpec + ValueRangeConstraint(0, 18446744073709551615)

mibBuilder.exportSymbols("ONEFS-MIB", PYSNMP_MODULE_ID=onefs, TimeTicks64=TimeTicks64, onefs=onefs)
