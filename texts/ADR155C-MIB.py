#
# PySNMP MIB module ADR155C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR155C-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:05:33 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, MibIdentifier, TimeTicks, NotificationType, Unsigned32, ModuleIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr155c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 12))
if mibBuilder.loadTexts: adr155c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr155c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr155c.setContactInfo('    ')
if mibBuilder.loadTexts: adr155c.setDescription('The MIB module specific for ARD155c equipment')
mibBuilder.exportSymbols("ADR155C-MIB", PYSNMP_MODULE_ID=adr155c, adr155c=adr155c)
