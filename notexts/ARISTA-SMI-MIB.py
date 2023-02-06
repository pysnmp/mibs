#
# PySNMP MIB module ARISTA-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  6 14:20:30 2023
# On host fv-az442-130 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Unsigned32, iso, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, NotificationType, Bits, Counter64, ModuleIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "NotificationType", "Bits", "Counter64", "ModuleIdentity", "MibIdentifier", "Gauge32")
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
mibBuilder.exportSymbols("ARISTA-SMI-MIB", PYSNMP_MODULE_ID=arista, arista=arista, aristaProducts=aristaProducts, aristaMibs=aristaMibs, aristaExperiment=aristaExperiment, aristaModules=aristaModules)
