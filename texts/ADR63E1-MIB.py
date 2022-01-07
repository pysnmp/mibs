#
# PySNMP MIB module ADR63E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR63E1-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:37:30 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Gauge32, ModuleIdentity, NotificationType, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "ModuleIdentity", "NotificationType", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr63e1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 18))
if mibBuilder.loadTexts: adr63e1.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr63e1.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr63e1.setContactInfo('    ')
if mibBuilder.loadTexts: adr63e1.setDescription('The MIB module specific for ADR63E1 equipment')
mibBuilder.exportSymbols("ADR63E1-MIB", adr63e1=adr63e1, PYSNMP_MODULE_ID=adr63e1)
