#
# PySNMP MIB module ADR155C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR155C-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:18:10 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, ModuleIdentity, Unsigned32, TimeTicks, MibIdentifier, Gauge32, NotificationType, Counter64, iso, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "TimeTicks", "MibIdentifier", "Gauge32", "NotificationType", "Counter64", "iso", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr155c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 12))
if mibBuilder.loadTexts: adr155c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr155c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
mibBuilder.exportSymbols("ADR155C-MIB", PYSNMP_MODULE_ID=adr155c, adr155c=adr155c)
