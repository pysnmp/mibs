#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/protelevision/PT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:47:17 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Unsigned32, TimeTicks, enterprises, MibIdentifier, Bits, Integer32, NotificationType, ModuleIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Unsigned32", "TimeTicks", "enterprises", "MibIdentifier", "Bits", "Integer32", "NotificationType", "ModuleIdentity", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18086))
pt.setRevisions(('2014-08-08 12:00',))
if mibBuilder.loadTexts: pt.setLastUpdated('201408081200Z')
if mibBuilder.loadTexts: pt.setOrganization('Protelevision Technologies, Denmark')
mibBuilder.exportSymbols("PT-MIB", PYSNMP_MODULE_ID=pt, pt=pt)
