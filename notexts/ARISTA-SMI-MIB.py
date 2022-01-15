#
# PySNMP MIB module ARISTA-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-SMI-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 16:26:42 2022
# On host fv-az126-328 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, Gauge32, ModuleIdentity, MibIdentifier, ObjectIdentity, NotificationType, Bits, Integer32, Unsigned32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Gauge32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "NotificationType", "Bits", "Integer32", "Unsigned32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arista = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065))
arista.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2008-10-27 18:30',))
if mibBuilder.loadTexts: arista.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: arista.setOrganization('Arista Networks, Inc.')
aristaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 1))
if mibBuilder.loadTexts: aristaProducts.setStatus('current')
aristaModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 2))
if mibBuilder.loadTexts: aristaModules.setStatus('current')
aristaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3))
if mibBuilder.loadTexts: aristaMibs.setStatus('current')
aristaExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 4))
if mibBuilder.loadTexts: aristaExperiment.setStatus('current')
mibBuilder.exportSymbols("ARISTA-SMI-MIB", aristaMibs=aristaMibs, aristaProducts=aristaProducts, aristaModules=aristaModules, aristaExperiment=aristaExperiment, PYSNMP_MODULE_ID=arista, arista=arista)
