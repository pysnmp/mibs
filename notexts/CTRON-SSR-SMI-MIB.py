#
# PySNMP MIB module CTRON-SSR-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SMI-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:42:58 2021
# On host fv-az135-680 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, ObjectIdentity, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, IpAddress, Gauge32, Integer32, Counter64, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "IpAddress", "Gauge32", "Integer32", "Counter64", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ssr = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501))
ssr.setRevisions(('2000-07-15 00:00',))
if mibBuilder.loadTexts: ssr.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssr.setOrganization('Cabletron Systems, Inc')
ssrMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1))
if mibBuilder.loadTexts: ssrMibs.setStatus('current')
ssrTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 10))
if mibBuilder.loadTexts: ssrTraps.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-SMI-MIB", ssr=ssr, PYSNMP_MODULE_ID=ssr, ssrMibs=ssrMibs, ssrTraps=ssrTraps)
