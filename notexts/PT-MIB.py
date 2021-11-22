#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/protelevision/PT-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:29:24 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, enterprises, iso, TimeTicks, NotificationType, ObjectIdentity, Counter32, Integer32, ModuleIdentity, MibIdentifier, Bits, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "enterprises", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "Bits", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18086))
pt.setRevisions(('2014-08-08 12:00',))
if mibBuilder.loadTexts: pt.setLastUpdated('201408081200Z')
if mibBuilder.loadTexts: pt.setOrganization('Protelevision Technologies, Denmark')
mibBuilder.exportSymbols("PT-MIB", PYSNMP_MODULE_ID=pt, pt=pt)
