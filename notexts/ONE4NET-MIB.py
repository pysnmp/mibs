#
# PySNMP MIB module ONE4NET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/ONE4NET-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 05:34:32 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, NotificationType, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, iso, Counter32, enterprises, Counter64, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "NotificationType", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "iso", "Counter32", "enterprises", "Counter64", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
one4net = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196))
one4net.setRevisions(('2002-01-12 00:00',))
if mibBuilder.loadTexts: one4net.setLastUpdated('200201120000Z')
if mibBuilder.loadTexts: one4net.setOrganization('One4net GmbH')
mibBuilder.exportSymbols("ONE4NET-MIB", one4net=one4net, PYSNMP_MODULE_ID=one4net)
