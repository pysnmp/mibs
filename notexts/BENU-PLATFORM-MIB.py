#
# PySNMP MIB module BENU-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:21:20 2022
# On host fv-az130-744 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, Bits, Counter64, ModuleIdentity, ObjectIdentity, TimeTicks, Unsigned32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Bits", "Counter64", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatform = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1))
benuPlatform.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatform.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benuPlatform.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-MIB", benuPlatform=benuPlatform, PYSNMP_MODULE_ID=benuPlatform)
