#
# PySNMP MIB module CTRON-SSR-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SMI-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 12:09:08 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, NotificationType, ObjectIdentity, TimeTicks, Gauge32, Integer32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "NotificationType", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ssr = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501))
ssr.setRevisions(('2000-07-15 00:00',))
if mibBuilder.loadTexts: ssr.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssr.setOrganization('Cabletron Systems, Inc')
ssrMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1))
if mibBuilder.loadTexts: ssrMibs.setStatus('current')
ssrTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 10))
if mibBuilder.loadTexts: ssrTraps.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-SMI-MIB", ssrTraps=ssrTraps, PYSNMP_MODULE_ID=ssr, ssr=ssr, ssrMibs=ssrMibs)
