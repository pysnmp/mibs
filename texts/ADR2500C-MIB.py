#
# PySNMP MIB module ADR2500C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR2500C-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:26:08 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ObjectIdentity, TimeTicks, MibIdentifier, Integer32, Bits, Counter64, NotificationType, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "Counter64", "NotificationType", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr2500c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 17))
if mibBuilder.loadTexts: adr2500c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr2500c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr2500c.setContactInfo('    ')
if mibBuilder.loadTexts: adr2500c.setDescription('The MIB module specific for ARD2500c equipment')
mibBuilder.exportSymbols("ADR2500C-MIB", PYSNMP_MODULE_ID=adr2500c, adr2500c=adr2500c)
