#
# PySNMP MIB module ADR2500C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR2500C-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 19:49:59 2021
# On host fv-az83-233 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, MibIdentifier, Bits, ModuleIdentity, ObjectIdentity, IpAddress, Counter32, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "MibIdentifier", "Bits", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter32", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr2500c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 17))
if mibBuilder.loadTexts: adr2500c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr2500c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
mibBuilder.exportSymbols("ADR2500C-MIB", adr2500c=adr2500c, PYSNMP_MODULE_ID=adr2500c)
