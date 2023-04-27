#
# PySNMP MIB module CTRON-SSR-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-SMI-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:35:30 2023
# On host fv-az988-178 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Counter32, ObjectIdentity, IpAddress, Integer32, Unsigned32, ModuleIdentity, NotificationType, MibIdentifier, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "Unsigned32", "ModuleIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ssr = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501))
ssr.setRevisions(('2000-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ssr.setRevisionsDescriptions(('Update contact information for Riverstone Networks as this mib\n          is found on the Riverstione RS product line and Enterasys SSR product line.',))
if mibBuilder.loadTexts: ssr.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssr.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ssr.setContactInfo('Enterasys Networks\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@enterasys.com\n     http://www.enterasys.com')
if mibBuilder.loadTexts: ssr.setDescription('This mib module defines enterprise MIBs under Cabletron\n         enterprise OID that manage Enterasys SmartSwitch Routers \n         and Riverstone Networks RS product Line.')
ssrMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1))
if mibBuilder.loadTexts: ssrMibs.setStatus('current')
if mibBuilder.loadTexts: ssrMibs.setDescription('All Smart Switch Router (SSR) enterprise MIBs are defined under mibs')
ssrTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 10))
if mibBuilder.loadTexts: ssrTraps.setStatus('current')
if mibBuilder.loadTexts: ssrTraps.setDescription('All enterprise traps are defined under this branch.')
mibBuilder.exportSymbols("CTRON-SSR-SMI-MIB", ssrMibs=ssrMibs, ssrTraps=ssrTraps, PYSNMP_MODULE_ID=ssr, ssr=ssr)
