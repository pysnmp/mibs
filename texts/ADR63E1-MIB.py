#
# PySNMP MIB module ADR63E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR63E1-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:47:29 2021
# On host fv-az77-509 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Integer32, TimeTicks, Gauge32, IpAddress, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Integer32", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adr63e1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 18))
if mibBuilder.loadTexts: adr63e1.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr63e1.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr63e1.setContactInfo('    ')
if mibBuilder.loadTexts: adr63e1.setDescription('The MIB module specific for ADR63E1 equipment')
mibBuilder.exportSymbols("ADR63E1-MIB", adr63e1=adr63e1, PYSNMP_MODULE_ID=adr63e1)
