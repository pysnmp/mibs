#
# PySNMP MIB module CTRON-SSR-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SMI-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 09:23:17 2023
# On host fv-az581-610 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, Integer32, Bits, TimeTicks, MibIdentifier, Counter32, NotificationType, IpAddress, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Integer32", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "NotificationType", "IpAddress", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ssr = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501))
ssr.setRevisions(('2000-07-15 00:00',))
if mibBuilder.loadTexts: ssr.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssr.setOrganization('Cabletron Systems, Inc')
ssrMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1))
if mibBuilder.loadTexts: ssrMibs.setStatus('current')
ssrTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 10))
if mibBuilder.loadTexts: ssrTraps.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-SMI-MIB", PYSNMP_MODULE_ID=ssr, ssr=ssr, ssrTraps=ssrTraps, ssrMibs=ssrMibs)
