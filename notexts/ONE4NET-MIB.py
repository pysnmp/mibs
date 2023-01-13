#
# PySNMP MIB module ONE4NET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/ONE4NET-MIB
# Produced by pysmi-1.1.8 at Fri Jan 13 12:08:43 2023
# On host fv-az218-3 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Unsigned32, enterprises, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, MibIdentifier, iso, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Unsigned32", "enterprises", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "MibIdentifier", "iso", "Counter32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
one4net = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196))
one4net.setRevisions(('2002-01-12 00:00',))
if mibBuilder.loadTexts: one4net.setLastUpdated('200201120000Z')
if mibBuilder.loadTexts: one4net.setOrganization('One4net GmbH')
mibBuilder.exportSymbols("ONE4NET-MIB", one4net=one4net, PYSNMP_MODULE_ID=one4net)
