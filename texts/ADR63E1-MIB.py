#
# PySNMP MIB module ADR63E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR63E1-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:48:14 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, IpAddress, NotificationType, TimeTicks, Counter64, MibIdentifier, Counter32, Integer32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "IpAddress", "NotificationType", "TimeTicks", "Counter64", "MibIdentifier", "Counter32", "Integer32", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adr63e1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 18))
if mibBuilder.loadTexts: adr63e1.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr63e1.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr63e1.setContactInfo('    ')
if mibBuilder.loadTexts: adr63e1.setDescription('The MIB module specific for ADR63E1 equipment')
mibBuilder.exportSymbols("ADR63E1-MIB", adr63e1=adr63e1, PYSNMP_MODULE_ID=adr63e1)
