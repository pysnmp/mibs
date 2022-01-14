#
# PySNMP MIB module ADR155C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR155C-MIB
# Produced by pysmi-1.1.8 at Fri Jan 14 00:06:58 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, Gauge32, ObjectIdentity, iso, Counter32, ModuleIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "ObjectIdentity", "iso", "Counter32", "ModuleIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adr155c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 12))
if mibBuilder.loadTexts: adr155c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr155c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr155c.setContactInfo('    ')
if mibBuilder.loadTexts: adr155c.setDescription('The MIB module specific for ARD155c equipment')
mibBuilder.exportSymbols("ADR155C-MIB", adr155c=adr155c, PYSNMP_MODULE_ID=adr155c)
