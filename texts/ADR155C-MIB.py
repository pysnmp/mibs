#
# PySNMP MIB module ADR155C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR155C-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 14:49:09 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter64, NotificationType, ModuleIdentity, Counter32, ObjectIdentity, Bits, Integer32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "Integer32", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr155c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 12))
if mibBuilder.loadTexts: adr155c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr155c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr155c.setContactInfo('    ')
if mibBuilder.loadTexts: adr155c.setDescription('The MIB module specific for ARD155c equipment')
mibBuilder.exportSymbols("ADR155C-MIB", PYSNMP_MODULE_ID=adr155c, adr155c=adr155c)
