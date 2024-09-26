#
# PySNMP MIB module BENU-ENTERPRISE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-ENTERPRISE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 26 02:10:49 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Gauge32, enterprises, MibIdentifier, Unsigned32, Integer32, ModuleIdentity, TimeTicks, iso, Counter32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "enterprises", "MibIdentifier", "Unsigned32", "Integer32", "ModuleIdentity", "TimeTicks", "iso", "Counter32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benu = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406))
benu.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benu.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benu.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-ENTERPRISE-MIB", PYSNMP_MODULE_ID=benu, benu=benu)
