#
# PySNMP MIB module ADR63E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR63E1-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:22:48 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, TimeTicks, Counter64, Gauge32, ObjectIdentity, Unsigned32, Bits, ModuleIdentity, NotificationType, MibIdentifier, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "ModuleIdentity", "NotificationType", "MibIdentifier", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adr63e1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 18))
if mibBuilder.loadTexts: adr63e1.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr63e1.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr63e1.setContactInfo('    ')
if mibBuilder.loadTexts: adr63e1.setDescription('The MIB module specific for ADR63E1 equipment')
mibBuilder.exportSymbols("ADR63E1-MIB", adr63e1=adr63e1, PYSNMP_MODULE_ID=adr63e1)
