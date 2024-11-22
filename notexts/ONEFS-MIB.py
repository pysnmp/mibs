#
# PySNMP MIB module ONEFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/emc/ONEFS-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:57:19 2024
# On host fv-az1205-935 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, IpAddress, Counter64, Unsigned32, ModuleIdentity, Integer32, ObjectIdentity, iso, Counter32, Gauge32, enterprises, MibIdentifier, NotificationType, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Counter64", "Unsigned32", "ModuleIdentity", "Integer32", "ObjectIdentity", "iso", "Counter32", "Gauge32", "enterprises", "MibIdentifier", "NotificationType", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
onefs = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124))
if mibBuilder.loadTexts: onefs.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: onefs.setOrganization('COMPANY_NAME')
class TimeTicks64(TextualConvention, Counter64):
    status = 'current'
    subtypeSpec = Counter64.subtypeSpec + ValueRangeConstraint(0, 18446744073709551615)

mibBuilder.exportSymbols("ONEFS-MIB", TimeTicks64=TimeTicks64, PYSNMP_MODULE_ID=onefs, onefs=onefs)
