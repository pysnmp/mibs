#
# PySNMP MIB module ARISTA-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-SMI-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 12:07:16 2023
# On host fv-az1234-823 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, TimeTicks, iso, enterprises, Counter32, NotificationType, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "enterprises", "Counter32", "NotificationType", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ARISTA-SMI-MIB", arista=arista, aristaProducts=aristaProducts, aristaModules=aristaModules, aristaExperiment=aristaExperiment, aristaMibs=aristaMibs, PYSNMP_MODULE_ID=arista)
