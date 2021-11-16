#
# PySNMP MIB module ADR63E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR63E1-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:47:27 2021
# On host fv-az77-509 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, Integer32, Counter64, Gauge32, IpAddress, Bits, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Integer32", "Counter64", "Gauge32", "IpAddress", "Bits", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adr63e1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 18))
if mibBuilder.loadTexts: adr63e1.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr63e1.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
mibBuilder.exportSymbols("ADR63E1-MIB", PYSNMP_MODULE_ID=adr63e1, adr63e1=adr63e1)
