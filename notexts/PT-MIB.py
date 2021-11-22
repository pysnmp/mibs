#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/protelevision/PT-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 11:43:49 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ModuleIdentity, Counter32, Integer32, Counter64, enterprises, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, MibIdentifier, Unsigned32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "Counter32", "Integer32", "Counter64", "enterprises", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18086))
pt.setRevisions(('2014-08-08 12:00',))
if mibBuilder.loadTexts: pt.setLastUpdated('201408081200Z')
if mibBuilder.loadTexts: pt.setOrganization('Protelevision Technologies, Denmark')
mibBuilder.exportSymbols("PT-MIB", pt=pt, PYSNMP_MODULE_ID=pt)
