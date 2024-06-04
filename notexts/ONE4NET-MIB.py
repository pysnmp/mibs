#
# PySNMP MIB module ONE4NET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/ONE4NET-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 07:51:36 2024
# On host fv-az837-21 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, enterprises, MibIdentifier, Counter64, ObjectIdentity, TimeTicks, IpAddress, Gauge32, Integer32, Bits, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "enterprises", "MibIdentifier", "Counter64", "ObjectIdentity", "TimeTicks", "IpAddress", "Gauge32", "Integer32", "Bits", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
one4net = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196))
one4net.setRevisions(('2002-01-12 00:00',))
if mibBuilder.loadTexts: one4net.setLastUpdated('200201120000Z')
if mibBuilder.loadTexts: one4net.setOrganization('One4net GmbH')
mibBuilder.exportSymbols("ONE4NET-MIB", PYSNMP_MODULE_ID=one4net, one4net=one4net)
